# MIT 6.S081 (xv6) 操作系统实验笔记

> 🎯 课程：MIT 6.S081 Operating System Engineering
> 📝 内容：xv6 源码分析 + Lab 题解 + 操作系统核心概念

---

## 目录

- [参考资料](#参考资料)
- [第一章 进程和内存](#第一章-进程和内存)
  - [Lab 1: Unix Utilities](#lab-1-unix-utilities)
    - [rm.c](#rmc)
    - [sleep.c](#sleepc)
    - [pingpong](#pingpong)
    - [primes.c](#primesc)
    - [find.c](#findc)
    - [xargs.c](#xargsc)
- [第二章 操作系统核心概念](#第二章-操作系统核心概念)
  - [Lab 2: 系统调用](#lab-2-系统调用)
    - [trace](#trace)
    - [sysinfo](#sysinfo)
- [第三章 虚拟内存](#第三章-虚拟内存)
  - [Lab 3: 页表](#lab-3-页表)
    - [print a page table](#print-a-page-table)
    - [a kernel page table per process](#a-kernel-page-table-per-process)
    - [simplify copyin/copyinstr](#simplify-copyincopyinstr)

---

## 参考资料

| 资源 | 链接 |
|------|------|
| MIT 6.1810 Lab 全解（掘金专栏） | [链接](https://juejin.cn/column/7276350321094082614) |
| 28天速通 6.S081 总结（知乎） | [链接](https://zhuanlan.zhihu.com/p/632281381) |
| 课程中文翻译文档 | [链接](https://mit-public-courses-cn-translatio.gitbook.io/mit6-s081/lec08-page-faults-frans/8.2-lazy-page-allocation) |
| 最全汇总文档（GitHub） | [链接](https://github.com/PiperLiu/CS-courses-notes/blob/master/notes/mit6.s081/README.md#课程资料) |



---

## 第一章 进程和内存

##### 内核

xv6 采用了传统的宏内核（Monolithic Kernel）形式，内核本身就是一个特殊的程序，为其他运行的程序提供服务 。**你未来要写的驱动代码，就是直接嵌在这个“特殊程序”里运行的。**

##### 用户空间与内核空间

进程在用户空间和内核空间中交替执行 。平时写的普通 C++ 或 Java 程序都在“用户空间”玩耍；而一旦你要操作底层硬件，就必须通过**系统调用 (System call)** 跨越边界，进入拥有最高权限的“内核空间” 



进程并不只存在于应用层（用户空间），它实际上是在用户空间和内核空间中交替执行的。



##### 核心系统调用一览

| 系统调用 | 功能 | 关键点 |
|----------|------|--------|
| `open()` | 创建文件描述符 | 返回一个指向打开文件的 fd（文件描述符） |
| `exit(status)` | 进程停止执行并释放资源 | `0` = 成功，`1` = 失败 |
| `wait(&status)` | 等待子进程终止 | 返回终止子进程的 PID，并将子进程退出状态写入 `&status` |
| `exec(path, argv)` | 用新程序**替换**当前进程 | 不创建新 PID，不返回（除非失败） |

##### exec 的三个关键特性

| 特性 | 说明 |
|------|------|
| **不创建新进程** | PID 不变（5 号进程 exec 后仍是 5 号），但"灵魂"被替换 |
| **内存大清洗** | 代码段、数据段、堆栈全部抹掉，从硬盘加载新二进制 |
| **通常不返回** | 成功时当前进程已不存在，没有地方可返回；只有失败时才返回 |

#### fork + exec 结合使用

```c
//写一个forkexec.c：fork then exec
#include "user/user.h"
int main()
{
    int pid,status;
    pid=fork()
    if(pid == 0)
    {
        //子进程
        char *argv[]={"echo","THIS","IS","ECHO",0};
        exec("echo",argv);
        printf("exec failed !\n");//只有exec运行失败才会运行这一行和下一行
        exit(1);
    }
    else
    {
        printf("parents waiting\n");
        wait(&status);
        peintf("the child exited with status %d\n",status);
    }
    exit(0);
}
```



#### 理解文件重定向

理解操作系统中万物皆文件，操作系统内核一开始就会有三个默认的文件描述符

0：对应标准输入，默认连接到键盘

1：对应标准输出，默认连接到屏幕

2：对应标准错误，默认连接到屏幕



```c
//redirect.c:run a command with output redirected
int main()
{
    int pid;
    pid = fork()
    {
        if(pid == 0)
        {
            close(1);//关闭标准输出(通常指向屏幕)，此时，文件描述符1变为未分配状态
            open("output.txt",O_WRONLY|O_CREATE);//打开或创建文件，由于内核总是分配最小的可用描述符，此时刚释放的1会被分配给output.txt
            char *argv[]={"echo","this","is","redirected","echo",0};
            exec("echo",argv);
            //echo启动并执行时，他会调用write(1,...)将字符发送到1号描述符，但由于1号管已经接到out.put.txt上,echo以为自己在往屏幕上打印，实际上数据全部流向了文件，也可以看出程序本身完全不需要知道重定向的存在，这正是文件描述符抽象的强大之处。
            printf("exec failed!\n")
            exit(1);
        }
        else
        {
            wait((int *)0);
        }
        exit(0);
    }
    
}
```



shell 中提供了方便的 I/O 重定向工具：

```bash
$ echo hello > out
$ cat < out
hello
```

---

## Lab 1: Unix Utilities

### rm.c

从rm.c的源码中可以看出，

* 最常见的int main(int argc,char *argv[]),其中的**agrc是参数的数目，argv则是一个数组容纳参数**，**第一个参数一定是echo**，然后才是内容。例如echo hello world 这一行命令，argc=3,而且argv[0]=echo ,argv[1]=“hello”,argv[2]=“world”

* 0是标准输入，1是标准输出，2是标准错误，对于rm.c如果传入参数过少或者删除有问题的话会把错误信息直接输出到**文件描述符2**，fprintf(2,“rm failed to dalete”);

* 在底层机制中Unix文件系统，删除文件的系统调用叫unlink(取消链接)

   原因在于在Unix的底层：

  1.数据和名字是分开的：文件在硬盘上存东西的地方是Inode(索引节点)，而在目录里看到的那个文件名只是一个指向Inode的链接。

  2.多对一的关系：允许多个不同的文件名指向同一个Inode，这就叫硬链接。

  3.unlink的真实动作：当rm调用unlink(“a.txt”)时，**内核其实并没有去硬盘上把文件的数据抹掉，它只是把a.txt这个名字从目录树里摘掉，然后把Inode的被链接次数减去1**

  

* 文件数据什么时候才真正删除(回收磁盘空间)呢：

  只有满足以下两个条件时：

  1.它的链接数减到了0(所有指向它的文件名都被unlink了)

  2.没有任何一个正在运行的进程打开着这个文件(文件的引用计数为0)

  

### sleep.c

* 需求：为 xv6 实现 UNIX 程序 sleep; 您的 sleep 应该暂停用户指定个数的 tick。tick 是由 xv6 内核定义的时间概念，即来自计时器芯片的两次中断之间的时间。您的解决方案应该在 user/sleep.c 文件中。

* The solution

  系统调用sleep(int)只接收一个整形参数，故要对通过命令行传入的参数个数进行判断，确认为一个之后还要判断其是否能转换为整数。



```c
#include "kernel/types.h"
#include "user/user.h"
int main(int argc,char *argv[])
{

    if(argc<2)
    {
        printf("no argument\n");

    }
    else if(argc >2)
    {
        printf("Excessive argument\n");

    }//上面是确保输入sleep后紧跟的是一个数字来表示时间
    else
    {
        int tag =1;
        char *p = argv[1];//明确指针的含义，这里的*p指的是argv[1]所指的第一位的地址作为开始的地址
        while (*p)//*p指的是在上面那个argv[1]的第一位，只有当读到内容最后结束\0的时候直接退出循环，因为\0的ASCLL码正好是0
        {
            if(*p<'0'||*p>'9')
            {
                tag = 0;
                break;
            }
            p++;//读内容的位数一点点往后加，读完第一位读第二位这种一直读下去
        }
        if ((tag))
        {
            sleep(atoi(argv[1]));//通过上面的循环是为了确保sleep后面的内容完全是数字，这样
            //传给atoi的也只是argv[1]的地址，atoi函数会自动从argv[1]的地址自己循环到末位\0
            //然后将这串字符算成一个整数返回
        }
        else
        printf("Illegal argument\n");    

    }
    exit(0);
}
```

### pingpong



需求：编写一个程序，使用 UNIX 系统调用通过一对管道(每个方向一个管道)在两个进程之间 "ping-pong" 传递一个字节。父进程应该向子进程发送一个字节; 子进程应该打印`<pid>: received ping`，其中 `<pid>` 是它的进程号，将管道上的字节写入父进程，然后退出; 父进程应该从子进程读取字节，打印`<pid>: received pong`，然后退出。您的解决方案应该在user/pingpong.c.文件中。

**代码流程：**首先创建父进程和子进程，然后创建两个管道Parent_fd和Child_fd，父进程向子进程发送“Ping”,子进程打印，然后子进程向父进程发送“Pong”，然后父进程打印，注意read，pipe，write的用法

* 需要注意的是例如Parent_fd[0]是读端，Parent_fd[1]是写端。



```c
#include "kernel/types.h"
#include "user/user.h"
int main(int argc,char *argv[])
{
    
    int Parent_fd[2];
    int Child_fd[2];
    pipe(Parent_fd);
    pipe(Child_fd);
    char buf[20]={0};
    int pid =fork();
    if(pid<0)
    {
        fprintf(2,"fork error\n");
        exit(1);
    }
    else if(pid == 0)//子进程
    {
        close(Parent_fd[1]);
        read(Parent_fd[0],buf,4);
        printf("%d:receive %s\n",getpid(),buf);
        close(Parent_fd[0]);
        write(Child_fd[1],"Pong",4);
        exit(0);
        
    }
    else
    {
        close(Parent_fd[0]);
        write(Parent_fd[1],"Ping",4);
        
        close(Child_fd[1]);
        read(Child_fd[0],buf,4);
       
        printf("%d:receive %s\n",getpid(),buf);
        exit(0);
    }
        
    
}
```



```c
#include "kernel/types.h"
#include "user/user.h"

int main(int argc ,char *argv[])
{
    int pid;
    int Parent_pd[2];
    int Child_pd[2];
    pipe (Parent_pd);
    pipe (Child_pd);
    char buf[20]={0};
    pid = fork();
    {
        if ((pid < 0))
        {
            fprintf(2,"fork error\n");
            exit(1);
        }
        else if (pid == 0)
        {
            close( Parent_pd[1]);
            read(Parent_pd[0],buf,4);
            printf("%d :receive %s\n",getpid(),buf);
            close(Child_pd[0]);
            write(Child_pd[1],"pong",4);
            exit(0);

        }
        else
        {
            close(Parent_pd[0]);
            write(Parent_pd[1],"ping",4);
            close(Child_pd[1]);
            read(Child_pd[0],buf,4);
            printf("%d:received %s",getpid(),buf);
            exit(0);
        }
    }
}
```



### primes.c

**需求：**

用管道写一个并发版本的素数筛（由 Unix 管道发明者 Doug McIlroy 提出），解决方案在 `user/primes.c`。参考：[说明页](http://swtch.com/~rsc/thread/)

**核心思路：递归管道链**

```
main: 将 2~35 写入管道 p
  │
  ▼
get_prime(p):
  ├─ 读出第一个数 n（一定是素数）→ 打印
  ├─ 创建新管道 p2
  ├─ fork 子进程 → 递归调用 get_prime(p2)（下一级过滤器）
  └─ 父进程：把 p 中剩余数中不能被 n 整除的 → 写入 p2
                                │
                                ▼
                      get_prime(p2):
                        读出第一个数 → 打印
                        再过滤传给 p3...
```

**逐步拆解：**

| 步骤 | 操作 | 说明 |
|------|------|------|
| **1. 初始化** | `main` 把 2~35 写入管道 `p` | 第一个管道装满候选数字 |
| **2. 取素数** | `get_prime(p)` 读管道第一个数 `n` | 管道中第一个数一定是素数，打印它 |
| **3. 建新管** | 创建新管道 `p2`，fork 子进程 | 子进程拿 `p2` 递归，父进程负责过滤 |
| **4. 过滤** | 父进程遍历 `p` 中剩余数 | 不能被 `n` 整除的数写入 `p2`（传给下一级） |
| **5. 递归** | 子进程调用 `get_prime(p2)` | 回到步骤 2，用新管道继续筛，直到管道空 |

> 💡 **关键理解**：`p1` 和 `p2` 不是全局变量，而是**局部变量**。每个 `get_prime()` 调用都有自己的 `p1`（从参数传入，负责接收）和 `p2`（新建，负责传给下一级），就像左手接、右手传，层层递归形成过滤器链。

![1.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3718ab145a44d248e387f64f0a44299~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=885&h=539&s=27474&e=png&b=ffffff)



```c
#include "kernel/type.h"
#include "user/user.h"

void get_prime(int p1[2])
{
    close(p1[1]);
    int n;
    int tag = read(p1[0],&n,4);
    if(tag =0)
    {
        close(p1[0]);
        exit(0);
    }
    printf("prime %d\n",n);
    int p2[2];
    pipe(p2);
    int pid =fork();
    {
        if(pid == 0)
        {
            get_prime(p2);
            
        }
        else if(pid>0)
        {
            int m;
            while(read(p1[0],&m,4))
            {
                if(m%n)
                {
                    write(p2[1],&m,4);
                }
            }
        }
        close(p1[1]);
        close(p2[0]);
        close(p2[1]);
        wait(0);
        
            
    }
    else
    {
        printf("fork error\n");
        exit(pid);
    }
    exit(0);
}


int main()
{
    int p[2];
    pipe(p);
    int i;
    for(i=2;i<35;i++)
    {
        write(p[1],&i,4);
    }
    get_prime(p);
    exit(0);
}



```



```c
#include "kernel/types.h"
#include "user/user.h"
void get_prime(int p1[2])
{
    close(p1[1]);
    int n;
    int tag = read(p1[0],&n,4);//将从管道读取到的第一个数字传给n地址存储，read是消耗性的，read之后第一个数字就被拿走了
    if(!tag)//这是没读到数据
    {
        close(p1[0]);
        exit(0);
    }
    printf("prime %d\n",n);
    int p2[2];
    pipe(p2);
    int pid =fork();
    if ((!pid))//子进程
    {
        get_prime(p2);
    }
    else if ((pid>0))//父进程
    {
        int m;
        while (read(p1[0],&m,4))
        {
            if ((m%n))
            {
                write(p2[1],&m,4);
            }   
        }
        close(p1[0]);
        close(p2[1]);//这个关掉p2[1]正好给了下一轮的while(read(p2[0],&m,4))信号，意思是已经关闭写端，已经写完了，可以读了
        close(p2[0]);//父进程并没用到往p2中读数据所以关掉

        wait(0);//回收子进程
    }
    else
    {
        printf("fork error\n");
    }
    return;
}
int main()
{
    int p[2];
    pipe (p);
    for (int i = 2 ; i <= 35; i++)
    {
        write(p[1],&i,4);//这里的4指的是i的长度，以为i定义为int，一个整数占4个字节，用sizeof()也可以自动计算大小

    }//相当于把这串数字都写入管道
    get_prime(p);
    exit(0); 
}

```



### find.c



```c
#include "kernel/types.h"
#include "kernel/fcntl.h"
#include "kernel/fs.h"
#include "kernel/stat.h"
#include "user/user.h"

char* get_name(char* path)//为了提取地址路径中的最后一部分
{
    char*p;//要理解指针对应的是地址
    for(p=path+strlen(path);p>=path&&*p!='/';p--);
    p++;
    return p;
}

void find(char *path,char *str)
{
    char buf[512];
    struct dirent de;
    struct stat st;
    int fd = open(path,0);
    if(fd<0)
    {
        fprintf(2,"find:cannot open %s\n",path);
        return;
    }
    if(fstat(fd,&st)<0)
    {
        fprintf(2,"find cannot stat %s\n",path);
        close(fd);
        return;
    }
    switch(st.type)
    {
        case T_DEVICE:
        case T_FILE://普通文件
            if(!strcmp(str,get_name(path)))
                printf("%s\n",path);
            break;
        case T_DIR://目录
            strcpy(buf,path);//目录放到buf中
            char *p=buf+strlen(buf);//此时指针p正好指向字符串末尾的那个\0
            *p='/';//将末尾的\0直接覆盖成了/
            p++;//指针指向了斜杠后的空位
            while(read(fd,&de,sizeof de)== sizeof de)//通过这个循环来保证每次抽取文件夹中的一行
            {
                if(de.ium == 0)
                    continue;//看档案袋上的编号如果是0说明是空袋子或者已经被销毁了，continue回到while开头
                memmove(p,de.name,DIRSIZ);
                p[DIRSIZ]=0;//有效的目录就在原本p指向的地址的/后面直接加文件名，也就是在buf上记下了它的绝对地址，这个0是在末尾画个句号，表示写完了
                if(stat(buf,&st)<0)//将buf信息放到st结构体中
                {
                    printf("ls:cannot stat %s\n",buf);
                    continue; 
                }
                if(st.type == T_DEVICE||st.type == T_FILE)
                {
                    if(!strcmp(str,get_name(buf)))
                        printf("%s\n",buf);//设备文件或者普通文件
                }
                else if(st.type == T_DIR&&strcmp(".",get_name(buf))&&strcmp("..",get_name(buf)))
                    find(buf,str);
            }//如果还是目录文件并且保证名字不是.也不是..的情况下，再次重复上面的操作find，进行递归
            break;
    }
    close(fd);
    return;
}


int main(int argc,char *argv[])
{
    if(argc != 3)
    {
        fprintf(2,"usage:find [directory][target filename]\n");
        exit(1);
    }
    find(argv[1],argv[2]);
    exit(0);
}


```



### xargs.c



编写一个简单版本的 UNIX xargs 程序:它的参数描述要运行的命令，它从标准输入中读取行，并为每一行运行命令，将该行附加到命令的参数中。您的解决方案应该在 user/xargs.c 文件中。

例如：cat abc.txt |xargs grep hello

其中abc.txt中存了两行字

f1.txt 

f2.txt

`cat abc.txt` 开始运行，把 `f1.txt\n` 和 `f2.txt\n` 倒进了系统的管道（标准输入）里。

`xargs` 开始运行，操作系统给 `main(int argc, char *argv[])` 传进来的初始参数是：

- `argc` = **3**
- `argv[0]` = `"xargs"`
- `argv[1]` = `"grep"`
- `argv[2]` = `"hello"`

p=[“grep”,”hello”,[512字节空内存],0]

此时传给 `exec` 的真实参数是：

- 你要执行谁：`"grep"` (也就是 `argv[1]`)
- 你的任务清单是：`["grep", "hello", "f1.txt", 0]`

于是，**子进程变成了 `grep hello f1.txt` 并开始执行**。父进程（xargs）走到 `else wait(0)` 躺下睡觉。



 **决定性瞬间（第二次 fork + exec）** 父进程再次 `fork` 出新的子进程。 此时传给 `exec` 的真实参数变成了：

- 你要执行谁：`"grep"`

- 任务清单：`["grep", "hello", "f2.txt", 0]`

- 代码走到：

  ```
  if(p[argc-1][0] == 0) break;
  ```

  

  条件成立！父进程终于跳出了 `while` 循环。



父进程 `xargs` 功成身退，完美谢幕。终端再次出现了等待你输入命令的 `$` 提示符。

```c
#include "kernel/types.h"
#include "user/user.h"
#include "kernel/param.h"
int main(int argc,char *argv[])
{
    char *p[MAXARG];
    int i;
    for(i=1;i<argc;i++)//因为原本argv[0]是xargs,因此将argv数组统一向前挪一位构成p
    {
        p[i-1]=argv[i];
    }
    p[argc-1]=malloc(512);//将p加一位是512空间的仓库
    p[argc]=0;//将p数组封底，用0直接结尾，p = ["grep", "hello", [512字节空内存], 0]
    while(gets(p[argc-1],512))//gets函数自己会一次读一行
    {
        if(p[argc-1][0]==0)//仓库的第一位如果是0则停止
        {
            break;
        }
        if(p[argc-1][strlen(p[argc-1])-1]=='\n')
            p[argc-1][strlen(p[argc-1])-1]=0;//因为gets会把前面的数据输入末尾自动加上\n
        if(fork()==0)
            exec(argv[1],p);//这个argv[1]是要执行的命令，p是我们刚才的数组
        //对于exec的使用规则：首先第一位argv[1]这个位置应该是要执行的命令的名字或者路径
        //p这个数组要求p[0]是这个命令名，p的最后一位是0
        else
            wait(0);
        
    }
    exit(0);
}
```



---

## 第二章 操作系统核心概念

### 抽象物理资源

> 🎯 **操作系统的首要任务**：不能让一个 bug 导致整个系统崩溃。如果程序直接运行在硬件上（没有内核），一个死循环或错误的内存写入就能让电脑彻底死机。

**核心思想：**

| 概念 | 说明 |
|------|------|
| **强隔离** | 把用户程序关在名为"进程"的笼子里，禁止应用直接访问敏感硬件资源 |
| **抽象化** | 将硬件资源（如磁盘）抽象为服务（如文件系统），通过系统调用访问 |
| **进程抽象 CPU** | 应用程序不能直接与 CPU 交互，只能与进程交互；内核负责在不同进程间切换 CPU |
| **分时复用** | 单 CPU 不能同时运行多个进程，而是运行一个进程一段时间，再切换到另一个 |
| **ELF 格式** | 可执行程序在不运行时，只是磁盘上的一个 ELF 格式二进制文件 |

### 用户模式、主管模式与系统调用

##### RISC-V CPU 三种权限模式

| 模式 | 权限 | 说明 |
|------|------|------|
| **机器模式 (Machine)** | 完全特权 | 最高权限，通常用于固件/引导 |
| **主管模式 (Supervisor)** | 部分特权 | 内核运行在此模式，可执行特权指令（如读写页表寄存器、开关中断） |
| **用户模式 (User)** | 无特权 | 应用程序运行在此受限模式，执行特权指令会触发切换 |

> 💡 用户模式下的应用尝试执行特权指令时，CPU 会**拒绝执行**并切换到主管模式。

##### ecall 指令：受控地请求内核服务

应用不能随意进入内核，必须通过 `ecall` 指令切换到内核指定的入口点。以 `fork()` 为例：

```
用户态调用 fork()
    │
    ▼
usys.S 汇编层：将 SYS_fork 编号(1) 放入 a7 寄存器，执行 ecall
    │
    ▼
内核 syscall() 分发：读取 a7 中的编号 → 查路由表 → 调用 sys_fork()
```

> 📌 **所有系统调用（如 write）都遵循同样的流程**：用户函数 → ecall 指令（携带系统调用编号） → syscall() 分发 → 内核实现函数。应用程序**不能直接调用**内核中的函数。

### 内核组织架构

| 架构 | 特点 | 优点 | 缺点 |
|------|------|------|------|
| **单体内核 (Monolithic)** | 整个 OS 运行在主管模式，全硬件特权 | 模块协作方便（如文件系统和虚拟内存共享缓存） | 任一模块错误都致命，导致内核崩溃 |
| **微内核 (Microkernel)** | 大部分 OS 功能作为用户态进程，内核只负责 IPC 和底层功能 | 隔离性好，单模块崩溃不影响内核 | 上下文切换开销大，性能偏低 |

> 📌 **xv6 采用单体内核设计**，与大多数 Unix 系统一致。

### xv6 源码目录结构

| 目录/文件 | 内容 |
|-----------|------|
| **kernel/** | 内核源代码：系统调用分发、进程管理、内存映射、磁盘驱动等核心逻辑 |
| **user/** | 用户态代码：ls、sh、grep 等工具，以及系统调用接口的用户库 |
| **头文件** (`user/user.h`, `kernel/defs.h`) | 定义用户态↔内核态、内核模块间的交互契约 |



### 进程概览

进程是xv6的隔离单位，防止进程破坏内核，也防止进程之间破坏彼此的内存、CPU

| 概念 | 说明 |
|------|------|
| **地址空间** | 每个进程有独立的**页表**，定义该进程的地址空间 |
| **进程状态结构体** | 内核为每个进程维护一个结构体，记录 PID、状态（运行/休眠/僵尸等）、页表地址、内核栈 |
| **双栈机制** | 每个进程有**用户栈**（运行普通代码）和**内核栈**（执行系统调用时使用），两栈隔离，防止用户程序破坏内核逻辑 |



### xv6 启动过程

**启动流程：**

> 🔌 QEMU 加载 xv6 内核代码到物理内存 `0x80000000`，将 CPU 指令指针（PC）指向此处，把控制权正式交给 xv6。



---

## Lab 2: 系统调用

### trace — 系统调用追踪

[(26 封私信 / 8 条消息) MIT 6.S081 Operating System  - 知乎](https://zhuanlan.zhihu.com/p/625526955)



我们要实现一个监控函数 trace，和 Lab 1 的函数不一样，这个涉及用户层和内核层。

具体执行流程：



在终端输入命令： trace 32 grep hello

这一行命令的含义是使用trace程序跟踪我的在执行grep hello 过程中的read操作

**第一天：登记监控（设置 Trace）**

1.我们在user/user.h中定义trace函数原型 int trace(int);

执行命令之后程序会把参数32放入a0寄存器，将22(SYS_trace)放入a7寄存器

2.进入内核之后会首先触发kernel/syscall.c 中的syscall函数

内核一看：`num = p->trapframe->a7;` （此时 `num` 是 22）。

内核去查路由表，执行 `sys_trace()`。

`sys_trace()` 把 32 写进了进程的小本本：`p->tracemask = 32;`。

3.执行完sys_trace()之后又回到syscall()中,判断 `if(p->tracemask & (1<<num))` 会执行吗？

- 此时 `num` 是 22，`1<<22` 肯定和 32 对不上，所以**不打印**。
- 程序退回用户态。第一天结束。

**【关键点】：这一步之后，`a7` 里的 22 就没用了！但进程的 `p->tracemask` 永远记住了 32。**

**第二天：真正干活（执行 Read）**

壳子程序通过 `exec` 变成了真正的 `grep` 程序。`grep` 开始去硬盘上读取文件了。它要调用 `read`。

1. **用户态重新填写菜单：** `grep` 程序把文件描述符、缓冲区地址放入寄存器，然后**把菜单号 `5`（`SYS_read`）放入 `a7`！**
2. 再次触发 `syscall` 函数

内核一看：`num = p->trapframe->a7;` **（注意！此时因为用户发起了全新的请求，`a7` 里面装的是 5！所以 `num` 变成了 5）**。

内核然后会跳转执行 `sys_read()` 帮你读文件。

文件读完了，准备返回，此时走到了你的探头代码：

**探头发挥作用：**

```
// 此时 num = 5
if(p->tracemask & (1<<num)) 
```

- 内核翻开这个进程的小本本，`p->tracemask` 里面写的是昨天存进去的 **32**。
- 算一下钥匙：`1 << 5`，结果正好也是 **32**。
- `32 & 32`，条件完全成立！
- 砰！探头触发，执行 `printf` 打印日志：`syscall read -> ...`

```c
void
syscall(void)
{
  int num;
  struct proc *p = myproc();

  num = p->trapframe->a7;
  if(num > 0 && num < NELEM(syscalls) && syscalls[num]) {
    // Use num to lookup the system call function for num, call it,
    // and store its return value in p->trapframe->a0
    p->trapframe->a0 = syscalls[num]();//返回值存在a0寄存器内
    if(p->tracemask & (1<<num))//判断是否需要trace这个系统调用
    {
      printf("%d:syscall %s -> %d\n",p->pid,sysnames[num],(int)p->trapframe->a0);
    }
  } else {
    printf("%d %s: unknown sys call %d\n",
            p->pid, p->name, num);
    p->trapframe->a0 = -1;
  }
}

```

```c
uint64
sys_trace(void)
{
  int trace_sys_mask;
  argint(0,&trace_sys_mask);//将a0寄存器中的值给trace_sys_mask

  myproc()->tracemask|=trace_sys_mask;
    //等同于myproc()->tracemask = myproc()->tracemask | trace_sys_mask;
  return 0;

}
```



### sysinfo — 系统状态



我们要新增一个系统调用 sysinfo，它收集系统的信息。，系统调用拿一个参数指向结构体sysinfo。内存应该填满该结构体的字段，结构体内容包括可用内存字节数和未被使用状态的进程数量。



#### 获取空闲内存字节数

从 `kernel/kalloc.c` 了解物理内存管理机制：

| 概念 | 说明 |
|------|------|
| **页面大小** | `PGSIZE = 4096` 字节 |
| **数据结构** | 空闲内存页用**单链表**管理（`kmem.freelist` 指向第一个空闲页） |
| **内存初始化** | `kinit()` 定义整个 xv6 的物理内存地址空间 |
| **计算方法** | 从 `kmem.freelist` 出发，遍历链表，每页 +4096，累加即得总空闲内存 |

> 📌 遍历时需要 `acquire(&kmem.lock)` 上锁，防止数据竞态。

```c
//kalloc.c里面， 这个是要加的函数
uint64
kfreemem(void)
{
    struct run *r;
    uint64 free =0;
    acquire(&kmem.lock);//上锁。防止数据竞态
    r=kmem.freelist;//将内存空间的开头的地址内容给r的值空间
    while(r)
    {
        free += PGSIZE;//每一页固定4096字节
        r = r->next;//遍历单链表
        //这个r->next是指的是存的下一页的地址，r->next在从r开始的前八个字节
        //这里指的是将前八个字节存的内容也就是下一页的地址给r的值空间
    }
    release(&kmem.lock);
    return free;
}
```



加一个在kalloc.c中的kfree函数(物理内存释放函数)

```c
void kfree(void *pa)
{
    struct run *r;
    if(((uint64)pa%PGSIZE)!=0||(char*)pa < end||(uint64)pa>= PHYSTOP)
        panic("kfree");
    memset(pa,1,PGSIZE);
    r=(struct run*)pa;
    acquire(&kmem.lock);
    r->next = kmem.freelist;//将当前第一个空闲页的地址抄到我们刚回收的next上，相当于原本的空闲页的内存放在回收的页内存后边了
    kmem.freelist = r;//当前第一个空闲页的地址更新为我们刚刚回收的这个页的地址r
    release(&kmem.lock);
}
```



#### 获取已分配进程数量

理解 xv6 进程管理相关的两个核心文件：

| 文件 | 层级 | 职责 |
|------|------|------|
| **kernel/proc.c** | 内核底层 | 进程管理大本营：分配/回收进程结构体、状态管理、CPU 调度切换、父子关系处理（孤儿进程接管）、`fork()`/`exit()`/`wait()` 的真正底层实现 |
| **kernel/sysproc.c** | 系统调用接口层 | 用户↔内核的桥梁，用户程序通过它发请求。包含 `sys_fork()`、`sys_getpid()`、`sys_sleep()` 等 |

> 📌 用户程序**不能直接调用** `proc.c` 中的函数，必须通过系统调用 → `sysproc.c` 转发。

**进程数组**：`proc.c` 开头定义了 `struct proc proc[NPROC]`（`NPROC=64`），xv6 静态分配最多 64 个进程的存储空间，即最多同时运行 64 个进程。通过遍历此数组，统计 `state != UNUSED` 的进程即可得到已分配进程数。

```c
//kernel/proc.c
//来监控有多少个进程空着
uint64
count_free_proc(void)
{
    struct proc *p;
    uint64 count =0;
    for(p=proc;p<&proc[NPROC];p++)//从第一个进程到最后一个进程
    {
        acquire(&p->lock);
        if(p->state != UNUSED)
        {
            count +=1;
        }
        release(&p->lock);
    }
    return count;
}

```



#### 将数据拷贝到用户态 buffer



xv6的用户态和内核态的数据并不能直接交互，需要使用copyout函数来将内核态的数据拷贝到用户态地址上，来看一下copyout的函数签名

```c
// 从内核态拷贝到用户态
// 拷贝len字节数的数据, 从src指向的内核地址开始, 到由pagetable下的dstv用户地址
// 成功则返回 0, 失败返回 -1
int
copyout(pagetable_t pagetable, uint64 dstva, char *src, uint64 len)
```

写出sysinfo函数调用内核函数：

```c
//kernel/sysproc.c
//collect system info
uint64
sys_sysinfo(void)
{
    struct proc *my_proc = myproc();
    uint64 p;
    if(argaddr(0,&p)<0) //获取用户提供的buffer地址
        return -1;
    struct sysinfo s;//先在内核生成包含信息的结构体
    s.freemem = kfreemem()
    s.nproc = count_free_proc();
    //把这个struct复制到用户态地址里去
    if(copyout(my_proc->pagetable,p,(char *)s,sizeof(s))<0)
        return -1;
    return 0;
    
}
```



---

## 第三章 虚拟内存


> 🎯 **虚拟内存的核心目标**：实现**隔离性** — 每个用户程序都装入盒子，与内核和其他程序相互独立。

**问题场景（没有虚拟内存时）：**

假设 cat 程序出现错误，将内存地址 1000（Shell 的起始地址）加载到寄存器 a0，执行 `sd $7, (a0)` 将 7 写入地址 1000 → **cat 破坏了 Shell 的内存镜像，隔离性被破坏。**

![](./xv6.assets/image.png)

> ⚠️ 不同程序共享同一物理内存，一个程序的错误就能破坏其他程序。

**解决方案：**

![](./xv6.assets/image-1779153494438-2.png)

给每个程序（包括内核）分配**专属的虚拟地址空间**：

![](./xv6.assets/image (1).png)

- 每个程序在自己的地址空间从 0 到 n 独立运行
- 不同程序的地址互不影响
- 通过**页表**将虚拟地址映射到物理内存的不同区域



### 页表的基本原理

> 💡 **核心问题**：如何在**同一个物理内存**上创建不同的地址空间？→ 使用**页表**。

##### 地址翻译流程

```
虚拟地址 (VA)
    │
    ▼
┌──────────────┬──────────┐
│   index      │  offset  │
│ (查找 page)  │ (页内偏移)│
└──────────────┴──────────┘
    │                │
    ▼                ▼
MMU 查页表       直接拷贝 12bit
    │
    ▼
物理 page 号 (PPN) + offset = 物理地址 (PA)
```

##### 核心概念

| 概念 | 说明 |
|------|------|
| **MMU** | 内存管理单元，**硬件电路**，在处理器中完成虚拟→物理地址翻译 |
| **页表 (Page Table)** | 虚拟地址 ↔ 物理地址的映射表，保存在内存中 |
| **SATP 寄存器** | RISC-V CPU 中的寄存器，存放当前进程页表在物理内存中的地址 |
| **以 Page 为单位** | 不是为每个地址建条目，而是为每个 **page（4096 字节）** 建一条条目 |
| **进程切换** | 切换进程时必须同时切换 SATP 寄存器，指向新进程的页表 |
| **地址结构** | 虚拟地址 = **index**（查找 page）+ **offset**（页内第几个字节） |

##### MMU 翻译步骤

1. 读取虚拟地址中的 **index** → 查页表获取物理 page 号
2. 读取虚拟地址中的 **offset** → 确定页内偏移
3. **物理地址 = page 起始地址 + offset**



**RISC-V的虚拟内存地址都是64bit**，因为RISV-V的寄存器是64bit的，但是实际上，在我们使用的RISC-V处理器上，并不是所有的64bit都被使用了，也就是高25bit并没有被使用。这样的结构是限制了虚拟内存地址的数量，虚拟内存地址的数量现在只有2^39个，大概是512GB。如果最新的处理器支持更大的地址空间，只需要将未使用的25bit拿出来做虚拟内存的一部分即可。

**在剩下的39bit中，有27bit被用来当作index，也就是有2^27个page，12bit被用来当作offset。offset必须是12bit，因为对应了page的4096个字节。**

![](./xv6.assets/image-1779180682275-5.png)



在RISC-V中，**物理内存地址是56bit**，其中44bit是物理page号(PPN，Physical Page Number)，剩下12bit是offset完全继承自虚拟内存地址（也就是地址转换时，只需要将虚拟内存中的27bit翻译成物理内存中的44bit的page号，剩下的12bitoffset直接拷贝过来即可）。

**物理内存中的一个page里的4096个字节是连续的**，

学生提问：我们从CPU到MMU之后到了内存，但是**不同的进程之间的怎么区别**？比如说Shell进程在地址0x1000存了一些数据，ls进程也在地址0x1000也存了一些数据，我们需要怎么将它们翻译成不同的物理内存地址。

Frans教授：SATP寄存器包含了需要使用的**地址转换表的内存地址**。所以ls有自己的地址转换表，cat也有自己的地址转换表。**每个进程都有完全属于自己的地址转换表。**



### 页表的三级映射

<img src="./xv6.assets/image (2).png" style="zoom:80%;" />

**这个是页表三级映射的图**

这个**EXT**是扩展位，L2,L1,L0都是index(page号),offset是在这一个page中具体哪个位置

L2,L1,L0都是9bit，如果要是单层直接映射的话，那对应2^9个page

但是这个三级映射的话，这里的这个L2不能直接对应2^9个page

**而是L2应该索引页表**，L2索引了最高级页目录中的2^9个页表项(PTE),每个页表项(条目)占是八个字节，所以一个Directory page有512个条目，**因此一个directory是4096个字节，大小和一个page是一样的**

**每个页表项(条目)是8个字节，每个字节等于8bit，因此每个页表项是64bit**，在图中也可以看到：

这个Reserved是高10位，目前硬件不使用，保留给未来的架构升级或者给操作系统做一些特殊的标记。

这个Flags是标志位，**V(Valid,第0位)是有效位**，这个是最重要的一位，如果V为0，说明这个PTE是空的，无论里面存了什么PPN硬件都不会管，直接抛出Page Fault(缺页异常)。只有V为1，硬件才会继续查。

**R,W,X：**读、写和执行权限，需要知道的特点就是一旦R=0且W=0且X=0，说明这个PTE是一个路标(页目录)，它的PPN指向下一级页表。

只要R、W、X中有任何一个为1，说明这个PTE是终点，PPN指向的是真正的物理数据内存。

**物理页号PPN：**

**占据了44个bit，负责存储下一级页表或者最终物理数据页的物理基地址(去掉末尾12个0之后的部分)**

**如L2中的PPN存储的是L1的物理基地址**



对于**不同的进程**，他们的虚拟地址是一样的，但都是相当于在自己的小世界里

他们对应的物理地址肯定是不同的，因此要看页表映射具体操作：

当启动一个新进程时，操作系统做的第一件事就是去物理内存的空闲池里，找一块干净的4KB物理页，

**这个4KB物理页就被正式任命为这个新进程的最高级页目录**，两个不同的进程的L2页表的物理内存地址是不同的，

因此，当执行进程A切换到执行进程B时，**操作系统调度器会把进程B的L2页表的物理基地址，硬塞到CPU的satp寄存器中**，这是关键，这样整个硬件MMU（内存管理单元）查字典的入口完全变了。



### 页表缓存（TLB）

| 概念 | 说明 |
|------|------|
| **为什么需要 TLB** | 单次虚拟地址寻址需读取 3 次内存（三级页表），代价太高 |
| **TLB 是什么** | 页表缓存（Translation Lookaside Buffer），缓存最近使用的虚拟地址翻译结果（本质是 PTE 的缓存） |
| **TLB 如何工作** | 再次访问同一虚拟地址时，**直接从 TLB 获取物理地址**，无需重新走页表 |
| **MMU vs walk 函数** | MMU（硬件电路）负责日常高频查表，快如闪电；`walk()` 函数（软件）负责建表和内核越权查用户物理地址 |

> 📌 MMU 是芯片中的**逻辑电路**，不是内存。它不执行软件指令，靠纯粹物理电路逻辑进行地址翻译。

### 内核页表（Kernel Page Table）

下图展示了内核地址空间的映射关系：

- **左边**：内核的虚拟地址空间
- **右边上半部分**：物理内存（DRAM）
- **右边下半部分**：I/O 设备

当操作系统启动时，从地址 `0x80000000` 开始运行。RISC-V 处理器有 4 个核，每个核都有自己的 MMU 和 TLB。

![](./xv6.assets/image (4).png)

> 📌 **主板地址路由规则**：虚拟→物理地址翻译后：
> - 物理地址 **≥ 0x80000000** → 走向 **DRAM 芯片**（内存）
> - 物理地址 **< 0x80000000** → 走向 **I/O 设备**



---

## Lab 3: 页表

硬件设备的物理地址(MMIO)

在RISC-V架构中，外设是通过内存映射输入输出(MMIO)来控制的。这意味着读写某段特定的内存地址，实际上是在向硬件设备发送或读取数据。



```c
#define UART0 0×10000000L //串口控制器地址(用于屏幕打印和键盘输入)
//kernel/memlayout.h
#define KERNBASE 0×80000000L//物理内存的起点
//UART0：指向串口，操作系统要想在屏幕上打字，就把字符往0×10000000这个地方送
//QEMU模拟器启动时，会把xv6内核的代码加载到物理地址0×80000000
```



### print a page table — 打印页表

第一个实验是比较简单的, 给定一个page table, 要求递归地打印出它所映射到的**3**层page table下所有存在的**PTE** (Page Table Entry).



```c
void vmprint_helper(pagetable_t pagetable ,int depth)
{
    static char* indent[]={
        ""
        ".. "
        ".. .."
        ".. .. .."
    };
    if(depth <=0||depth >=4)
    {
        panic("vmprit_helper: depth not in {1,2,3}");
    }
    for(int i=0;i<512;i++)
    {
        pte_t pte =pagetable[i];
        if(pte&PTE_V)
        {
            printf("%s%d:pte:%p pa %p \n",indent[depth],i,pte,PTE2PA(pte));
            if((pte&(PTE_R|PTE_W|PTE_X))==0)
            {
                uint64 child = PTE2PA(pte);//这个PTE2PA(pte)是将pte中的PPN取出
                vmprint_helper((pagetable_t)child,depth+1);//递归，深度加了一层
            }
        }
    }
}

void vmprint_helper(pagetable_t pagetable)
{
    printf("page table %p\n",pagetable);
    vmprint_helper(pagetable,1);
}
```



### a kernel page table per process — 进程专属内核页表

> 🧠 **底层真相**：无论上层怎么花哨，所有进程的运行最终都是 CPU 顺着电线、通过物理总线，去内存条上抓取指令和读写数据的。

##### 背景：虚拟地址 → 物理地址的必经之路

| 概念 | 说明 |
|------|------|
| **进程** | 操作系统包装的概念，物理内存里实际装的是程序的代码段、数据段和栈空间 |
| **虚拟地址** | 进程使用的地址（为隔离性和安全），CPU 不能直接使用 |
| **MMU** | 硬件电路，将虚拟地址翻译为物理地址后 CPU 才能访问内存 |
| **程序逻辑在哪执行** | 在 CPU 芯片内部的硬件电路里（PC 寄存器→取指电路→ALU 译码执行） |

##### CPU 内部核心部件

```
PC 寄存器（存虚拟地址）
    │
    ▼
取指电路 ——通过 MMU 查页表→ 物理内存条抓取机器指令
    │
    ▼
ALU + 译码器 —— 晶体管电路解析指令、通电/断电算出结果
```

##### 页表在什么时候起作用

| 场景 | 机制 |
|------|------|
| **用户态执行** | CPU 取指令/读变量时，硬件 MMU **强制**看**用户页表**翻译地址 |
| **内核态执行**（系统调用触发） | 内核切换 `stap` 寄存器，CPU 看**内核页表**翻译地址 |

##### 为什么要做这个实验

| 对比 | 没有专属内核页表（原 xv6） | 有专属内核页表（本实验目标） |
|------|--------------------------|---------------------------|
| **问题** | 内核态下无法识别用户空间的虚拟地址（如 `buf=0x1000`） | 将用户页表映射**提前复制**到专属内核页表 |
| **做法** | 每次系统调用都要调用 `walk()` 去查用户页表 → 极度低效 | 内核态直接通过硬件 MMU 拿到用户物理内存 |
| **结果** | 每次系统调用都耗费大量 CPU | 一次复制，后续直接访问，高效 |

##### 专属内核页表的合并结构

```
┌──────────────────────────────────┐
│ 高地址区：抄自全局内核页表        │ ← 保证内核能访问硬件（UART0等）
│ (外设、内核代码 0x80000000 以上)  │
├──────────────────────────────────┤
│ 低地址区：抄自用户页表            │ ← 保证内核能”看穿”用户指针
│ (用户变量/代码 0~0x600000)        │
└──────────────────────────────────┘
```

> 📌 硬件 MMU 只认**三级映射**，不管这是用户页表还是内核页表。只要 CPU 顺着 `stap` 寄存器去查，它就会把虚拟地址拆成 L2/L1/L0 三段逐级查找。

然后因为用户页表的虚拟地址都是从0开始往上的(比如0到00600000这一段低地址)，而内核的代码和硬件外设都存放在非常高的地址(比如0×80000000以上)。

这样低地址和高地址刚好互不冲突

于是，内核在软件层面上，把用户页表低地址的那些PTE(页表项条目)一行行复制下来，强行贴到这个专属内核页面的低地址空白页。

**【最终的合体专属内核页表（三级页表）】**
┌──────────────────────────────────────────────┐
│ 高地址区：完全抄自全局内核表 (外设、内核代码)   │ ───> 保证内核自己能活、能管硬件
├──────────────────────────────────────────────┤
│ 零和低地址区：抄自用户页表 (用户的变量/Hello)  │ ───> 保证内核能“开天眼”秒杀用户指针
└──────────────────────────────────────────────┘



#### 为 struct proc 加入新字段

```c
#kernel/proc.h
//per-process state
struct proc
{
    ......
    uint64 tracemask; //the syscalls this proc is tracing
    pagetable_t kpagetable;//the kernel table per process 专属内核页
};
```

#### 在 allocproc 中分配专属内核页



```c
#kernel/vm.c
//add a mapping to the per-process kernel pagetable
void ukvmapp(pagetable_t kpagetable ,uint64 va,uint64 pa,uint64 sz,int perm)
{
    if(mappages(kpagetable,va,sz,pa,perm)!=0)
    {
        panic("ukvmmap");
    }
}
pagetable_t ukvminit()
{
    pagetable_t kpagetable =(pagetable_t) kalloc();
    if(kpagetable == 0)
    {
        return kpagetable;
    }
    memset(kpagetable,0,PGSIZE);
    ukvmmap(kpagetable,UART0,UART0,PGSIZE,PTE_R|PTE_W);
    ukvmmap(kpagetable,VIRTIO0,PGSIZE,PTE_R|PTE_W);
    ukvmmap(kpagetable,CLINT,CLINT,0x10000,PTE_R|PET_W);
    ukvmmap(kpagetable,PLIC,PLIC,0x400000,PTE_R|PTE_W);
    ukvmmap(kpagetable,KERNBASE,KERNBASE,(uint64)etext-KERNBASE,PTE_R|PTE_X);
    ukvmmap(kpagetable,(uint64)etext,(uint64)etext,PHYSTOP-(uint64)etext,PTE_R|PTE_W);
    ukvmmap(kpagetable,TRAMPOLINE,(uint64)trampoline,PGSIZE,PTE_R|PTE_X);
    return kpagetable;

    //一本包含该进程，包含所有公共内核硬件设施的全新三级页表树做好了
}
```



allocproc函数

```c
#kernel/proc.c
static struct proc*
allocproc(void)
{
    ...
found:
    p->pid =allocpid();
    ...
    p->pagetable = proc_pagetable(p);
    if(p->pagetable == 0)
    {
        freeproc(p);
        release(&p->lock);
        return 0;
    }
    p-<kpagetable = ukvminit();
    if(p->kpagetable == 0)
    {
        freeproc(p);
        release(&p->lock);
        return 0;
    }
    
    uint64 va = KSTACK((int)(p-proc));
    pte_t pa =walkaddr(kernel_pagetable,uint64 va);
    memset((void*)pa,0,PGSIZE);
    ukvmmap(p->k_pagetable,va,(uint64)pa,PGSIZE,PTE_R|PTE_W);
    P->ksta
    ...
}
```

#### 在 scheduler 切换进程时刷新 TLB
，刷新TLB和使用的虚拟-物理页表影射base,注意在进程切换跑完返回后，要重新切换回全局的kernel page

```c
#kernel/proc.c
void scheduler(void)
{
    struct proc *p;
    struct cpu *c=mycpu();
    c->proc =0;
    for(;;)
    {
        intr_on;
        int found = 0;
        for(p=proc;p<&proc[NPROC];p++)
        {
            acquire(&p->lock);
            if(p->state == RUNNABLE)
            {
                p->state =RUNNING;
                c->proc =p;
                w_satp(MAKE_SATP(p->kpagetable));
                //这是CPU将进程专属内核页表地址塞到CPU内部的satp寄存器里
                sfence_vma();//清理缓存，避免CPU为了偷懒把之前的大内核页表的对应关系直接拿来用
                swtch(&c->context,&p->context);
                //把CPU从调度器的内核处转到目标进程的内核处
                kvminithart();//切换回全局内核表
                c->proc=0;
                found =1;
            }
            release(&p->lock);
        }
    }
}
```

#### 销毁进程时回收内核页表
，这里需要注意的是，我们并不需要去回收内核页表所映射的物理地址，因为那些物理地，例如device mapping，是全局共享的，进程专属内核表只是全局内核表的一个复制，但是间接映射所消耗的物理内存是需要回收的，举个例子，在kernel pagetable可能有这样一个三级映射：

0x 810 (第一级) -> 0x 910 (第二级) -> 0x 1100(第三级) -> 0x 10000000L **UART0**

我们是需要把**0x 810**, **0x 910**, **0x 1100** 回收的, 但是**UARTO**不需要回收因为是共享的.

```c
#kernel/vm.c
void ukvmunmap(pagetable_t pagetable,uint64 va, uint64 npages)
{//从指定的L0页表中解除一部分虚拟内存页的映射，并清空对应的L0页表项PTE，va是要解除映射的起始虚拟地址
    //npages是要解除映射的页面数量
    uint64 a;
    pte_t *pte;
    if((va%PGSIZE)!=0)//检查起始虚拟地址va是否是页大小的整数倍
    {
        //如果不是，则直接触发panic崩溃提示。
        panic("ukvmunmap:not aligned");
    }
    for(a=va;a<va+npages*PGSIZE;a+=PGSIZE)
    {
        //从va开始，以PGSIZE为步长进行循环，直至把npages个页面都处理完，变量a代表当前正在处理的虚拟地址。
        if((pte=walk(pagetable,a,0)) == 0)//通过walk可以直接给出a对应的L0页表行
            goto clean;
        //调用walk函数，在多级页表中查找虚拟地址a对应的页表项(PTE)指针，第三个参数0表示如果中途的页表目录不存在，不要创建新的页表。walk返回0说明这个虚拟地址没有对应的底层页表结构，说明它本来就没被映射，直接跳转clean
        if((*pte&PTE_V)==0)
            goto clean;
        //如果找到了页表项，但该项的有效位PTE_V为0，说明这个虚拟页面当前没有映射到物理内存
        if(PTE_FLAGS(*pte)==PTE_V)
            //说明这个PTE只有PTE_V标志而没有读写执行等其他权限标志，表明它是指向下一级页表目录(L2或者L1)，而不是具体的物理页(L0)，系统会触发panic
            panic("ukvmunmap:not a leaf");
        clean:
            *pte = 0;//这个pte指的是直接映射到物理内存的那个页表项
    }
}

void ufreewalk(pagetable_t pagetable)
{//这个函数是删掉了三级页表本身所占的物理内存
    for(int i =0;i<512;i++)
    {
        pte_t pte = pagetable[i];
        if((pte&PTE_V)&&(pte&(PTE_R|PTE_W|PTE_X))==0)
            //判断既要有效还不能有读写执行权限，所以肯定是L2或者L1而不能是L0
        {
            uint64 child = PTE2PA(pte);//取出下一级的物理地址
            ufreewalk((pagetable_t)child);//用下一级递归
            pagetable[i]=0;
        }
        pagetable[i]=0;//页表中每行都为0
    }
    kfree((void*)pagetable);//回收页表本身所占的4096字节的内存
}

void freeprockvm(struct proc* p)
{
    pagetable_t kpagetable = p->kpagetable;
    ukvmunmap(kpagetable,p->kstack,PGSIZE/PGSIZE);
    ukvmunmap(kpagetable,(uint64)etext,(PHYSTOP-(uint64)etext)/PGSIZE);
    ukvmunmap(kpagetable,KERNBASE,((uint64)etext-KERNBASE)/PGSIZE);
    ukvmunmap(kpagetable,PLIC,0x400000/PGSIZE);
    ukvmunmap(kpagetable,CLINT,0x10000/PGSIZE);
    ukvmunmap(kpagetable,VIRTIO0,PGSIZE/PGSIZE);
    ukvmunmap(kpagetable,UART0,PGSIZE/PGSIZE);
    //ukvmunmap函数是将最底层的L0页表的对应行给清零了
    ufreewalk(kpagetable);
    //将这三级页表里的内容都擦干净了，而且将页表所占的物理内存也回收了。
      
}



# kernel/proc.c
// free a proc structure and the data hanging from it,
// including user pages.
// p->lock must be held.
static void
freeproc(struct proc *p)
{
  if(p->trapframe)
    kfree((void*)p->trapframe);
  p->trapframe = 0;
  if(p->pagetable)
    proc_freepagetable(p->pagetable, p->sz);
  p->pagetable = 0;
  p->sz = 0;
  p->pid = 0;
  p->parent = 0;
  p->name[0] = 0;
  p->chan = 0;
  p->killed = 0;
  p->xstate = 0;
  p->state = UNUSED;
  if (p->kpagetable) {
    freeprockvm(p);//释放专属内核页表
    p->kpagetable = 0;//将指向内存的指针变为0
  }
  if (p->kstack) {
    p->kstack = 0;
  }
}
```



### simplify copyin/copyinstr — 简化内核态拷贝

> 🎯 **目标**：利用上一步的专属内核页表，将用户页表的映射关系**实时同步**到专属内核页表，让内核态直接通过硬件 MMU 访问用户内存，省掉 `walk()` 的软件查表开销。

| 要点 | 说明 |
|------|------|
| **复制什么** | 把用户页表的前半段（低地址区）原封不动复制到专属内核页表 |
| **为什么要一致** | `pagetable` 和 `kpagetable` 前半段映射必须时刻同步，内核态才能直接用硬件寻址 |
| **同步时机** | `fork()`、`sbrk()`、`exec()` 等导致页表增长/缩减的地方，都要同步更新 `kpagetable` |

首先写一个 helper 函数，将一段内存映射从 `pagetable` 复制到 `kpagetable`：



```c
#kernel/vm.c
//这个函数是建立起了虚拟内存地址和物理内存地址的映射关系
int umappages(pagetable_t pagetable,uint64 va,uint64 size,uint64 pa,int perm)
{
    uint64 a,last;
    pte_t *pte;
    
    a=PGROUNDDOWN(va);
    //原版mappages如果发现va不是4096(页大小)的倍数会直接报错崩溃，但在这里PGROUNDDOWN会向下取整到当前页的起始边界，这就允许你传入非对齐的地址，它会自动帮你找到对应的整页
    last = PGROUNDDOWN(va+size-1);//计算最后需要映射的一页的起始地址
    for(;;)//一直循环
    {
        if((pte=walk(pagetable,a,1))==0)//顺着多级页表往下找，寻找虚拟地址a对应的底层pte的地址
            return -1;
        *pte=PA2PTE(pa)|perm|PTE_V;
        //不检查原来有没有映射，直接用当前的物理地址pa转换为PTE格式，拼上要求的权限perm，再强制打上有效标记PTE_V，然后直接覆盖写进去
        if(a==last)
            break;
        //如果当前处理的地址a已经等于计算出的最后一页地址last，说明所有要求的内存页已经映射完毕，跳出循环。
        a += PGSIZE;
        pa +=PGSIZE;
    }
    return 0;
    
}
//这个函数是来解决我们知道虚拟内存地址，但是不知道这个虚拟内存地址对应的实际的物理地址，因为物理内存地址
int pagecopy(pagetable_t oldpage,pagetable_t newpage,uint64 begin,uint64 end)
{
    pte_t *pte;
    uint64 pa,i;
    uint flags;
    begin = PGROUNDUP(begin);
    //将传入的起始虚拟地址begin向上取整，对齐到页面的边界(4096的倍数)，为了确保我们每次处理的都是一个完整的页面
    for(i=begin;i<end;i+=PGSIZE)
    {
        if((pte=walk(oldpage,i,0))==0)//提取旧页表中对应的最底层页表L0的pte
            panic("pagecopy walk oldpage nullptr");
        if((*pte&PTE_V)==0)//判断页表项是不是有效的
            panic("pagecop y oldpage pte not valid");
        pa=PTE2PA(*pte);//将这个页表项中的物理地址提取出来
        flags=PTE_FLAGS(*pte)&(~PTE_U)//把Uflags抹去，把用户态可访问权限给抹除
        if(umappages(newpage,i,PGSIZE,pa,flags)!=0)
        {
            geto err;
        }
    }
    return 0;
    
err://如果出现错误，则解除映射
    uvmunmap(newpage,0,i/PGSIZE,1);
    return -1;
    
}
```



刚写的pagecopy函数只做到将oldpage的一段范围抄到newpage中，并且把用户权限涂黑，将权限升级到内核态

紧接着, 我们在**fork()**, **exec()**, **sbrk()** 和**userinit()**的相应位置进行**pagetable**和**kpagetale**的同步.




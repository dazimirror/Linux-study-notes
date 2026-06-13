# Linux 系统编程学习笔记

> 📅 学习时间：2026年2月 - 4月  
> 🎯 目标：快速过完 Linux 系统编程核心概念

---

## 目录

- [第一章 环境搭建](#第一章-环境搭建)
  - [安装 VMware 和 Ubuntu](#安装-vmware-和-ubuntu)
  - [安装必要软件](#安装必要软件)
- [第二章 Linux 基本命令](#第二章-linux-基本命令)
  - [文件与目录操作](#文件与目录操作)
    - [ls — 列出目录及文件名](#ls-—-列出目录及文件名)
    - [cd — 切换目录](#cd-—-切换目录)
    - [pwd — 显示当前目录](#pwd-—-显示当前目录)
    - [mkdir — 创建新目录](#mkdir-—-创建新目录)
    - [cp — 复制文件或目录](#cp-—-复制文件或目录)
    - [rm — 删除文件或目录](#rm-—-删除文件或目录)
    - [mv — 移动文件与目录](#mv-—-移动文件与目录)
    - [chmod — 修改文件或目录的权限](#chmod-—-修改文件或目录的权限)
  - [压缩与磁盘管理](#压缩与磁盘管理)
    - [tar — 打包压缩](#tar-—-打包压缩)
    - [df — 查看磁盘空间](#df-—-查看磁盘空间)
- [第三章 GCC 编译与库](#第三章-gcc-编译与库)
  - [GCC 编译四步骤](#gcc-编译四步骤)
    - [编译流程示例](#编译流程示例)
  - [静态库](#静态库)
  - [动态库（共享库）](#动态库共享库)
  - [Makefile 与 CMake](#makefile-与-cmake)
    - [Makefile 核心要素](#makefile-核心要素)
    - [Makefile 示例](#makefile-示例)
    - [CMake 简介](#cmake-简介)
- [第四章 文件 I/O](#第四章-文件-i/o)
  - [系统 I/O（open / close / read / write / lseek）](#系统-i/oopen-/-close-/-read-/-write-/-lseek)
    - [open() — 打开文件](#open-—-打开文件)
    - [close() — 关闭文件](#close-—-关闭文件)
    - [open/close 基本示例](#open/close-基本示例)
    - [write() — 写入文件](#write-—-写入文件)
    - [read() — 读取文件](#read-—-读取文件)
    - [lseek() — 设置文件读写位置](#lseek-—-设置文件读写位置)
    - [综合示例：文件的写、读、定位操作](#综合示例：文件的写、读、定位操作)
    - [实战：用 read 和 write 实现 cp 命令](#实战：用-read-和-write-实现-cp-命令)
  - [系统 I/O vs 标准 I/O 对比](#系统-i/o-vs-标准-i/o-对比)
  - [缓冲区机制](#缓冲区机制)
    - [用户缓冲区（User Buffer）](#用户缓冲区user-buffer)
    - [内核缓冲区（Kernel Buffer / Page Cache）](#内核缓冲区kernel-buffer-/-page-cache)
    - [缓冲区数据何时写入设备？](#缓冲区数据何时写入设备？)
  - [标准 C I/O（fopen / fclose / fwrite / fread / fseek）](#标准-c-i/ofopen-/-fclose-/-fwrite-/-fread-/-fseek)
    - [fopen() — 打开文件](#fopen-—-打开文件)
    - [fclose() — 关闭文件](#fclose-—-关闭文件)
    - [fopen/fclose 基本示例](#fopen/fclose-基本示例)
    - [fwrite() — 写入文件](#fwrite-—-写入文件)
    - [fread() — 读取文件](#fread-—-读取文件)
    - [fseek() — 设置文件位置](#fseek-—-设置文件位置)
    - [标准 I/O 综合示例](#标准-i/o-综合示例)
    - [write 与 fwrite 的区别](#write-与-fwrite-的区别)
- [第五章 进程管理](#第五章-进程管理)
  - [进程概念](#进程概念)
    - [为什么需要进程？](#为什么需要进程？)
    - [并发 vs 并行](#并发-vs-并行)
  - [Linux 父子进程](#linux-父子进程)
  - [fork 创建子进程](#fork-创建子进程)
    - [fork 函数](#fork-函数)
    - [fork 基本示例](#fork-基本示例)
  - [进程终止与等待](#进程终止与等待)
    - [进程终止方式](#进程终止方式)
    - [waitpid — 等待子进程终止](#waitpid-—-等待子进程终止)
    - [示例：父进程等待子进程终止](#示例：父进程等待子进程终止)
  - [exec 系列函数](#exec-系列函数)
    - [示例：fork + execl 结合使用](#示例：fork-+-execl-结合使用)
  - [实战：保活进程（Monitor）](#实战：保活进程monitor)
    - [第一步：创建被监控程序 hello](#第一步：创建被监控程序-hello)
    - [第二步：实现保活程序 monitor](#第二步：实现保活程序-monitor)
- [第六章 进程间通信（IPC）](#第六章-进程间通信ipc)
  - [概述：为什么需要 IPC](#概述：为什么需要-ipc)
    - [Linux IPC 方式一览](#linux-ipc-方式一览)
  - [匿名管道（Anonymous Pipe）](#匿名管道anonymous-pipe)
    - [pipe() 函数](#pipe-函数)
    - [示例一：父子进程单向通信（父→子）](#示例一：父子进程单向通信父→子)
    - [示例二：父子进程双向通信（双管道模拟全双工）](#示例二：父子进程双向通信双管道模拟全双工)
  - [命名管道（FIFO）](#命名管道fifo)
    - [mkfifo() 函数](#mkfifo-函数)
    - [示例一：父子进程通过 FIFO 通信](#示例一：父子进程通过-fifo-通信)
    - [示例二：非亲缘进程通过 FIFO 通信（独立进程）](#示例二：非亲缘进程通过-fifo-通信独立进程)
    - [匿名管道 vs 命名管道 对比](#匿名管道-vs-命名管道-对比)
    - [FIFO 与普通文件的区别](#fifo-与普通文件的区别)
  - [共享内存（Shared Memory）](#共享内存shared-memory)
    - [shm_open() — 创建或打开共享内存对象](#shm_open-—-创建或打开共享内存对象)
    - [ftruncate() — 设置共享内存大小](#ftruncate-—-设置共享内存大小)
    - [mmap() — 将共享内存映射到进程地址空间](#mmap-—-将共享内存映射到进程地址空间)
    - [munmap() — 解除共享内存映射](#munmap-—-解除共享内存映射)
    - [shm_unlink() — 删除共享内存对象](#shm_unlink-—-删除共享内存对象)
  - [消息队列（Message Queue）](#消息队列message-queue)
    - [mq_open() — 创建或打开消息队列](#mq_open-—-创建或打开消息队列)
    - [mq_send() / mq_receive() — 发送和接收消息](#mq_send-/-mq_receive-—-发送和接收消息)
    - [mq_close() — 关闭消息队列](#mq_close-—-关闭消息队列)
    - [mq_unlink() — 删除消息队列](#mq_unlink-—-删除消息队列)
    - [示例一：父子进程通过消息队列通信](#示例一：父子进程通过消息队列通信)
    - [示例二：独立进程间传递结构体数据](#示例二：独立进程间传递结构体数据)
  - [信号（Signal）](#信号signal)
    - [信号的基本用法](#信号的基本用法)
  - [信号量（Semaphore）](#信号量semaphore)
    - [sem_open() — 创建或打开信号量](#sem_open-—-创建或打开信号量)
    - [sem_close() — 关闭有名信号量](#sem_close-—-关闭有名信号量)
    - [sem_unlink() — 删除有名信号量](#sem_unlink-—-删除有名信号量)
    - [sem_wait() / sem_trywait() — 等待信号量](#sem_wait-/-sem_trywait-—-等待信号量)
    - [sem_post() — 增加信号量值](#sem_post-—-增加信号量值)
    - [示例：共享内存 + 信号量实现同步](#示例：共享内存-+-信号量实现同步)
  - [IPC 总结与选型指南](#ipc-总结与选型指南)
- [第七章 多线程编程](#第七章-多线程编程)
  - [为什么需要线程](#为什么需要线程)
  - [核心线程函数](#核心线程函数)
  - [线程互斥锁（Mutex）](#线程互斥锁mutex)
    - [核心函数](#核心函数)
    - [互斥锁使用示例](#互斥锁使用示例)
  - [条件变量（Condition Variable）](#条件变量condition-variable)
    - [核心函数](#核心函数)
- [第八章 xv6](#第八章-xv6)


## 学习计划

结合小智的文档快速过完系统编程的基本概念，然后去做飞书的相机项目。

---

## 第一章 环境搭建

### 安装 VMware 和 Ubuntu

安装虚拟机 VMware 和操作系统 Ubuntu。

<img src="./日常记录.assets/image-20260227161359940-1772180059056-1-1772180064658-3-1772180067621-5.png" alt="image-20260227161359940" style="zoom:67%;" />

- 系统密码：`123456`
- Ubuntu 用户名密码同样为：`123456`

![image-20260227164200401](./日常记录.assets/image-20260227164200401.png)

### 安装必要软件

安装飞书、VPN 和 MATLAB。

---

## 第二章 Linux 基本命令

### 文件与目录操作

#### ls — 列出目录及文件名

ls -l    列出详细信息

![image-20260309155845878](./日常记录.assets/image-20260309155845878.png)

如图所示：第一位指的是文件类型，d表示目录，-表示普通文件，c表示字符设备，b表示块设备

第一位之后的九位，以三位为一个单元，分别表示文件所有者、所属用户组、其他用户的文件使用权限，rwx分别为读，写，执行权限

#### cd — 切换目录

- `cd ~` / `cd .` / `cd ..`

#### pwd — 显示当前目录

- 直接执行 `pwd`

#### mkdir — 创建新目录

- `mkdir dirname`

#### cp — 复制文件或目录

- `cp filename dirname` — 复制文件到目录
- `cp filename1 filename2` — 复制文件1并重命名为文件2
- `cp -a dirname1 dirname2` — 复制目录1及其下所有文件到目录2
- `cp -r dirname1 dirname2` — 递归复制目录1到目录2

#### rm — 删除文件或目录

- `rm filename` / `rm -r dirname`

#### mv — 移动文件与目录

- `mv file1 file2 location` — 将文件1和文件2移动到目标位置

#### chmod — 修改文件或目录的权限

- 操作码设置权限：`chmod 764 file`，设置文件权限为 `rwxrw-r--`

### 压缩与磁盘管理

#### tar — 打包压缩

- **压缩（gzip 方式）**：`tar zcvf spacefile.tar.gz hello.c nihao.c`
- **单独压缩**：`gzip filename` → 生成 `filename.gz`
- **压缩（bzip2 方式）**：`tar jcvf spacefile.tar.bz2 hello.c nihao.c`
- **解压**：将 `c` 改为 `x`
  - `tar jxvf spacefile.tar.bz2` — 解压 bzip2 压缩包
  - `tar zxvf spacefile.tar.gz` — 解压 gzip 压缩包

#### df — 查看磁盘空间

- 默认以 1KB 为单位，数字很大，可读性差
- `df -h` 会自动换算成 GB、MB、KB 等易读单位

---

## 第三章 GCC 编译与库

### GCC 编译四步骤

GCC 编译的四个步骤：**预处理 → 编译 → 汇编 → 链接**

| 步骤 | 动作 | 说明 |
|------|------|------|
| 1. 预处理 | 展开宏、头文件，替换条件编译，删除注释/空行/空白 | `gcc -E` |
| 2. 编译 | 检查语法规范，**消耗时间和系统资源最多** | `gcc -S` |
| 3. 汇编 | 将汇编指令翻译成机器指令 | `gcc -c` |
| 4. 链接 | 数据段合并，地址回填 | `gcc -o` |



![image-20260310140238224](./日常记录.assets/image-20260310140238224.png)

#### 编译流程示例

**分步编译：**

```bash
# 编译生成目标文件（.o 文件）
gcc -c hello.c -o hello.o

# 链接目标文件生成可执行文件
gcc hello.o -o hello
```

**一步到位：**

```bash
gcc hello.c -o hello
```

**运行：**

```bash
./hello
```

**指定头文件路径：**

```bash
gcc -I ./hellodir hello.c -o hello
```

> `-I` 参数指定 hello.c 程序中头文件所在位置。

### 静态库

> 💡 **库是为了提高代码的复用效率。**

**静态库特点：**
- 对空间要求低，对时间要求高
- 在编译阶段库文件**完整复制**到程序中
- 如果库文件 100MB + 运行程序 10KB → 编译后占用 **100MB + 10KB**

静态库的生成是对目标文件（.o 文件）进行操作：

```bash
# 编译各源文件为目标文件
gcc -c add.c -o add.o
gcc -c sub.c -o sub.o
gcc -c div1.c -o div1.o

# 生成静态库（名字以 lib 开头，以 .a 结尾）
ar rcs libmymath.a add.o sub.o div1.o

# 使用静态库编译
gcc test.c libmymath.a -o a.out
./a.out
```

```c
// add.c — 加法函数
int add(int a, int b)
{
    return a + b;
}
// sub.c、div1.c 结构类似
```

```c
// test.c — 调用静态库中的函数
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

int add(int, int);
int sub(int, int);
int div1(int, int);  // 函数声明

int main(int argc, char *argv[])
{
    int a = 9, b = 3;
    printf("%d + %d = %d\n", a, b, add(a, b));
    printf("%d - %d = %d\n", a, b, sub(a, b));
    printf("%d / %d = %d\n", a, b, div1(a, b));
    return 0;
}
```

### 动态库（共享库）

**动态库特点：**
- 对时间要求低，对空间要求高
- 在编译阶段库文件仅**记录库引用**
- 如果库文件 100MB + 运行程序 10KB → 编译后占用 **仅 10KB**

> 📌 **核心区别**：静态库在编译时完整复制，动态库在运行时动态加载。

动态库也是对 .o 文件进行操作：

```bash
# 编译为目标文件（-fPIC 使函数与位置无关，挂上 @plt 标识等待动态绑定）
gcc -c add.c -o add.o -fPIC
gcc -c sub.c -o sub.o -fPIC
gcc -c div1.c -o div1.o -fPIC

# 制作动态库（lib库名.so）
gcc -shared -o libmymath.so add.o sub.o div1.o

# 编译可执行程序（-l 指定库名，-L 指定库路径）
gcc test.c -o a.out -l mymath -L ./lib

# 运行
./a.out
```

**运行时加载错误分析与解决：**

| 组件 | 工作阶段 | 所需参数 |
|------|---------|---------|
| 连接器 (Linker) | 链接阶段 | `-l` 和 `-L` |
| 动态链接器 (Dynamic Linker) | 程序运行阶段 | 动态库所在目录位置 |

**解决方法：** 通过环境变量指定动态库路径：

```bash
export LD_LIBRARY_PATH=./lib
```

### Makefile 与 CMake

Makefile 主要用于大型项目管理中。

#### Makefile 核心要素

**1 个规则：**

规则的格式为：`目标 : 依赖条件`

1. 目标的时间必须晚于依赖条件的时间，否则更新目标
2. 依赖条件如果不存在，找寻新的规则去产生依赖条件
3. `ALL`：指定 Makefile 的终极目标

**2 个函数：**

```makefile
src = $(wildcard ./*.c)
# 匹配当前工作目录下的所有 .c 文件，将文件名组成列表，赋值给变量 src
# 用 src 代指 add.c, sub.c, div1.c
```

```makefile
obj = $(patsubst %.c, %.o, $(src))
# 将参数3中包含参数1的部分替换成参数2
# 用 obj 代指 add.o, sub.o, div1.o
```

**3 个自动变量：**

| 变量 | 含义 |
|------|------|
| `$@` | 在规则命令中表示规则中的目标 |
| `$<` | 将依赖条件列表中的依赖依次取出，套用模式规则 |
| `$^` | 表示规则中的所有条件，组成列表（以空格隔开），有重复项则去重 |

#### Makefile 示例

遍历当前路径下所有的 .c 文件：

```makefile
CC = gcc
SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)

hello: $(OBJS)
	$(CC) $^ -o $@

%.o: %.c
	$(CC) -c $< -o $@

clean:
	rm -f $(OBJS) hello
```

**规则解释：**

- `hello: $(OBJS)` — 通过所有 .o 依赖文件生成可执行文件，`$^` 表示所有依赖文件，`$@` 表示目标文件（hello）
- `%.o: %.c` — 将任意的 .c 源文件编译成对应的 .o 目标文件，无需为每个 .c 文件单独编写编译规则，简化 Makefile 编写；`$<` 表示依赖文件（.c），`$@` 表示目标文件（.o）

#### CMake 简介

CMake 是一个 Makefile 生成器，通过 CMake 生成 Makefile 后，最终还是通过 make 编译。相对而言，CMake 工程更容易读懂和维护。



---

## 第四章 文件 I/O

> 💡 **Linux 一切皆文件**：系统将几乎所有硬件设备、进程、网络连接等资源都抽象为文件，通过统一的文件操作接口（如 `open()`、`read()`、`write()`、`close()`）来访问和管理，使得 Linux 编程更加统一和简洁。

### 系统 I/O（open / close / read / write / lseek）

系统 I/O 基于操作系统提供的系统调用实现，直接与内核交互，操作的是**文件描述符（fd）**，更加底层，灵活性高但使用相对复杂。

#### open() — 打开文件



```c
#include <fcntl.h>
int open(const char *pathname, int flags, mode_t mode);

/* 参数说明：
 * pathname — 文件路径名
 * flags    — 必选其一：O_RDONLY(只读)、O_WRONLY(只写)、O_RDWR(读写)
 *            可选组合：O_CREAT(不存在则创建)、O_TRUNC(清空)、O_APPEND(追加)
 *            高级选项：O_NONBLOCK(非阻塞)、O_SYNC(同步写入)
 * mode     — 权限（仅 O_CREAT 时有效），如 0644 对应 -rw-r--r--
 * 返回值   — 成功返回文件描述符(fd)，失败返回 -1
 */
```

#### close() — 关闭文件

```c
#include <unistd.h>
int close(int fd);
// 参数：fd — 文件描述符
// 返回值：成功返回 0，失败返回 -1
```

#### open/close 基本示例

```c
#include <stdio.h>   // 标准输入输出函数
#include <fcntl.h>   // open() 函数声明
#include <unistd.h>  // close() 函数声明

int main()
{
    int fd;
    fd = open("example.txt", O_RDWR | O_CREAT, 0644);
    if (fd == -1) {
        printf("打开文件失败");
        return 1;
    }
    // 使用文件描述符进行读写操作...
    close(fd);
    return 0;
}
```

#### write() — 写入文件

```c
#include <unistd.h>
ssize_t write(int fd, const void *buf, size_t count);

/* 参数说明：
 * fd    — 文件描述符（由 open() 返回）
 * buf   — 指向内存缓冲区的指针，存放要写入的数据
 * count — 请求写入的字节数
 * 返回值 — 成功返回实际写入的字节数，失败返回 -1
 *
 * 类型说明：
 *   size_t  — unsigned long / unsigned long long（无符号）
 *   ssize_t — signed long / signed long long（有符号，对应 size_t）
 */
```

#### read() — 读取文件

```c
#include <unistd.h>
ssize_t read(int fd, void *buf, size_t count);

/* 参数说明：
 * fd    — 文件描述符
 * buf   — 指向内存缓冲区的指针，用于存储读取的数据
 * count — 请求读取的最大字节数
 * 返回值 — 成功返回实际读取的字节数(可能小于 count)
 *          0 表示已到达文件末尾(EOF)
 *          -1 表示出错
 */
```

#### lseek() — 设置文件读写位置

```c
#include <unistd.h>
off_t lseek(int fd, off_t offset, int whence);

/* 参数说明：
 * fd     — 文件描述符
 * offset — 偏移量（正数向后移动，负数向前移动，0 不移动）
 * whence — 基准位置：
 *          SEEK_SET — 从文件开头计算
 *          SEEK_CUR — 从当前位置计算
 *          SEEK_END — 从文件末尾计算（offset 可为负数）
 * 返回值 — 成功返回新的文件偏移量（从文件头算起的字节数），失败返回 -1
 */
```



#### 综合示例：文件的写、读、定位操作

```c
#include <fcntl.h>   // open 函数
#include <unistd.h>  // read、write、close 函数
#include <stdio.h>   // 标准输入输出函数
#include <string.h>  // strlen 函数

int main()
{
    int fd;
    char write_buf[] = "Hello, World!";
    char read_buf[100];
    ssize_t bytes_written, bytes_read;

    // 打开文件，如果不存在则创建，设置读写权限
    fd = open("test.txt", O_RDWR | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        printf("打开文件失败");
        return 1;
    }

    // write：将 write_buf 缓冲区中的内容写入 fd 文件
    bytes_written = write(fd, write_buf, strlen(write_buf));
    if (bytes_written == -1) {
        printf("写入失败");
        close(fd);
        return 1;
    }
    printf("成功写入 %zd 字节\n", bytes_written);

    // 将文件指针重置到开头
    if (lseek(fd, 0, SEEK_SET) == -1) {
        printf("重置文件指针失败");
        close(fd);
        return 1;
    }

    // read：将 fd 文件内容读取到 read_buf 缓冲区中
    // sizeof(read_buf)-1 是为了留出最后一字节的空间存放 '\0'
    bytes_read = read(fd, read_buf, sizeof(read_buf) - 1);
    if (bytes_read == -1) {
        printf("读取失败");
        close(fd);
        return 1;
    }
    read_buf[bytes_read] = '\0';  // 必须加 '\0' 保证内容正确结束
    printf("成功读取 %zd 字节：%s\n", bytes_read, read_buf);

    close(fd);
    return 0;
}
```

#### 实战：用 read 和 write 实现 cp 命令

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <pthread.h>

int main(int argc, char *argv[])
{
    char buf[1024];
    int n = 0;
    int fd1 = open(argv[1], O_RDONLY);
    int fd2 = open(argv[2], O_RDWR | O_CREAT | O_TRUNC, 0664);

    // 1024 是缓冲区的最大长度
    // 内容 < 1024 字符 → 一次性传输
    // 内容 > 1024 字符 → 分批传输，n 为每次传输的字符数量
    while ((n = read(fd1, buf, 1024)) != 0) {
        write(fd2, buf, n);
    }

    close(fd1);
    close(fd2);
    return 0;
}
```

### 系统 I/O vs 标准 I/O 对比

<img src="./日常记录.assets/image-20260314201625600.png" alt="image-20260314201625600" style="zoom:50%;" />

> 此图清晰展示了系统 I/O 和标准 I/O 的层次关系。

- **系统 I/O**：基于系统调用，直接与内核交互，操作文件描述符（fd），较底层，无用户空间缓冲
- **标准 I/O**：C 标准库提供的 I/O 函数，基于系统 I/O 封装，**自带用户缓冲区**，遵循"预读入缓输出"机制

### 缓冲区机制

#### 用户缓冲区（User Buffer）

在进行数据读写时，数据先不直接写入或读入设备，而是写入或读入**内存空间**，当满足一定条件时再将数据写入文件或设备中。

> 🎯 **作用**：**减少系统调用次数**，提高读写速度和代码效率。每一次系统调用都是很浪费系统资源的。

#### 内核缓冲区（Kernel Buffer / Page Cache）

为了提高磁盘 I/O 性能，操作系统使用缓冲区（页缓存）技术。当调用 `write` 时，数据首先被复制到内核的页缓存中，而不是直接写入磁盘。

> 🎯 **作用**：将多次小的写入操作合并成一次大的写入操作，**减少磁盘寻道和旋转延迟**，提高整体性能。

#### 缓冲区数据何时写入设备？

1. 缓冲区已满
2. 手动强制写入（`fsync` / `fflush`）
3. 程序结束
4. 关闭文件

---

### 标准 C I/O（fopen / fclose / fwrite / fread / fseek）

#### fopen() — 打开文件

```c
#include <stdio.h>
FILE *fopen(const char *path, const char *mode);

/* 参数说明：
 * path — 文件路径名
 * mode — 打开模式（如 "r", "w", "r+", "w+", "a" 等）
 * 返回值 — 成功返回文件指针(FILE*)，失败返回 NULL
 */
```

#### fclose() — 关闭文件

```c
#include <stdio.h>
int fclose(FILE *fp);
// 参数：fp — 文件指针
// 返回值：成功返回 0，失败返回 EOF
```

#### fopen/fclose 基本示例

```c
#include <stdio.h>

int main()
{
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        printf("fopen error");
        return 1;
    }

    fclose(file);
    return 0;
}
```

#### fwrite() — 写入文件

```c
#include <stdio.h>
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);

/* 参数说明：
 * ptr    — 需要写入的数据缓存地址
 * size   — 数据块大小（每个元素的字节数）
 * nmemb  — 要写入的数据块个数
 * stream — 目标文件指针
 * 返回值 — 成功返回写入的数据块个数（注意：不是字节数！），失败返回 0
 */
```

#### fread() — 读取文件

```c
#include <stdio.h>
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);

/* 参数说明：
 * ptr    — 存放数据的缓存地址
 * size   — 数据块大小（每个元素的字节数）
 * nmemb  — 要读取的数据块个数
 * stream — 源文件指针
 * 返回值 — 成功返回读取到的数据块个数（注意：不是字节数！），失败返回 0
 */
```

#### fseek() — 设置文件位置

```c
#include <stdio.h>
int fseek(FILE *stream, long offset, int whence);

/* 参数说明：
 * stream — 文件指针
 * offset — 光标偏移量
 * whence — 基准位置：
 *          SEEK_SET — 从文件头开始
 *          SEEK_CUR — 从当前位置开始
 *          SEEK_END — 从文件末尾开始
 */
```



#### 标准 I/O 综合示例

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *fp;
    char write_buffer[] = "Hello, World!";
    char read_buffer[100];
    size_t bytes_written, bytes_read;

    // 创建并打开文件
    fp = fopen("example.txt", "w+");
    if (fp == NULL) {
        printf("无法创建文件");
        return 1;
    }

    // fwrite 写入数据
    bytes_written = fwrite(write_buffer, sizeof(char), strlen(write_buffer), fp);
    if (bytes_written != strlen(write_buffer)) {
        printf("写入失败");
        fclose(fp);
        return 1;
    }
    printf("成功写入 %zu 字节\n", bytes_written);

    // fseek 将文件指针重置到文件开头
    if (fseek(fp, 0, SEEK_SET) != 0) {
        printf("重置文件指针失败");
        fclose(fp);
        return 1;
    }

    // fread 读取数据
    bytes_read = fread(read_buffer, sizeof(char), sizeof(read_buffer) - 1, fp);
    if (bytes_read > 0) {
        read_buffer[bytes_read] = '\0';  // 添加字符串结束符
        printf("成功读取 %zu 字节：%s\n", bytes_read, read_buffer);
    } else {
        printf("读取失败");
    }

    fclose(fp);
    return 0;
}
```

#### write 与 fwrite 的区别

| 对比维度 | write（系统 I/O） | fwrite（标准 I/O） |
|----------|-------------------|---------------------|
| **层次** | 系统调用，直接与内核交互 | C 标准库函数，基于 write 封装 |
| **缓冲区** | 无用户空间缓冲 | 自带用户空间缓冲区 |
| **数据流向** | 用户空间 → 内核缓冲区 | 用户空间 → 用户缓冲区 → 内核缓冲区 |
| **强制写入** | `fsync` | `fflush` |
| **性能** | 频繁调用时系统调用次数多，性能受影响 | 缓冲机制减少系统调用，效率更高 |

---

## 第五章 进程管理

### 进程概念

| 概念 | 比喻 | 说明 |
|------|------|------|
| **程序 (Program)** | 剧本 | 死的，只占用磁盘空间，静态的可执行文件（机器指令 + 数据） |
| **进程 (Process)** | 戏 | 活的，运行起来的程序，占用内存、CPU 等系统资源 |
| **PID** | 身份证 | 每个进程唯一的标识符，由操作系统分配，方便管理 |

#### 为什么需要进程？

- **安全性**：每个进程运行在独立的地址空间中，一个进程的错误不会影响其他进程，增强系统稳定性
- **提高效率**：多进程实现并发执行，提高处理能力和响应速度
- **简化编程**：进程模型直观管理程序，方便复杂任务的分解和并行处理

#### 并发 vs 并行

| 概念 | 说明 | 硬件要求 |
|------|------|----------|
| **并发 (Concurrency)** | 逻辑上同时发生，任何瞬间只做一件事，宏观上同时推进多项任务 | 单核 CPU |
| **并行 (Parallelism)** | 物理上同时发生，同一瞬间多件事确实同时进行 | 多核 CPU |

> 📌 **结论**：单核 CPU 只能实现并发，多核 CPU 才能实现真正的并行。

### Linux 父子进程

Ubuntu 内核在启动时创建第一个 PID 为 1 的进程（init），后续所有进程都由此进程创建和管理（僵尸进程除外）。Linux 把所有进程放在一个**树状结构**中管理，可通过 `pstree` 命令查看。

| 概念 | 说明 |
|------|------|
| **父进程** | 创建子进程，可向子进程发送信号，等待子进程结束 |
| **子进程** | 是父进程的副本，继承父进程的资源，可向父进程发送信号 |
| **孤儿进程** | 父进程先终止而子进程未终止，孤儿进程被 init 进程（PID=1）收养 |
| **僵尸进程** | 子进程终止但父进程未调用 `wait`/`waitpid` 获取退出状态，占用少量资源但不消耗 CPU



### fork 创建子进程

#### fork 函数

```c
#include <unistd.h>
pid_t fork(void);
// 创建一个新进程，新进程为原进程的副本
```

**子进程特性：**
- 拥有与父进程相同的代码段、数据段、堆栈段
- 有自己的独立内存空间，但初始内容与父进程相同
- 从 fork 调用后的下一条指令开始执行

**返回值：**
- 父进程中：返回**子进程的 PID**（> 0）
- 子进程中：返回 **0**
- 失败时：返回 **-1**

> 💡 **通过 fork 的返回值区分父进程和子进程。**

#### fork 基本示例

```c
#include <stdio.h>
#include <unistd.h>

int main(void)
{
    int result;
    printf("This is a fork demo!\n\n");

    result = fork();

    if (result == -1) {
        // 出错处理
        printf("Fork error\n");
        return -1;
    }
    else if (result == 0) {
        // 返回值为 0 代表子进程
        printf("The returned value is %d, In child process!! My PID is %d\n\n",
               result, getpid());
    }
    else {
        // 返回值大于 0 代表父进程，result 为子进程 PID
        printf("The returned value is %d, In father process!! My PID is %d\n\n",
               result, getpid());
    }

    while (1);  // 让进程保持运行，方便观察
    return result;
}
```

### 进程终止与等待

#### 进程终止方式

**正常终止（两种方式）：**

```c
// 方式一：main 函数中调用 return
int main() {
    return 0;
}

// 方式二：调用 exit 函数
#include <stdlib.h>
void exit(int status);
// status — 进程退出状态码（0~255），传递给父进程，标识执行结果

void func() {
    exit(1);  // 在非 main 函数中调用，进程直接退出
}
```

**异常终止：**

进程收到某些信号（如 SIGKILL、SIGSEGV）而终止。例如：`kill -9 <PID>`

#### waitpid — 等待子进程终止

```c
#include <sys/wait.h>
pid_t waitpid(pid_t pid, int *status, int options);
// pid     — 要等待的子进程 PID
// status  — 存储子进程退出状态的指针
// options — 0 表示阻塞等待，WNOHANG 表示非阻塞模式
```

#### 示例：父进程等待子进程终止

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    int pid;
    printf("This is a fork demo!\n\n");

    pid = fork();

    if (pid == -1) {
        printf("Fork error\n");
        return -1;
    }
    else if (pid == 0) {
        // 子进程
        printf("The returned value is %d, In child process!! My PID is %d\n\n",
               pid, getpid());
        return 1;
    }
    else {
        // 父进程
        int status;
        waitpid(pid, &status, 0);  // 阻塞等待子进程运行完成
        printf("child return status = %d\n", WEXITSTATUS(status));
        printf("The returned value is %d, In father process!! My PID is %d\n\n",
               pid, getpid());
    }
    return 0;
}
```

### exec 系列函数

虽然 fork 创建了子进程，但子进程和父进程执行的代码是一样的（相当于复制）。如果我们希望新进程执行**不同的任务**，应该使用 exec 系列函数。

```c
#include <unistd.h>
int execl(const char *path, const char *arg, ...);

/* 功能：在当前进程中加载并执行新的程序
 * 参数：
 *   path — 可执行文件的绝对路径
 *   arg  — 参数列表，第一个参数通常为程序名（argv[0]），最后一个参数必须是 NULL
 *   例如：execl("/bin/ls", "ls", "-l", NULL)
 * 返回值：成功时无返回值，失败时返回 -1 并设置 errno
 */
```

#### 示例：fork + execl 结合使用

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    pid_t pid = fork();

    if (pid == -1) {
        printf("fork error");
        return 1;
    }
    else if (pid == 0) {
        // 子进程：执行新程序
        printf("Child process: PID = %d\n", getpid());
        if (execl("/bin/ls", "ls", "-l", "/home/xiaozhi", NULL) < 0) {
            printf("execl error");
            return 1;
        }
    }
    else {
        // 父进程：等待子进程
        printf("Parent process: PID = %d, Child PID = %d\n", getpid(), pid);
        int status;
        waitpid(pid, &status, 0);
        printf("Child exited with status %d\n", WEXITSTATUS(status));
    }
    return 0;
}
```

### 实战：保活进程（Monitor）

> 🎯 **目标**：实现一个监控程序，对另一个进程进行启动和异常重启保活。

#### 第一步：创建被监控程序 hello

```c
#include <unistd.h>
#include <stdio.h>

int main()
{
    while (1) {
        printf("hello\n");
        usleep(5000 * 1000);  // 每 5 秒打印一次
    }
    return 0;
}
```

编译生成 `hello` 可执行文件。

#### 第二步：实现保活程序 monitor

```c
#include <stdio.h>    // 标准输入输出
#include <stdlib.h>   // 标准库函数，包含 exit()
#include <unistd.h>   // 包含 fork(), execl(), sleep(), read(), write()
#include <sys/wait.h> // 包含 wait(), waitpid()

#define PROGRAM1 "./hello"

pid_t pid;  // 全局变量：保存子进程 PID

void start_program(const char *program)
{
    pid = fork();
    if (pid == 0) {
        // 子进程：执行目标程序，不再返回
        execl(program, program, (char *)NULL);
        printf("execl error");
        exit(1);
    } else if (pid < 0) {
        printf("fork error");
        exit(1);
    }
    // 父进程默认分支：pid > 0，全局变量 pid 保存了子进程 PID
}

void monitor_programs()
{
    while (1) {
        int status;
        pid_t result;
        usleep(10 * 1000);  // 每 10ms 检查一次

        // WNOHANG 非阻塞模式：子进程未结束时立即返回，父进程可以继续干其他事
        result = waitpid(pid, &status, WNOHANG);

        if (result == 0) {
            // 子进程还在运行，什么都不做
        } else if (result == -1) {
            printf("waitpid error");
            exit(1);
        } else {
            // 子进程已退出，重新启动
            printf("restart process\n");
            usleep(2 * 1000);
            start_program(PROGRAM1);
        }
    }
}

int main()
{
    start_program(PROGRAM1);
    printf("start %s\n", PROGRAM1);

    monitor_programs();
    return 0;
}
```

> 📌 **核心逻辑**：父进程用 `WNOHANG` 非阻塞轮询子进程状态，子进程退出时自动重启，实现保活。

---



---

## 第六章 进程间通信（IPC）

### 概述：为什么需要 IPC

在项目进行模块化开发时，一个大项目有多个不同的模块，可以把这些模块作为独立的仓库开发。只要规范好 IPC 接口和协议，不同模块可以由不同开发人员开发，互不影响，而且一个模块的 BUG 也不会影响到其他模块运行。

当应用被分为多个独立运行的进程时，进程之间需要有效地交换信息，这正是通过进程间通信（Inter-Process Communication, IPC）来实现的。

#### Linux IPC 方式一览

| IPC 方式 | 特点 | 适用场景 |
|----------|------|----------|
| **匿名管道 (Pipe)** | 单向，仅限亲缘进程（父子/兄弟） | 简单父子进程数据传递 |
| **命名管道 (FIFO)** | 通过文件系统路径名访问，可用于非亲缘进程 | 任意进程间简单通信 |
| **共享内存 (Shared Memory)** | 最快，多进程共享同一物理内存 | 大数据量、高频交互（视频/图像处理） |
| **消息队列 (Message Queue)** | 结构化消息，支持优先级 | 结构化数据传输 |
| **信号 (Signal)** | 异步通知机制，类似软件中断 | 事件通知、异常处理 |
| **信号量 (Semaphore)** | 同步互斥机制 | 配合共享内存实现同步 |

---

### 匿名管道（Anonymous Pipe）

> 📌 **特点**：单向通信（半双工），仅限亲缘进程（父子/兄弟），数据在内存中，管道缓冲区通常为 64KB。

#### pipe() 函数

```c
#include <unistd.h>
int pipe(int pipefd[2]);
// pipefd[0] — 读端，pipefd[1] — 写端
// 返回值：成功返回 0，失败返回 -1 并设置 errno

/* 使用注意事项：
 * 1. 只能用于亲缘进程（父子进程、兄弟进程）
 * 2. 单工通信 — 一端读，一端写（需提前设计好方向）
 * 3. 创建管道后，关闭不用的端口（防止文件描述符泄漏）
 * 4. 管道缓冲区固定大小（通常 64KB），写满会阻塞，需保证读写速度匹配
 */
```

#### 示例一：父子进程单向通信（父→子）

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main()
{
    int pipefd[2];     // 管道文件描述符数组
    pid_t pid;
    char buf[100];     // 缓冲区用于读取数据

    // 1. 创建管道（成功时内核将读端 ID 填入 pipefd[0]，写端 ID 填入 pipefd[1]）
    if (pipe(pipefd) == -1) {
        printf("pipe error");
        exit(1);
    }

    // 2. 创建子进程
    pid = fork();
    if (pid == -1) {
        printf("fork error");
        exit(1);
    }

    if (pid == 0) {
        // === 子进程（读取端） ===
        close(pipefd[1]);  // 关闭写端
        ssize_t bytes_read = read(pipefd[0], buf, sizeof(buf));
        // read 将内核缓冲区数据复制到用户空间的 buf 中（安全隔离）
        // strlen(msg)+1 已经包含了 '\0'，所以不用手动补
        if (bytes_read == -1) {
            printf("read error");
            exit(1);
        }
        printf("Child received: %s\n", buf);
        close(pipefd[0]);  // 关闭读端
    }
    else {
        // === 父进程（写入端） ===
        close(pipefd[0]);  // 关闭读端
        const char *msg = "Hello, World!";
        // strlen(msg)+1 把末尾 '\0' 也发送过去，子进程可正确识别字符串结尾
        ssize_t bytes_written = write(pipefd[1], msg, strlen(msg) + 1);
        if (bytes_written == -1) {
            printf("write error");
            exit(1);
        }
        close(pipefd[1]);  // 关闭写端
        wait(NULL);        // 等待子进程结束
    }
    return 0;
}
```



#### 示例二：父子进程双向通信（双管道模拟全双工）

Linux 匿名管道是单向（半双工）的，要像打电话一样你来我往，必须用**两个管道**：

```
父进程 ──pipe1[写]──▶ 子进程（收）
父进程 ◀──pipe2[读]── 子进程（发）
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main()
{
    int pipefd1[2];  // 管道1：父 → 子
    int pipefd2[2];  // 管道2：子 → 父
    pid_t pid;
    char buf[100];

    // 创建两个管道
    if (pipe(pipefd1) == -1) { printf(“pipe1 error”); exit(1); }
    if (pipe(pipefd2) == -1) { printf(“pipe2 error”); exit(1); }

    pid = fork();
    if (pid == -1) { printf(“fork error”); exit(1); }

    if (pid == 0) {
        // === 子进程 ===
        close(pipefd1[1]);  // 关掉管道1写端（只收）
        close(pipefd2[0]);  // 关掉管道2读端（只发）

        // 从管道1收父进程消息
        ssize_t n = read(pipefd1[0], buf, sizeof(buf));
        printf(“Child received from parent: %.*s\n”, (int)n, buf);

        // 向管道2发消息给父进程
        const char *msg = “Hello, Parent!”;
        write(pipefd2[1], msg, strlen(msg) + 1);

        close(pipefd1[0]);
        close(pipefd2[1]);
    }
    else {
        // === 父进程 ===
        close(pipefd1[0]);  // 关掉管道1读端（只发）
        close(pipefd2[1]);  // 关掉管道2写端（只收）

        // 向管道1发消息给子进程
        const char *msg = “Hello, Child!”;
        write(pipefd1[1], msg, strlen(msg) + 1);

        // 从管道2收子进程消息
        ssize_t n = read(pipefd2[0], buf, sizeof(buf));
        printf(“Parent received from child: %.*s\n”, (int)n, buf);

        close(pipefd1[1]);
        close(pipefd2[0]);
        wait(NULL);
    }
    return 0;
}
```

**设计思路（用端口开关表理解）：**

| 进程 | 保留端口 | 关闭端口 | 角色 |
|------|---------|----------|------|
| **子进程** | pipefd1[0]（读）、pipefd2[1]（写） | pipefd1[1]、pipefd2[0] | 管道1的接收站 + 管道2的发送站 |
| **父进程** | pipefd1[1]（写）、pipefd2[0]（读） | pipefd1[0]、pipefd2[1] | 管道1的发送站 + 管道2的接收站 |



### 命名管道（FIFO）

> 📌 **特点**：类似匿名管道，但通过文件系统路径名访问，可在**没有亲缘关系**的进程之间使用，在文件系统中占个座（权限位开头为 `p`），但数据只存在于内核缓冲区，不占用磁盘空间。

![image-20260322141925063](./日常记录.assets/image-20260322141925063.png)

#### mkfifo() 函数

```c
#include <sys/types.h>
#include <sys/stat.h>
int mkfifo(const char *pathname, mode_t mode);
// pathname — FIFO 路径名
// mode     — 权限模式（如 0666）
// 返回值   — 成功返回 0，失败返回 -1 并设置 errno

/* 注意事项：
 * 1. 有名管道可使非亲缘的两个进程互相通信
 * 2. 通过路径名操作，在文件系统中可见，但内容存放在内存中
 */
```

#### 示例一：父子进程通过 FIFO 通信

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main() {
    const char *fifo_name = "/tmp/myfifo";
    //这个路径下的文件的权限位开头也会是p(代表pipe)，他在文件系统中占个座，但它不占用磁盘空间，数据依然只存在于内核缓冲区。
    mode_t mode = 0666;

    // 创建命名管道，理解mkfifo函数
    if (mkfifo(fifo_name, mode) == -1) {
        printf("mkfifo error");
        exit(1);
    }

    // 创建子进程
    pid_t pid = fork();
    if (pid == -1) {
        printf("fork error");
        exit(1);
    }

    if (pid == 0) {
        // 子进程
        int fd;
        char buf[100];
        // 打开命名管道进行读取
        fd = open(fifo_name, O_RDONLY, 0644);
        if (fd == -1) {
            printf("open error");
            exit(1);
        }
        // 从命名管道读取数据
        ssize_t bytes_read = read(fd, buf, sizeof(buf));
        if (bytes_read == -1) {
            printf("read error");
            exit(1);
        }
        printf("Child received: %s\n", buf);
        close(fd);
        exit(0);//exit(1)代表出错了，exit(0)代表一切正常，主动刷新缓冲区，收回内存
    } else {
        // 父进程
        int fd;
        const char *msg = "Hello, Child!";
        // 打开命名管道进行写入
        fd = open(fifo_name, O_WRONLY, 0644);
        if (fd == -1) {
            printf("open error");
            exit(1);
        }
        // 向命名管道写入数据
        ssize_t bytes_written = write(fd, msg, strlen(msg) + 1);
        if (bytes_written == -1) {
            printf("write error");
            exit(1);
        }
        close(fd);
        // 等待子进程结束
        wait(NULL);
    }
    // 删除命名管道
    unlink(fifo_name);
    return 0;
}
```



#### 示例二：非亲缘进程通过 FIFO 通信（独立进程）



##### fifo_write（写入进程）

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main()
{
    printf("run fifo write\n");
    const char *fifo_name = "/tmp/myfifo";
    mode_t mode =0666;
    char buf[100];
    if(access (fifo_name , F_OK)==-1)
    {
        if(mkfifo(fifo_name,mode)==-1)
        {
            printf("mkfifo error");
            return 1;
        }
    }
    //打开命名管道进行读取
    const char *msg ="Hello,Child!";
    //打开命名管道进行写入
    int fd =open(fifo_name,O_WRONLY,0644);
    if(fd == -1)
    {
        printf("open error");
        return 1;
    }
    while(1)
    {
        printf("write data\n");
        //向命名管道写入数据
        ssize_t bytes_written= write(fd,msg,strlen(msg)+1);
        if(byte_written == -1)
        {
            peintf("write error");
            return 1;
        }
        usleep(1000*1000);
    }
    close (fd);
    printf("write finish \n");
    return 0;
}


```



##### fifo_read（读取进程）

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
    printf("run fifo read\n");
    
    const char *fifo_name ="/tmp/myfifo";
    mode_t mode =0666;
    if(access(fifo_name,F_OK)==-1)
    {
        if(mkfifo(fifo_name,mode)==-1)
        {
            printf("mkfifo error");
            return 1;
        }
    }
    char buf[100];
    int fd = open(fifo_name,O_RDONLY,0644);
    if(fd == -1)
    {
        printf("open error");
        return 1;
    }
    while(1)
    {
        //从管道读取数据
        ssize_t bytes_read = read(fd,buf,sizeof(buf));
        if(bytes_read == -1)
        {
            printf("read error");
            return 1;
        }
        else if (bytes_read ==0)
        {
            printf("Writer closed the FIFO.\n");
            break;
        }
        else
            printf("Child received:%s\n",buf);
        
    }
    close(fd);
    return 0;
}




```





#### 匿名管道 vs 命名管道 对比


* 相同点：open打开管道文件以后，在内存中开辟了一块空间，管道的内容在内存中存放，有两个指针，头指针和尾指针指向它，读写数据是在给内存的操作，并且都是半双工通讯。
* 区别：有名在任意进程之间使用，无名在父子进程之间使用。



#### FIFO 与普通文件的区别

有名管道(FIFO):主要用于不同进程之间的单向或双向通信，FIFO提供了一种机制，使得一个进程可以向另一个进程发送数据，而不需要它们直接共享内存或文件，FIFO是一种先进先出的数据结构，数据按照顺序读取和写入。

普通文件：常规文件类型，用于存储数据，主要用于持久化存储数据，可以被多个进程读取和写入



### 共享内存（Shared Memory）


共享内存是Linux的一种高效的进程间通信方式，通过共享内存，多个进程可以访问同一块内存区域，从而实现数据的快速交换。

![image-20260323203007787](./日常记录.assets/image-20260323203007787.png)

映射内存就是在每个人进程的虚拟地址空间中，实现了某块虚拟内存区域与物理内存中的“共享内存”的链接，但是各进程之间隔离。



#### shm_open() — 创建或打开共享内存对象

```c
#include <sys/mman.h>
#include <fcntl.h>
int shm_open(const char *name,int oflag,mode_t mode);
```

功能：创建或打开一个命名的共享内存对象。

参数： name：共享内存对象的名字，使用路径字符串(如./my_shm)。

oflag：操作标志，如 `O_CREAT`, `O_RDWR`, `O_RDONLY` 等。

 O_RDONLY（只读）、O_WRONLY（只写）、O_RDWR（读写） O_CREAT（不存在则创建）、O_TRUNC（清空）、O_APPEND（追加）

mode：权限设置，常见的权限设置包括 0666（所有用户都有读写权限）。

返回值：成功返回文件描述符(fd)，失败返回-1。

```c
 // 创建或打开共享文件（如果不存在则创建，设置读写权限）
 int shm_fd = shm_open("/my_shared_memory", O_CREAT | O_RDWR, 0666);
```

#### ftruncate() — 设置共享内存大小

```c
#include <unistd.h>
#include <sys/mman.h>
int ftruncate(int fd,off_t length);
```

功能：设置由shm_open返回的共享内存对象的大小。

参数：

* fd:由shm_open返回的文件描述符
* length:共享内存大小(字节)
* 返回值：成功返回0，失败返回-1。



#### mmap() — 将共享内存映射到进程地址空间

完成物理内存到虚拟地址空间的映射

```c
#include <sys/mman.h>
void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);
```

- `addr`：建议的映射起始地址（通常为 `NULL` 让系统自动分配）。
- `length`：要映射的内存长度。
- `prot`：设置内存区域的保护模式（读/写/执行权限），如 `PROT_READ`可读、`PROT_WRITE`可写。
- `flags`：映射标志，默认 `MAP_SHARED`适用于进程间通信，`MAP_PRIVATE`不会被其他进程看到，适用于只读映射或临时数据处理。
- `fd`：由 `shm_open` 返回的文件描述符。
- `offset`：偏移量（通常为 `0`）。

返回值：成功返回映射后的指针，失败返回MAP_FAILED。

```c
//创建共享映射
char *map =mmap(NULL,1024,PROT_READ|PROT_WRITE,MAO_SHARED,fd,0);
```



#### munmap() — 解除共享内存映射

```c
#include <sys/mman.h>
int munmap(void *addr,size_t length);
```

功能：解除当前进程通过mmap建立的内存映射，要注意的是解除不是删除。

参数：

addr:由mmap返回的指针

length：映射区域的大小

返回值：成功返回0，失败返回-1



#### shm_unlink() — 删除共享内存对象

```c
#include <sys/mman.h>
int shm_unlink (const char *name);
```



功能：删除指定名称的共享内存对象(类似于unlink)

参数：
name：共享内存对象的名称

返回值：成功返回0，失败返回-1

注意：即使有进程仍在映射该内存，shm_unlink也会将其标记为删除，所有映射解除后才会真正删除。



注意事项：

共享内存本身不提供同步机制，如果要确保多个进程之间的同步，可以使用信号量或者其他同步机制。

由于共享内存是通过共享同一块内存区域，多个进程可以直接读写这块内存中的数据，所以速率会更快，更适合以下这些场景应用：

**高性能计算**：需要高速数据交换的场景，如实时数据处理、图形渲染等。

 **大数据传输**：需要传输大量数据的场景，如文件传输、数据库操作等。

 **多进程协作**：多个进程需要频繁共享和更新数据的场景。



**下面我们来看一个例子：如何使用共享内存在两个进程之间进行通信**

**父进程：创建共享内存并写入一条消息。**

**子进程：读取共享内存中的消息。**

 **不使用同步机制（如信号量），只展示共享内存的基本通信功能。**

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/wait.h>

#define SHM_NAME "/my_shared_memory"
#define SIZE 1024

int main()
{
    //删除已有的共享内存(防止残留)
    shm_unlink(SHM_NAME);
    //创建共享内存对象
    int shm_fd =shm_open(SHM_NAME,O_CREAT|O_RDWR,0666);
    if(shm_fd == -1)
    {
        printf("shm_open failed");
        return 1;
    }
    //设置共享内存大小
    if(ftruncate(shm_fd,SIZE)==-1)
    {
        printf("ftruncate failed");
        close(shm_fd);
        return 1;
    }
    //映射共享内存到当前进程地址空间
    char *shared_data =mmap(NULL,SIZE,PROT_READ|PROT_WRITE,MAP_SHARED,shm_fd,0)；
    //这个shared_data是一个指针，进程中可以调用他，指向通过mmap映射的那块共享内存。
    if(shared_data == MAP_FAILED)
    {
        printf("mmap failed");
        close(shm_fd);
        return 1;
    }
    pid_t pid =fork();
    
    if(pid<0)
    {
        printf("fork failed");
        return 1;
    }
    if(pid == 0)
    {
        //子进程：读取者
        sleep(1);//简单等待父进程写入完成
        printf("[Child Process] Read message:%s\n",shared_data);
        
    }
    else 
    {
        //父进程：写入者
        const char *msg ="Hello from parent!";
        strcpy(shared_data,msg);
        //strcpy会把msg里的字符一个一个搬运到shared_data指向的物理地址，直到遇到结束符\0
        printf("[Parent Process] Message written to shared memory .\n");
        //等待子进程读取完成
        wait(NULL);
        
    }
    //清理资源
    munmap(shared_data,SIZE);//取消内存映射，但这并不会删除共享内存里的数据，只是切断了当前进程与那块内存的联系。
    close(shm_fd);//同样不会删除共享内存，在Linux中，只要还有一个进程打开着这个对象，或者他还没被unlink，他就一直存在于内核中。
    shm_unlink(SHM_NAME);//从系统中删除共享内存对象的名字，如果有其他进程正在使用它，内核会等所有的进程都munmap后，才真正释放物理内存，一旦unlink成功，其他进程就再也无法通过这个名字找到这块内存了。
    
    return 0;

}

```



### 消息队列（Message Queue）


提供一种在进程间传递结构化消息的机制，传输结构化数据指的是通过消息队列发送的不是简单的字符串或字节流，而是具有明确格式和逻辑结构的自定义数据类型(例如结构体)。消息队列可以存储多个消息，并且可以设置消息的优先级。

#### mq_open() — 创建或打开消息队列

```c
#include <mqueue.h>
mqd_t mq_open(const char *name,int oflag,mode_t mode,struct mq_attr *attr);
```

功能：创建或打开一个命名的消息队列

参数：

* name:消息队列名称(以/开头，如/my_queue)。

* oflag：操作标志，如O_CREAT,O_RDONLY,O_WRONLY,O_RDWR。

* mode:权限设置，如0666，仅在创建时使用

* attr：指向mq_attr结构，指定最大消息数，每条消息最大长度等属性，如果attr为NULL，则使用系统默认值(通常mq_maxmsg=10,mq_nsgsize=8192)

返回值：成功返回消息队列描述符(mqd_t),失败返回(mqd_t)-1



结构体定义：

```c
代码块
struct mq_attr
{
    long mq_flags;  //队列标志
    long mq_maxmsg; //最大消息数
    long mq_msgsize; //每条消息最大长度
    long mq_curmsgs;//当前队列中的消息数
};

使用参考:
struct mq_attr attr;
attr.mq_flags =0;
attr.mq_maxmsg = 10;
attr.mq_msgsize = 256;
attr.mq_curmsgs = 0;
```



#### mq_send() / mq_receive() — 发送和接收消息

```c
#include <mqueue.h>
int mq_send(mqd_t mqdes,const char*msg_ptr,size_t msg_len,unsigned int msg_prio);
ssize_t mq_receive(mqd_t mqdes,char *msg_ptr,size_t msg_len,unsigned int *msg_prio)
```

功能：

* mq_send 向队列中发送一条消息

* mq_receive 从队列中接收一条消息

* mqdes：由mq_open返回的消息队列描述符

* msg_ptr:消息内容缓冲区

* msg_len:消息长度

* msg_prio:消息优先级（数值越大优先级越高）。

  返回值：成功返回0（发送）或实际读取字节数（接收），失败返回-1。

#### mq_close() — 关闭消息队列

```c
#include<mqueue.h>
int mq_close(mqd_t mqdes);
```

功能：关闭之前打开的消息队列描述符

返回值：成功返回0，失败返回-1。



#### mq_unlink() — 删除消息队列

```c
#include <mqueue.h>
int mq_unlink(const char *name);
```

功能：删除指定名称的消息队列（即使仍有进程打开也不会立即删除，直到所有引用关闭）

返回值：成功返回0，失败返回-1。



#### 示例一：父子进程通过消息队列通信

**功能描述：**
- 父进程：创建并打开消息队列，向其中发送一条消息
- 子进程：打开同一队列，读取消息并打印

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mqueue.h>
#include <unistd.h>
#include <sys/wait.h>

#include QUEUE_NAME "/my_message_queue"
#define MAX_MESSAGES 10
#define MAX_MSG_SIZE 256
#define MSG_PRIORITY 1
int main()
{
    mqd_t mq;
    struct mq_attr attr;
    
    //设置消息队列属性
    attr.mq_flags = 0;//默认为阻塞状态
    attr.mq_maxmsg = MAX_MESSAGES;//队列深度：能塞几封信
    attr.mq_msgsize =MAX_MSG_SIZE;//消息尺寸：每一条消息最大包含多少字节
    attr.mq_curmsgs =0;
    //删除已存在的队列(防止残留)
    mq_unlink(QUEUE_NAME);
    //创建消息队列
    mq=mq_open(QUEUE_NAME,O_CREAT|O_RDWR,0666,&attr);
    //正式让内核分配内存，建立队列
    if(mq == (mqd_t)-1)
    {
        printf("mq_open failed");
        return 1;
    }
    pid_t pid =fork();
    if(pid<0)
    {
        printf("mq_open failed");
        return 1;      
    }
    if(pid == 0)
    {
        //子进程：接收者
        char buffer[MAX_MSG_SIZE];
        unsigned int priority;
        //这个变量用来记录即将收到的消息是什么优先级
        ssize_t bytes_read;
        printf("[Child] Waiting for message...\n");
        bytes_read = mq_receive(mq,buffer,MAX_MSG_SIZE，&priority)
        //记录实际到底收到了几个字节
        if(bytes_read>=0)
        {
            buffer[bytes_read]='\0';//添加字符串结束符
            printf("[Child] Received: %s\n",buffer);
        }
    }
    else
    {
        //父进程：发送者
        const char *message = "Hello from parent process!";
        printf("[Parent] Sending message : %s\n",message);
        if(mq_send(mq,message,strlen(message),MSG_PRIORITY)==-1)
        {
            printf("mq_send failed");
        }
        //等待子进程处理完成
        wait(NULL);
    }
    mq_close(mq);//关闭队列
    mq_unlink(QUEUE_NAME)//删除队列
    return 0;
}
```



#### 示例二：独立进程间传递结构体数据



```c
//mq_read
#include <fcntl.h>//提供了文件控制的宏文件
#include <sys/stat.h>//提供设置文件权限的宏
#include <mqueue.h>//核心头文件，包含所有消息队列函数的声明
#include <stdio.h>//输入输出
#include <unistd.h>//提供了对POSIX操作系统API的访问，fork()或sleep(   )
//必须与发送方相同的结构体定义
typedef struct
{
    int sensor_id;
    float temperature;
    char timestamp[20];
}SensorData;//结构体定义通信的数据协议

int main()
{
    //1.打开消息队列(只读模式)
    mqd_t mq =mq_open("/sensor_queue",O_CREAT|O_RDONLY,0666,NULL);
    if(mq==(mqd_t)-1)
    {
        printf("mq_open error");
        return 1;
    }
    //2.获取队列属性(用于确定消息大小)
    struct mq_attr attr;//声明一个系统内置的属性结构体
    mq_getattr (mq,&attr);//把attr的地址传给内核，内核会把这个队列当前的极限参数(能存几条，每条最大多大)填到这个结构体里
    printf("Queue max message size: %ld\n",attr.mq_msgsize);
    //3.接收消息
    SensorData received_data;
    ssize_t bytes_read =mq_receive(mq,(char*)&received_data,attr.mq_msgsize,NULL);
    if(bytes_read == -1)
    {
        printf("mq_receive error");
        mq_close(mq);
        return 1;
    }
    printf("Received:sensor_id=%d,temp=%.1f,time=%s\n",received_data.sensor_id,received_data.temperature,received_data.timestamp);
    //4.关闭并删除队列(避免资源泄漏)
    mq_close(mq);
    mq_unlink("/sensor_queue");
    return 0;
    
}


```



```c
#include <fcntl.h>
#include <sys/stat.h>
#include <mqueue.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
//定义消息结构体(注意：不能直接传输指针或动态分配的内存)
typedef struct
{
    int sensor_id;
    float temperature;
    char timestamp[20];
}SensorData;

int main()
{
    //1.打开或创建消息队列
    mqd_t mq = mq_open("/sensor_queue",O_CREAT|O_WRONLY,0666,NULL);
    if(mq==(mqd_t)-1)
    {
        printf("mq_open error");
        return 1;
    }
    //2.准备结构化数据
    SensorData data ={
        .sensor_id =1001,
        .temperature =25.5,
        .timestamp ="12:00:00"
    };
    //3.发送消息
    if(mq_send(mq,(const char*)&data,sizeof(SensorData),0)==-1)
    {
        printf("mq_send error");
        mq_close(mq);
        return 1;
    }
    printf("Sent:sensor_id=%d,temp=%.1f\n",data.sensor_id,data.temperature);
    //4.关闭队列(不删除，接收方可能还需读取)
    mq_close(mq);
    return 0;
}


```





### 信号（Signal）

在 Linux 中，信号是一种常用的进程间通信（IPC）机制，用于进程之间的异步通信。通过发送信号，一个进程就可以通知另一个进程发生某些事件。信号和学习单片机的中断异常概念是非常类似的，信号是一种软件中断。



#### 信号的基本用法

```c
1、设置信号处理函数
#include <signal.h>
__sighandler_t signal(int __sig, __sighandler_t __handler)
参数：
__sig：信号编号。
__handler：信号处理函数。
返回值：
成功时返回之前的信号处理函数指针。
失败时返回 SIG_ERR。

__sighandler_t 是一个函数指针类型，我们可以基于它来传递函数。
使用示例：
void signal_handler(int sig) {
    printf("Caught signal %d\n", sig);
}
signal(SIGINT, signal_handler);  // 捕获 Ctrl+C


2、发送信号给进程。
#include <signal.h>
#include <sys/types.h>
int kill(pid_t pid, int sig);
参数：
pid：目标进程的 PID。
sig：要发送的信号编号。

3、使进程暂停，直到接收到信号。
#include <unistd.h>
int pause(void);
```



例子：例如我们可以通过注册SIGINT信号来监听按下键盘Ctrl+C的信号，更改它的实现方式

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
/**信号处理函数*/
void signal_handler(int sig)
{
    printf("this signal number is %d \n",sig)
    if(sig == SIGINT)
    {
        printf("I have get SIGINT!\n\n");
        exit(1);
    }
}
int main(void)
{
    signal(SIGINT,signal_handler);
    while(1)
    {
        printf("waiting for the SIGINT signal , please enter \"ctrl + c\"...\n");
        sleep(1);   
    }
    return 0;
}
```



除了系统预定义的信号，你还可以使用自定义信号来进行进程间的通信。自定义信号通常使用 `SIGUSR1` 和 `SIGUSR2`，这两个信号是专门为用户自定义用途保留的。

```c
#include<stdio.h>
#include<signal.h>
#include<unistd.h>
#include<sys/wait.h>
//信号处理函数
void signal_handler(int sig)
{
    if(sig==SIGINT)//这是为了确认内核传来的确实是SIGUSR1信号
    {
        printf("I have get SIGINT!\n\n");
        exit(1);
    }
}
int main()
{
    pid_t pid;
    pid=fork();
    if(pid==0)
    {
        //子进程
        signal(SIGUSR1,signal_handler);//子进程向内核注册预案：收到信号SIGUSR1，就去执行上面的signal_handler函数
        pause();//核心阻塞点，子进程执行到这里，主动放弃CPU执行权，进入内核的休眠队列等待信号
    }
    if(pid>0)
    {
        sleep(1);//当创建父进程和子进程后，这里的父进程休息1s为了把CPU让给子进程，确保子进程能安稳地把signal()和pause()执行完。
        kill(pid,SIGUSR1);//这个是给子进程发送SIGUSR1信号
        wait(NULL);//清理子进程
    }
    return 0; 
}
```





### 信号量（Semaphore）

共享内存本身不提供同步机制，没有同步机制会导致问题：一个是数据不一致，也就是例如A和B两个进程共享一个计数器变量counter，A进程读取计数器变量并对其增加1，B在A操作之后读取还是A增加1之前的数据，并没有实现同步数据。另一个是A在往共享内存中写入结构体数据，但如果没有同步机制，B在读取这个共享内存的结构体容易出现问题。

因此需要在资源中添加同步机制，例如在共享内存中使用信号量来实现同步。

#### sem_open() — 创建或打开信号量

```c
#include <semaphore.h>
#include <fcntl.h>
sem_t *sem_open(const char *name,int oflag,mode_t mode,unsigned int value);
```

功能：创建或打开一个命名信号量

参数：

name:信号量名称（以/开头，如/my_sem）

oflag:操作标志，如O_CREAT，O_RDWR

mode:权限设置(如0666)

value:初始值

返回值：成功返回指向sem_t的指针，失败返回SEM_FAILED。

例如：

```		c++
sem_open(SEM_NAME,O_CREAT|O_RDWR,0666,0);
```

#### sem_close() — 关闭有名信号量

```c
#include<semaphore.h>
int sem_close(sem_t *sem);
```

功能：关闭之前由sem_open打开的信号量

返回值：成功返回0，失败返回-1

#### sem_unlink() — 删除有名信号量

```c
#include<semaphore.h>
int sem_unlink(const char *name);
```



功能：删除指定名称的有名信号量(即使仍有进程打开也不会立即删除)

返回值：成功返回0，失败返回-1。



#### sem_wait() / sem_trywait() — 等待信号量

sem_wait

```c
int sem_wait(sem_t *sem);
```

阻塞直到信号量大于0，并将其减1

sem_trywait

```c
int sem_trywait(sem_t *sem);
```

非阻塞，如果信号量为0，则立即返回-1，否则减1.

#### sem_post() — 增加信号量值

```c
#include<semaphore.h>
int sem_post(sem_t *sem);
```

功能：将信号量值加1，唤醒正在等待的线程/进程

返回值：成功返回0，失败返回-1



#### 示例：共享内存 + 信号量实现同步

```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fcntl.h>
#include<sys/mman.h>
#include<unistd.h>
#include<semaphore.h>
#include<sys/wait.h>

#define SHM_NAME "/my_shared_memory"
#define SEM_NAME "/my_semaphore"
#define SIZE 1024
int main()
{
    //删除已有的共享内存和信号量(防止残留)
    shm_unlink(SHM_NAME);
    sem_unlink(SEM_NAME);
    //创建共享内存
    int shm_fd =shm_open(SHM_NAME,O_CREAT|O_RDWR,0666);
    if(shm_fd==-1)
    {
        printf("shm_open failed");
        return 1;
    }
    if(ftruncate(shm_fd,SIZE)==-1)
    {
        printf("ftruncate failed");
        close(shm_fd);
        return 1;
    }//设置共享内存大小
    char *shared_data =mmap(NULL,SIZE,PROT_READ|PROT_WRITE,MAP_SHARED,shm_fd,0);
    //对共享内存进行映射
    if(shared_data==MAP_FAILED)
    {
        printf("mmap failed");
        close(shm_fd);
        return 1;
    }
    //创建信号量
    sem_t *sem=sem_open(SEM_NAME,O_CREAT|O_RDWR,0666,0);
    if(sem==SEM_FAILED)
    {
        printf("sem_open failed");
        munmap(shared_data,SIZE);
        close(shm_fd);
        return 1;
    }
    pid_t pid =fork();
    if(pid == 0)
    {
        //子进程：读取者
        printf("[Child]Waiting for signal ...\n");
        sem_wait(sem);//等待信号量变为>0
        printf("[Child] Received message :%s\n",shared_data);
    }
    else
    {
     //父进程：写入者
        const char *msg ="Hello from parent process!";
        strcpy(shared_data,msg);
        printf("[Parent] Message written.\n");
        sem_post(sem);//发送信号,将信号量从0变成1
        wait(NULL);//等待子进程结束，等待回收子进程，消失僵尸进程
    }
    //清理资源
    sem_close(sem);//进程级清理：将这个信号量在当前进程空间里占用的内存释放掉
    sem_unlink(SEM_NAME);//系统级清理：将此信号量名字从系统目录中彻底抹除
    munmap(shared_data, SIZE);//将当前的虚拟地址(shared_data)和1024字节物理内存之间的连线剪掉，使得当前进程失去访问那块物理内存的权限。
    close(shm_fd);//共享内存本身也是一种文件，释放共享内存这个文件描述符
    shm_unlink(SHM_NAME);//把 /my_shared_memory 这个名字从系统中删掉。
    return 0; 
        
}
```






> 📝 *多进程双向通信控制框架（待补充）*



### IPC 总结与选型指南


* 匿名管道：当存在父子进程或兄弟进程，且需要进行简单的单向数据传输时，匿名管道是一个不错的选择。
* 命名管道：当需要在不同的、没有亲缘关系的进程之间进行简单的数据传递时，命名管道非常合适。
* 共享内存：当多个进程需要频繁地交互大量数据时，共享内存是效率最高的选择。如视频处理、图像处理等，共享内存可以减少数据传输的延迟，确保数据能够及时被处理。
* 消息队列：当进程之间需要传递结构化的数据，并且对数据的顺序和类型有要求时，消息队列是一个很好的选择。
* 信号：信号主要用于进程之间的异步通知，适用于处理系统中的紧急事件或者异常情况。例如，当用户按下Ctrl+C组合键时，系统会向当前进程发送SIGINT信号，进程可以捕获这个信号并进行相应的处理，如清理资源、退出程序等。

---

## 第七章 多线程编程


### 为什么需要线程


资源开销：

进程拥有独立的地址空间，这意味着每一个进程都有自己的一套数据段、堆栈段和代码段，这导致创建和销毁进程的开销较大。

线程共享同一进程的地址空间，包括内存资源和文件描述符等，因此创建和销毁线程的开销较小。

通信效率：

进程间通信(IPC)需要通过特定的机制如管道、消息队列、共享内存等来实现，这增加了通信的复杂性和开销。

同一进程内的线程可以直接访问共享的内存区域，使得线程间的通信更加高效和简单。

调度灵活性：

操作系统调度的基本单位是进程，这意味着如果一个进程中的任务需要等待I/O操作完成，整个进程都会被阻塞。

线程作为更细粒度的调度单位，可以在一个线程等待I/O操作时，让其他线程继续执行，提高了系统的响应速度和资源利用率。



### 核心线程函数

在 Linux 中，使用 C 语言进行多线程编程，pthread 库提供了几个核心函数来管理线程的创建、退出、等待和取消。

```c
#include <pthread.h>

// ========== pthread_create ==========

int pthread_create(pthread_t *thread,const pthread_attr_t *attr,void *(*start_routine)(void*),void *arg);
功能：创建一个新的线程
参数：
thread:用于存储新创建线程的标识符
attr:用于指定线程属性(如栈大小、优先级等)。通常设置为NULL表示使用默认属性
start_routine:线程的入口函数,类型为void*(*start_routine)(void*)
arg:传递给start_routine函数的参数,类型为void*。
返回值：成功时返回0，失败时返回错误码
    
pthread_join
int pthread_join(pthread_t thread,void **retval);
功能：等待指定的线程结束，并获取其返回值
参数：
thread:要等待的线程的标识符
retval:指向void*类型的指针，用于存储线程的返回值。如果不需要获取返回值，可以设置为NULL。
返回值：成功时返回0，失败时返回错误码。
    
pthread_exit
void pthread_exit(void *retval);
功能：使当前线程终止，并返回一个值。
参数：
retval：线程的返回值，类型为void*。这个值可以通过pthread_join函数获取。
返回值：无返回值，因为函数不会返回
    
pthread_cancel
int pthread_cancel(pthread_t thread)
功能：请求取消指定的线程。可以用于一个线程取消另一个线程
参数：
    thread:要取消的线程的标识符
    返回值：成功返回0，失败时返回错误码
```



线程在完成任务后调用pthread_exit正常终止，并返回一个值。

```c
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
void *thread_function(void *arg)//子线程一出来就直接执行thread_function的第一行
{
    int *data = (int *)arg;//子线程拿到万能指针，把它变回整数指针
    printf("Thread:Data received is %d\n",*data);
    pthread_exit ((void *)123);//子进程宣告任务结束，把结果包装成指针丢给系统，然后自行消亡
}
int main()
{
    pthread_t thread;//声明一个线程句柄
    int data =42;
    if(pthread_create(&thread,NULL,thread_function,(void*)&data)!=0)
    {//创建子线程，主线程把data的内存地址&data伪装成万能指针void*丢给操作系统，让新线程执行thread_function,并把这个地址带过去。
        printf("pthread_create fail");
        return 1;
    }
    void *retval;
    if(pthread_join(thread,&retval)!=0)//这是一个阻塞挂起动作，当子线程执行了pthread_exit后，唤醒pthread_join，同时接住了子进程丢出来的123，并把它塞进主线程的retval中
    {
        printf("pthread_join fail");
        return 1;
    }
    printf("Main:Thread returned with value %ld\n",(long)retval);
    //这个(long)retval是强行把指针形式变成长整型数字处理
    return 0;
        
}
```



需要注意：

系统规定 `pthread_exit` 必须交出一个**指针**（内存坐标）。

但如果你像现在这样，只是想简单地告诉主线程“我执行成功了（状态码 123）”，难道还要专门去主线程的栈上或者用 `malloc` 开辟一块内存，把 123 塞进去，然后再把地址传出来吗？太麻烦了！

**黑客做法：** 我直接把数字 `123` 强行贴上一个指针的标签 `(void *)`。系统内核并不聪明，它一看标签是指针，就把它当成一个“极其靠前的内存地址（地址为 0x0000007B）”收了上去。

主线程准备了一个空指针变量 `retval`。

`pthread_join` 执行完后，系统内核把刚才收到的那个“假地址”交给了主线程，塞进了 `retval` 里。

此时，`retval` 的值就是 `0x0000007B`（十进制的 123）。但系统依然坚定地认为，它是一个指向某块内存的指针。

主线程心里清楚，这个 `retval` 根本不是什么真实的内存坐标，里面装的就是个纯数字状态码，那主线程怎么把它打印出来？

- **为什么要强转？** 如果你直接用 `%d` 打印 `retval`，C 编译器会立刻报错或报警：“你正在试图把一个指针当成普通数字打印！” 所以你必须用 `(long)retval` 强行扒掉它的指针外衣，告诉编译器：“闭嘴，我知道我在干什么，把它当成一个长整型数字处理！”

**为什么是 `(long)` 而不是 `(int)`？** 这是 Linux 底层开发里最容易踩的坑！在现代的 64 位 Linux 系统中：

- 指针（内存地址）是 **64 位（8个字节）**。
- 普通的 `int` 只有 **32 位（4个字节）**。
- 如果你写成 `(int)retval`，编译器会爆出极其严厉的警告：`cast from pointer to integer of different size`。因为你试图把一个 8 字节的庞大指针，硬塞进 4 字节的小盒子里，存在精度丢失的风险（哪怕里面只装了 123）。
- 而在 Linux 64 位下，`long` 刚好也是 **64 位（8个字节）**。所以用 `(long)` 强转，体积严丝合缝，绝对安全。



主线程在运行了一段时间之后调用pthread_cancel请求取消子进程

```c
#include <stdio.h>
#include <stdlib.h>
#include<pthread.h>
#include<unistd.h>
void *thread_function(void *arg)
{
    while(1)
    {
        printf("Thread:Running ...\n");
        sleep(1);
    }
    pthread_exit(NULL);
}
int main()
{
    pthread_t thread;
    if(pthread_create(&thread,NULL,thread_function,NULL)!=0)
    {
        printf("pthread_create fail");
        return 1;
    }
    sleep(3);
    if(pthread_cancel(thread)!=0)//给子进程发送了一个信号
    {
        printf("pthread_cancel fail")
            return 1;
    }
    if(pthread_join(thread,NULL)!=0)
    {
        printf("pthread_join fail");
        return 1;
    }
    return 0;
}
```



### 线程互斥锁（Mutex）

在 Linux 中，使用 C 语言多线程编程时，互斥锁是一种常用的同步机制，用于保护共享资源，防止多个线程同时访问同一资源而导致的数据不一致问题，互斥锁的主要功能是确保同一时间只有一个线程可以访问临界区。

进程间共享数据同步用信号量，线程间共享数据同步用互斥锁。



#### 核心函数

##### pthread_mutex_init() — 初始化互斥锁

```c
int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *attr);
// 功能：初始化一个互斥锁
// mutex — 指向互斥锁的指针
// attr  — 互斥锁属性，通常传 NULL 使用默认属性
// 返回值：成功返回 0，失败返回错误码
```

##### pthread_mutex_lock() — 获取互斥锁（阻塞）

```c
int pthread_mutex_lock(pthread_mutex_t *mutex);
// 功能：获取互斥锁，如果锁已被其他线程占用则阻塞等待
// 返回值：成功返回 0，失败返回错误码
```

##### pthread_mutex_trylock() — 尝试获取互斥锁（非阻塞）

```c
int pthread_mutex_trylock(pthread_mutex_t *mutex);
// 功能：尝试获取互斥锁，如果锁已被占用则立即返回（不阻塞）
// 返回值：成功返回 0；锁被占用返回 EBUSY
```

##### pthread_mutex_unlock() — 释放互斥锁

```c
int pthread_mutex_unlock(pthread_mutex_t *mutex);
// 功能：释放互斥锁
// 返回值：成功返回 0，失败返回错误码
```

##### pthread_mutex_destroy() — 销毁互斥锁

```c
int pthread_mutex_destroy(pthread_mutex_t *mutex);
// 功能：销毁互斥锁
// 返回值：成功返回 0，失败返回错误码
```



#### 互斥锁使用示例

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

// 共享资源
int shared_data = 0;

// 互斥锁
pthread_mutex_t mutex;

// 线程入口函数
void *thread1_function(void *arg) {
    for (int i = 0; i < 1000; i++) {
        // 获取互斥锁
        pthread_mutex_lock(&mutex);
        // 临界区
        shared_data++;
        printf("Thread 1: shared_data = %d\n", shared_data);
        // 释放互斥锁
        pthread_mutex_unlock(&mutex);
        // 模拟一些工作
        usleep(1);
    }
    pthread_exit(NULL);
}

void *thread2_function(void *arg) {
    for (int i = 0; i < 1000; i++) {
        // 获取互斥锁
        pthread_mutex_lock(&mutex);
        shared_data++;
        printf("Thread 2: shared_data = %d\n", shared_data);
        pthread_mutex_unlock(&mutex); // 释放互斥锁
        usleep(1);
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t thread1, thread2;
    // 初始化互斥锁
    if (pthread_mutex_init(&mutex, NULL) != 0) {
        printf("pthread_mutex_init fail\n");
        return 1;
    }

    // 创建线程
    if (pthread_create(&thread1, NULL, thread1_function, NULL) != 0) {
        printf("pthread_create fail\n");
        return 1;
    }
    if (pthread_create(&thread2, NULL, thread2_function, NULL) != 0) {
        printf("pthread_create fail\n");
        return 1;
    }

    // 等待线程结束
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    // 销毁互斥锁
    if (pthread_mutex_destroy(&mutex) != 0) {
        printf("pthread_mutex_destroy fail\n");
        return 1;
    }

    return 0;
}
```

使用互斥锁并不能保证线程1先执行或者线程2先执行，不能保证顺序只能保证同一时间只有一个可以执行，主线程会一直执行，创建线程1然后继续执行创建线程2，就跟裁判一样创建两个运动员然后公平竞争，并不知道会先执行线程1还是线程2。



### 条件变量（Condition Variable）


```c
#### 核心函数

##### pthread_cond_init() — 初始化条件变量
int pthread_cond_init(pthread_cond_t *cond,const pthread_condattr_t *attr)；
功能：初始化一个条件变量
参数：
    cond:指向pthread_cond_t类型的指针，用于存储条件变量
    attr:指向pthread_condattr_t类型的指针，用于指定条件变量属性。通常设置为NULL表示使用默认属性。
返回值：成功时返回0，失败时返回错误码。
##### pthread_cond_signal() — 唤醒一个等待的线程
int pthread_cond_signal(pthread_cond_t *cond);
功能：唤醒一个等待该条件变量的线程
参数：
cond:指向pthread_cond_t类型的指针，表示要唤醒的条件变量
返回值：成功时返回0，失败时返回错误码
##### pthread_cond_wait() — 等待条件变量
int pthread_cond_wait(pthread_cond_t *cond,pthread_mutex_t *mutex)
功能：等待条件变量，调用此函数的线程会释放互斥锁并进入等待状态，直到被其他线程唤醒。
参数：
    cond:指向pthread_cond_t类型的指针，表示要等待的条件变量
    mutex:指向pthread_mutex_t类型的指针，表示与条件变量关联的互斥锁
返回值：成功时返回0，失败时返回错误码
##### pthread_cond_destroy() — 销毁条件变量
int pthread_cond_destroy(pthread_cond_t *cond);
功能：销毁一个条件变量
参数：
    cond:指向pthread_cond_t类型的指针，用于销毁条件变量。
    返回值：成功时返回0，失败时返回错误码。
```



```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

int shared_data =0;
pthread_mutex_t mutex;
pthread_cond_t cond;

void *producer(void *arg)
{
    for(int i = 0;i<5;i++)
    {
        pthread_mutex_lock(&mutex);
        shared_data ++;
        printf("shared_data = %d\n",shared_data);
        pthread_cond_signal(&cond);
        pthread_mutex_unlock(&mutex);
        sleep(3);
    }
    pthread_exit(NULL);
}
void *consumer(void *arg)
{
    for (int i =0;i<5;i++)
    {
        pthread_mutex_lock(&mutex);
        while(shared_data==0)
        {
            pthread_cond_wait(&cond,&mutex);
         //这一行代码执行时的逻辑：一旦执行后首先是自动解锁把锁给生产者；然后是挂机状态不消耗CPU资源，最后如果生产者调用pthread_cond_signal(&cond)系统内核会让消费者重新抢夺锁然后执行下边代码。
        }
        shared_data--;
        printf("shared_data=%d\n",shared_data);
        pthread_mutex_unlock(&mutex);
        sleep(1);
    }
    pthread_exit(NULL);
}

int main()
{
    pthread_t producer_thread,consumer_thread;
    if(pthread_mutex_init(&mutex,NULL)!=0)
    {
        printf("pthread_mutex_init fail");
        return 1;
    }
    if(pthread_cond_init(&cond,NULL)!=0)
    {
        printf("fail");
        return 1;
    }
    if(pthread_create(&producer_thread,NULL,producer,NULL)!=0)
    {
        printf("pthread_create fail");
        return 1;
    }
    if(pthread_create(&consumer_thread,NULL,consumer,NULL)!=0)
    {
        printf("pthread_create fail");
        return 1;
    }
    
}
```

---

## 第八章 xv6

> 📝 *本章内容待补充*























































# Linux 驱动开发学习笔记

> 📅 学习时间：2026年5月 ~ 6月
> 📦 开发板：正点原子阿尔法 Linux 开发板 (i.MX6ULL)
> 🎯 课程：正点原子 Linux 驱动开发篇

---

## 目录

- [第一章 字符设备驱动基础](#第一章-字符设备驱动基础)
- [第二章 LED 字符设备驱动（真实 GPIO）](#第二章-LED-字符设备驱动真实-GPIO)
- [第三章 新字符设备 LED 驱动](#第三章-新字符设备-LED-驱动)
- [第四章 设备树与 OF 函数](#第四章-设备树与-OF-函数)
- [第五章 设备树 LED 驱动](#第五章-设备树-LED-驱动)
- [第六章 Pinctrl 与 GPIO 子系统](#第六章-Pinctrl-与-GPIO-子系统)
- [第七章 蜂鸣器驱动](#第七章-蜂鸣器驱动)
- [第八章 原子操作（并发保护）](#第八章-原子操作并发保护)
- [第九章 自旋锁（Spinlock）](#第九章-自旋锁Spinlock)
- [第十章 信号量（Semaphore）](#第十章-信号量Semaphore)
- [第十一章 互斥体（Mutex）](#第十一章-互斥体Mutex)
- [第十二章 四种并发保护机制对比](#第十二章-四种并发保护机制对比)
- [第十三章 按键输入驱动](#第十三章-按键输入驱动)
- [第十四章 内核定时器](#第十四章-内核定时器)

---

## 第一章 字符设备驱动基础

### 1. 实验目的

学习 Linux 内核模块开发，掌握字符设备驱动的基本框架：注册、注销、文件操作回调函数的实现，以及用户空间程序如何与内核驱动通过设备文件交互。

### 2. 整体架构

```
用户空间（User Space）              内核空间（Kernel Space）
┌─────────────────────┐          ┌──────────────────────────┐
│ chrdevbaseAPP       │          │ chrdevbase.ko            │
│                     │  open()  │                          │
│  fd = open("/dev/   │ ───────> │ chrdevbase_open()        │
│    chrdevbase",     │          │                          │
│    O_RDWR)          │  read()  │ chrdevbase_read()        │
│                     │ ───────> │   ┌─ memcpy(readbuf,     │
│  read(fd, buf, 50)  │          │   │    kerneldata)       │
│                     │          │   └─ copy_to_user()      │
│                     │ <─────── │                          │
│                     │  write() │ chrdevbase_write()       │
│  write(fd, buf, 50) │ ───────> │   ┌─ copy_from_user()    │
│                     │          │   └─ printk()            │
│                     │ close()  │                          │
│  close(fd)          │ ───────> │ chrdevbase_release()    │
└─────────────────────┘          └──────────────────────────┘
```

### 3. 关键数据结构

### file_operations

驱动通过 `struct file_operations` 向内核注册回调函数指针，将用户空间的 `read`/`write`/`open`/`close` 系统调用映射到驱动中的具体函数：

```c
static struct file_operations chrdevbase_fops = {
    .owner   = THIS_MODULE,         // 模块引用计数
    .open    = chrdevbase_open,     // 对应 open() 系统调用
    .release = chrdevbase_release,  // 对应 close() 系统调用
    .read    = chrdevbase_read,     // 对应 read() 系统调用
    .write   = chrdevbase_write,    // 对应 write() 系统调用
};
```

### 主设备号

`#define CHRDEVBASE_MAJOR 200` — 主设备号是内核中设备的统一标识，范围 0~255 为静态分配。 `/dev/chrdevbase` 是一个设备节点，`c` 表示字符设备，`200 0` 表示主设备号 200、次设备号 0。

### 4. 驱动流程

### 4.1 加载 (insmod)

```
insmod chrdevbase.ko
  └─ module_init(chrdevbase_init)   // 宏展开为 __initcall
       └─ register_chrdev(200, "chrdevbase", &chrdevbase_fops)
            └─ 向内核注册：主设备号 200 → file_operations 绑定
```

### 4.2 用户打开设备

```
open("/dev/chrdevbase", O_RDWR)
  └─ 内核根据设备号 200 查找 file_operations
       └─ chrdevbase_open(inode, filp)
```

### 4.3 读取数据

```
read(fd, buf, count)
  └─ chrdevbase_read(filp, buf, count, ppos)
       1. 边界检查，防止 count 越界
       2. memcpy(readbuf, kerneldata)  — 内核数据拷贝到驱动内部缓冲
       3. copy_to_user(buf, readbuf)   — 驱动缓冲 → 用户空间 buf
       4. 返回实际读取字节数
```

### 4.4 写入数据

```
write(fd, buf, count)
  └─ chrdevbase_write(filp, buf, count, ppos)
       1. 边界检查，留 '\0' 位置
       2. copy_from_user(writebuf, buf) — 用户空间 buf → 驱动内部缓冲
       3. writebuf[count] = '\0'        — 字符串结尾
       4. printk()                      — 打印到内核日志
       5. 返回实际写入字节数
```

### 4.5 卸载 (rmmod)

```
rmmod chrdevbase
  └─ module_exit(chrdevbase_exit)
       └─ unregister_chrdev(200, "chrdevbase")
            └─ 从内核注销设备号 200 的绑定
```

### 5. copy_to_user / copy_from_user

用户空间和内核空间地址隔离，驱动**不能直接访问用户空间指针**。必须使用内核提供的专用函数：

| 函数 | 方向 | 返回值 |
|------|------|--------|
| `copy_to_user(to, from, n)` | 内核 → 用户 | 未拷贝的字节数，0 表示成功 |
| `copy_from_user(to, from, n)` | 用户 → 内核 | 未拷贝的字节数，0 表示成功 |
| `-EFAULT` | 出错时返回的错误码 | Bad address |

这两个函数内部包含 access_ok 权限检查，是安全的跨空间拷贝方式。

### 6. 运行步骤

```bash
# 1. 编译驱动模块
make

# 2. 加载驱动
sudo insmod chrdevbase.ko

# 3. 创建设备节点（只需一次）
sudo mknod /dev/chrdevbase c 200 0
sudo chmod 777 /dev/chrdevbase

# 4. 读测试：从驱动读取内核数据
sudo ./chrdevbaseAPP /dev/chrdevbase 1
# 输出: APP read data:kernel data!

# 5. 写测试：向驱动写入用户数据
sudo ./chrdevbaseAPP /dev/chrdevbase 2
# 内核日志: kernel recevdata:usr data!

# 6. 查看内核日志
dmesg | tail -10

# 7. 卸载驱动
sudo rmmod chrdevbase

# 8. 清理设备节点
sudo rm /dev/chrdevbase
```

### 7. Makefile 解析

```makefile
KERNELDIR := $(HOME)/wsl2-kernel     # 内核源码树路径
CURRENT_PATH := $(shell pwd)          # 当前模块源码路径
obj-m := chrdevbase.o                 # 告诉 kbuild 编译成 .ko 模块

kernel_modules:
    $(MAKE) -C $(KERNELDIR) M=$(CURRENT_PATH) modules
    # -C: 切换到内核源码目录，使用其顶层 Makefile
    # M=: 让内核构建系统回到模块目录找 obj-m 中列出的源文件
    # 这确保模块使用与内核完全一致的头文件、配置和编译选项
```

### 8. 完整执行流程与函数详解

### 8.1 总览：一条 read 调用走过的路

```
APP.c                              内核 VFS 层                        chrdevbase.c
─────                              ──────────                        ────────────

read(fd, readbuf, 50)              
  │  C库 → int $0x80 / syscall     sys_read(fd, buf=0x7fff_1234, 50)
  │                                │
  │                                通过 fd 查到内核 file 结构体
  │                                从中取出 f_op = &chrdevbase_fops
  │                                取出 f_op->read 即 chrdevbase_read
  │                                │
  │                                └────> chrdevbase_read(filp, buf=0x7fff_1234, count=50, ppos)
  │                                                                    │
  │                                                                    memcpy(readbuf, kerneldata, ...)
  │                                                                    copy_to_user(buf, readbuf, count)
  │                                                                    return count
  │                                <────
  │  返回值 = count                                                   
  readbuf 中已有数据
```

### 8.2 阶段一：加载驱动 (insmod)

**调用链：**

```
sudo insmod chrdevbase.ko
  → module_init(chrdevbase_init)     // 宏展开，内核在模块加载时自动调用
```

**函数详解：**

```c
// 函数签名
static int __init chrdevbase_init(void);

// 传入：无
// 传出：0 成功，负值失败
// 核心操作：
ret = register_chrdev(CHRDEVBASE_MAJOR,      // 主设备号 200
                      CHRDEVBASE_NAME,        // 设备名 "chrdevbase"
                      &chrdevbase_fops);      // 操作函数表指针
```

`register_chrdev()` 做的事：在内核的字符设备全局注册表（`chrdevs[]` 数组）中，把 **主设备号 200** 这个槽位，指向你提供的 `chrdevbase_fops`。此后任何对设备号 200 的 open 请求，内核都会从这个表里取出你的 fops。

---

### 8.3 阶段二：创建设备节点 (mknod)

```
sudo mknod /dev/chrdevbase c 200 0
```

mknod 在文件系统上创建一个设备文件 `/dev/chrdevbase`，文件属性中存了 `(c, 200, 0)`，即：字符设备、主设备号200、次设备号0。此时只是创建了一个文件路径，**还没有触发任何驱动代码**。

---

### 8.4 阶段三：打开设备 (open)

**调用链：**

```
APP: fd = open("/dev/chrdevbase", O_RDWR)
  → C库 → 系统调用 sys_open
    → VFS: 根据路径找到 inode，发现是设备文件（主=200,次=0）
    → VFS: 在 chrdevs[200] 中取出之前注册的 chrdevbase_fops
    → VFS: 创建内核 file 结构体，将 f_op = &chrdevbase_fops 挂上去
    → VFS: 调用 f_op->open(inode, filp)
      → chrdevbase_open(inode, filp)   ← 你的函数被调用了
    → 返回 fd=3（整数文件描述符）给 APP
```

**用户侧入参 → 驱动侧入参 映射：**

| 用户调用 | VFS 转换后 | 说明 |
|----------|-----------|------|
| `"/dev/chrdevbase"` | `inode`（内核 inode 指针） | 路径被解析成索引节点 |
| `O_RDWR` | `filp->f_flags` | 打开标志存入文件对象 |
| fd=3（返回值）| — | 用户拿到的只是一个整数编号 |

**函数详解：**

```c
// 函数签名
static int chrdevbase_open(struct inode *inode, struct file *filp);

// 传入：
//   inode — 设备文件的索引节点，包含设备号等信息
//   filp  — 新创建的内核文件对象，f_op 已指向 chrdevbase_fops
// 传出：0 成功，负值失败
// 本实验中为空实现，仅返回 0
```

**关键理解：** `open` 阶段完成了"绑定"——内核 file 结构体的 `f_op` 字段永久指向 `chrdevbase_fops`。之后的 `read`/`write`/`close` 都**直接从这个 file 结构体取函数指针**，不再重复查表。

---

### 8.5 阶段四：读取数据 (read) — 核心流程

**调用链：**

```
APP: ret = read(fd, readbuf, 50)
  → C库 → 系统调用 sys_read(fd, buf, count)
    → VFS: 根据 fd=3 找到内核 file 结构体
    → VFS: 取出 file->f_op->read，即 chrdevbase_read
    → VFS: 拼装参数，调用 chrdevbase_read(filp, buf, count, ppos)
      → 驱动内部执行（见下方详细流程）
    → 返回 count 给 APP
```

**参数映射详解：**

| APP 调用 | VFS 层 | 驱动函数收到的 | 变化说明 |
|----------|--------|---------------|---------|
| `fd` (int = 3) | 内核查 fd 表 → file 结构体 | `filp` (struct file *) | **完全替换**：int 编号 → 完整内核对象 |
| `readbuf` (char *, 0x7fff_1234) | 原值透传 | `buf` (char __user *, 0x7fff_1234) | **不变**：指向 APP 栈上的同一块内存 |
| `50` (size_t) | 原值透传 | `count` (size_t, 50) | **不变** |
| — | 内核自动添加 | `ppos` (loff_t *) | **新增**：指向 file 结构体中的文件偏移量 |

**函数详解：**

```c
// 函数签名
static ssize_t chrdevbase_read(struct file *filp,    // 文件对象
                                char __user *buf,     // 用户空间目标地址（= APP的readbuf）
                                size_t count,         // 用户请求的字节数（= 50）
                                loff_t *ppos);        // 文件偏移指针

// 传入：
//   filp  — 内核文件对象，open 时创建
//   buf   — 用户空间缓冲区地址（就是 APP 中 readbuf 变量的地址）
//   count — 用户想读多少字节
//   ppos  — 文件读写位置（本实验未使用）
//
// 传出：>0 = 实际读到的字节数，负数 = 错误码（如 -EFAULT）
```

**函数内部执行步骤：**

```
chrdevbase_read(filp, buf=0x7fff_1234, count=50, ppos)
│
├─ 步骤1: 边界检查
│   if (count > sizeof(readbuf))     // 50 > 100? → 否，不触发
│       count = sizeof(readbuf);     // 确保不越界
│
├─ 步骤2: 数据源 → 内核工作缓冲
│   memcpy(readbuf, kerneldata, sizeof(kerneldata));
│   // readbuf (0xffff_xxxx, 内核空间) ← "kernel data!"
│   // 为什么需要 readbuf 中转？
│   //   1. 真实驱动中数据可能来自硬件寄存器，先读到工作缓冲
│   //   2. 配合 ppos 支持分段读取（本次读前30字节，下次读剩余部分）
│   //   3. 可在拷出前做校验/解密/格式化等预处理
│
├─ 步骤3: 内核空间 → 用户空间（核心！）
│   ret = copy_to_user(buf=0x7fff_1234, readbuf=0xffff_xxxx, count=50);
│   //                     ↑                  ↑
│   //              这就是 APP 的 readbuf！   内核的临时缓冲
│   //   copy_to_user 内部：
│   //     a. access_ok() 校验用户地址是否可写
│   //     b. 逐字节从内核地址拷贝到用户地址
│   //   ret = 0 表示全部拷贝成功
│   //   ret > 0 表示有 ret 个字节没拷过去
│   if (ret)
│       return -EFAULT;   // 部分失败，告诉 APP "Bad address"
│
└─ 步骤4: 返回
    return count;  // 返回实际传输的字节数
                   // 这个值会一路回到 APP 作为 read() 的返回值
```

**数据流向总结：**

```
kerneldata[]           readbuf[]            buf (即APP的readbuf)
(内核常量字符串)  →    (内核工作缓冲)  →    (用户空间变量)
"kernel data!"    memcpy             copy_to_user
  0xffff_xxxx_A     0xffff_xxxx_B      0x7fff_1234
```

---

### 8.6 阶段五：写入数据 (write)

**调用链：**

```
APP: write(fd, writebuf, 50)
  → C库 → 系统调用 sys_write(fd, buf, count)
    → VFS: 根据 fd=3 找到内核 file 结构体
    → VFS: 取出 file->f_op->write，即 chrdevbase_write
    → 调用 chrdevbase_write(filp, buf, count, ppos)
```

**函数详解：**

```c
// 函数签名
static ssize_t chrdevbase_write(struct file *filp,     // 文件对象
                                 const char __user *buf, // 用户空间源地址（= APP的writebuf）
                                 size_t count,           // 用户要写多少字节
                                 loff_t *ppos);          // 文件偏移指针

// 传入：
//   buf   — 指向 APP 中 writebuf 的地址（存了 "usr data!"）
//   count — 50
//
// 传出：>0 = 实际写入字节数，负数 = 错误码
```

**函数内部执行步骤：**

```
chrdevbase_write(filp, buf=0x7fff_5678, count=50, ppos)
│
├─ 步骤1: 边界检查（留 '\0' 位置）
│   if (count > sizeof(writebuf) - 1)   // 50 > 99? → 否
│       count = sizeof(writebuf) - 1;
│
├─ 步骤2: 用户空间 → 内核空间
│   ret = copy_from_user(writebuf, buf, count);
│   //     从用户 buf (0x7fff_5678) 拷 50 字节到内核 writebuf
│   //     用户 buf 指向 APP 中 writebuf 变量（内容是 "usr data!"）
│   if (ret)
│       return -EFAULT;
│
├─ 步骤3: 收尾
│   writebuf[count] = '\0';  // 手动补字符串结束符，安全打印
│
├─ 步骤4: 验证数据
│   printk("kernel recevdata:%s\r\n", writebuf);
│   // 输出到内核日志：kernel recevdata:usr data!
│   // 通过 dmesg 查看
│
└─ 步骤5: 返回
    return count;
```

---

### 8.7 阶段六：关闭设备 (close)

**调用链：**

```
APP: close(fd)
  → C库 → 系统调用 sys_close(fd)
    → VFS: 根据 fd 找到 file 结构体
    → VFS: 调用 file->f_op->release(inode, filp)
      → chrdevbase_release(inode, filp)
```

**函数详解：**

```c
// 函数签名
static int chrdevbase_release(struct inode *inode, struct file *filp);

// 传入：同 open，inode + filp
// 传出：0 成功
// 本实验中为空实现
```

---

### 8.8 阶段七：卸载驱动 (rmmod)

**调用链：**

```
sudo rmmod chrdevbase
  → module_exit(chrdevbase_exit)
```

**函数详解：**

```c
// 函数签名
static void __exit chrdevbase_exit(void);

// 传入：无
// 传出：无
// 核心操作：
unregister_chrdev(CHRDEVBASE_MAJOR, CHRDEVBASE_NAME);
// 从内核全局表中移除设备号 200 的注册
```

---

### 8.9 全部函数速查表

| 函数 | 所在文件 | 触发方式 | 参数 → 返回值 | 核心作用 |
|------|---------|---------|-------------|---------|
| `chrdevbase_init()` | chrdevbase.c | `insmod` | `void → int (0成功/<0失败)` | 注册字符设备，绑定主设备号与 fops |
| `chrdevbase_open()` | chrdevbase.c | `open()` | `inode, filp → int (0)` | 设备打开回调（本实验空实现） |
| `chrdevbase_read()` | chrdevbase.c | `read()` | `filp, buf, count, ppos → ssize_t (字节数/-EFAULT)` | 内核数据 → copy_to_user → 用户空间 |
| `chrdevbase_write()` | chrdevbase.c | `write()` | `filp, buf, count, ppos → ssize_t (字节数/-EFAULT)` | 用户空间 → copy_from_user → 内核打印 |
| `chrdevbase_release()` | chrdevbase.c | `close()` | `inode, filp → int (0)` | 设备关闭回调（本实验空实现） |
| `chrdevbase_exit()` | chrdevbase.c | `rmmod` | `void → void` | 注销字符设备 |
| `main()` | chrdevbaseAPP.c | 命令行执行 | `argc, argv → int (0成功/-1失败)` | 用户态测试：open/read/write/close |

### 8.10 寄存器类比

本实验中的数据缓冲区和真实硬件驱动的对应关系：

| 本实验（虚拟） | 真实硬件驱动 | 操作 |
|---------------|------------|------|
| `kerneldata[]` | 硬件寄存器（如 ADC 数据寄存器） | 数据源 |
| `readbuf[]` | 驱动的 DMA 缓冲区 / 临时缓冲 | 内核内部工作区 |
| `buf`（用户传入） | 完全一样 | 用户空间目标 |
| `memcpy(readbuf, kerneldata)` | `value = ioread32(reg_addr)` | 从数据源获取数据 |
| `copy_to_user(buf, readbuf)` | 完全一样 | 安全地交给用户 |
| `writebuf[]` | 驱动的写缓冲 / DMA 发送区 | 内核内部工作区 |
| `copy_from_user(writebuf, buf)` | 完全一样 | 从用户安全获取数据 |
| `printk(writebuf)` | `iowrite32(value, reg_addr)` | 把数据发送到硬件 |

> 核心结论：这个实验虽然没操作真实硬件，但**整个框架和真实驱动一模一样**。将来写 LED、按键、串口驱动时，唯一要改的就是把 `memcpy(kerneldata)` 换成读写硬件寄存器的代码。

### 9. 环境说明

- **OS**: Ubuntu 24.04 LTS on WSL2
- **内核**: 自编译 6.6.87.2-microsoft-standard-WSL2+ (GCC 13.3.0)
- **关键点**: WSL2 默认内核未启用模块加载支持或存在 GCC 版本不匹配，需要手动编译自己的 WSL2 内核并替换，模块才能正常加载

---

## 第二章 LED 字符设备驱动（真实 GPIO）

### 1. 实验目的

在 chrdevbase 虚拟字符设备的基础上，进阶到**操作真实硬件**——通过 GPIO 驱动控制 i.MX6ULL 开发板上的 LED 灯。核心学习点：
- `ioremap` 将物理寄存器地址映射为虚拟地址
- `readl` / `writel` 读写硬件寄存器
- GPIO 外设的完整初始化流程（时钟 → 复用 → 电气属性 → 方向 → 电平）
- 与 chrdevbase 的对比：数据来源从内存数组变成了硬件寄存器

### 2. 整体架构

```
用户空间                             内核空间
┌────────────────────┐            ┌─────────────────────────────────┐
│ ledAPP             │            │ led.ko                         │
│                    │  open()    │                                 │
│ fd = open(         │ ────────> │ led_open()                      │
│   "/dev/led")      │            │                                 │
│                    │  write()   │ led_write()                     │
│ databuf[0] = 1     │ ────────> │   copy_from_user(databuf, buf)  │
│ write(fd, buf, 1)  │            │   led_switch(databuf[0])        │
│                    │            │    ┌ readl(GPIO1_DR) ────┐     │
│                    │            │    │ val &= ~(1<<3)      │     │
│                    │            │    │ writel(val, GPIO1_DR)│     │
│                    │            │    └──────────────────────┘     │
│                    │            │         ↓                       │
│                    │            │   ┌─────────────────┐           │
│                    │  close()   │   │ i.MX6ULL 芯片    │           │
│                    │ ────────> │   │ GPIO1_IO03 引脚  │           │
│                    │            │   │ → 低电平 → LED亮 │           │
└────────────────────┘            │   └─────────────────┘           │
                                  └─────────────────────────────────┘
```

### 3. 与 chrdevbase 的关键区别

| | chrdevbase（实验1）| led（实验2）|
|---|---|---|
| 硬件依赖 | **无**（纯虚拟）| **有**（i.MX6ULL 开发板）|
| 数据来源/去向 | `kerneldata[]` 内存数组 | **GPIO1_DR 硬件寄存器** |
| 核心 API | `copy_to_user` / `copy_from_user` | `ioremap` / `readl` / `writel` |
| 地址类型 | 虚拟地址（内核默认）| **物理地址 → 虚拟地址（ioremap）** |
| 支持操作 | read + write | **仅 write**（LED 亮灭肉眼可见）|
| 初始化 | 仅 register_chrdev | **硬件初始化 + register_chrdev** |
| 可运行环境 | WSL (x86_64) | **必须 ARM 开发板**（i.MX6ULL）|

### 4. 核心新概念

### 4.1 物理地址 vs 虚拟地址

```
CPU 只能访问虚拟地址，不能直接访问物理地址
硬件寄存器位于物理地址空间（由芯片设计决定，写死在手册里）

物理地址 (0x0209C000)  ──ioremap()──>  虚拟地址 (GPIO1_DR 指针)
  │                                              │
  │  这是芯片手册上写的                             │  这是代码里用的
  │  代码不能直接用                                │  readl/writel 操作它
```

chrdevbase 里所有变量天生是虚拟地址，所以不需要映射。但硬件寄存器是物理地址，`ioremap` 是访问硬件的**第一步**。

### 4.2 readl / writel 不是 memcpy

```c
memcpy(dst, src, n);         // 普通内存拷贝
val = readl(GPIO1_DR);       // 读取硬件寄存器的当前值
writel(val, GPIO1_DR);       // 将值写入硬件寄存器
```

`readl`/`writel` 操作的是 **I/O 内存**，CPU 通过总线访问物理硬件，不是访问 RAM。它们确保：
- 操作顺序不会被编译器/CPU 乱序重排（内存屏障）
- 访问宽度正确（32 位对齐）
- 不会使用缓存（每次都是从硬件读最新值）

### 4.3 读-改-写模式

```c
val = readl(GPIO1_DR);       // ① 读出当前 32 位的值
val |= (1 << 3);             // ② 改目标 bit
writel(val, GPIO1_DR);       // ③ 整个 32 位写回
```

**不能直接写目标 bit**，因为寄存器按 32 位整字访问。如果跳过第①步直接写，会把其他 31 个 bit 全清为 0，破坏其他引脚的状态。读-改-写确保**只动目标 bit，其他 bit 保持不变**。

### 5. GPIO 硬件初始化流程（顺序不可颠倒）

GPIO 外设在 i.MX6ULL 上不是开箱即用的，必须按以下顺序逐级使能：

```
                        ┌─────────────────┐
                        │ ① 地址映射       │
                        │ ioremap(物理→虚拟)│
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │ ② 使能外设时钟   │
                        │ CCM_CCGR1        │
                        │ bit[27:26]=11    │
                        └────────┬────────┘
                                 │ 时钟不开，GPIO 模块不供电！
                        ┌────────▼────────┐
                        │ ③ 引脚功能复用   │
                        │ SW_MUX = 0x5    │
                        │ (选 GPIO，不选I2C)│
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │ ④ 引脚电气属性   │
                        │ SW_PAD = 0x10B0 │
                        │ (驱动/速度/上下拉)│
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │ ⑤ GPIO 方向     │
                        │ GDIR bit3 = 1  │
                        │ (输出模式)       │
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │ ⑥ GPIO 初始电平  │
                        │ DR bit3 = 1    │
                        │ (高电平, LED灭)  │
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │ ⑦ register_chrdev│
                        │ 向内核注册设备     │
                        └─────────────────┘
```

### 各寄存器详解

| 寄存器 | 物理地址 | 作用 | 本实验设置 |
|--------|---------|------|-----------|
| CCM_CCGR1 | 0x020C406C | 外设时钟门控 | bit[27:26]=11，GPIO1 时钟开启 |
| SW_MUX | 0x020E0068 | 引脚功能选择 | 0x5 = ALT5 = GPIO1_IO03 |
| SW_PAD | 0x020E02F4 | 电气属性 | 0x10B0，配置驱动能力/速度 |
| GPIO1_GDIR | 0x0209C004 | 方向（输入/输出）| bit3=1，输出 |
| GPIO1_DR | 0x0209C000 | 数据（高低电平）| bit3=1，高电平（LED灭）|

### 6. 完整执行流程

### 6.1 加载 (insmod)

```
insmod led.ko
  └─ led_init()
       ├─ ioremap × 5          → 五组物理地址 → 虚拟指针
       ├─ CCM_CCGR1 使能时钟     → GPIO1 外设上电
       ├─ SW_MUX 引脚复用        → 选 GPIO 功能
       ├─ SW_PAD 电气属性        → 配置驱动参数
       ├─ GDIR 方向 = 输出       → 引脚设为输出模式
       ├─ DR 初始 = 高电平       → 默认 LED 灭
       └─ register_chrdev(200)  → 注册字符设备
```

### 6.2 用户开灯 (write)

```
APP: databuf[0] = 1; write(fd, databuf, 1)
  → sys_write → vfs_write → led_write(filp, buf, 1, ppos)
       │
       ├─ copy_from_user(databuf, buf, 1)
       │   databuf[0] = 1  (APP 传来的开灯命令)
       │
       └─ led_switch(LEDON)
            ├─ val = readl(GPIO1_DR)      // 读当前 GPIO 电平状态
            ├─ val &= ~(1 << 3)            // bit3 清零 = 输出低电平
            └─ writel(val, GPIO1_DR)       // 写回寄存器 → 引脚变低 → LED 亮！
```

### 6.3 用户关灯 (write)

```
APP: databuf[0] = 0; write(fd, databuf, 1)
  → led_write → led_switch(LEDOFF)
       ├─ val = readl(GPIO1_DR)
       ├─ val |= (1 << 3)             // bit3 置 1 = 输出高电平
       └─ writel(val, GPIO1_DR)       // → 引脚变高 → LED 灭！
```

### 6.4 卸载 (rmmod)

```
rmmod led
  └─ led_exit()
       ├─ 关灯（安全）        → GPIO 输出高电平
       ├─ iounmap × 5        → 释放 ioremap 映射
       └─ unregister_chrdev  → 注销字符设备
```

### 7. 数据流向详解

### chrdevbase（实验1）数据流

```
用户 read() → copy_to_user() ← memcpy ← kerneldata[] (内存数组)
用户 write() → copy_from_user() → writebuf[] → printk (内核日志)
```

### led（实验2）数据流

```
用户 write(databuf="1") → copy_from_user() → databuf[0]=1
                              ↓
                        led_switch(1)
                              ↓
                    readl(GPIO1_DR)     ← 从物理硬件读
                    val &= ~(1<<3)      ← 内核修改 CPU
                    writel(val, GPIO1_DR) → 写到物理硬件
                              ↓
                     i.MX6ULL 芯片 GPIO1_IO03 引脚
                              ↓
                          LED 发光！
```

**本质区别：** chrdevbase 的数据终点是内核日志（软件），led 的数据终点是**芯片引脚的电平**（物理世界）。

### 8. 全部函数速查表

| 函数 | 文件 | 触发 | 参数 → 返回值 | 作用 |
|------|------|------|-------------|------|
| `led_init()` | led.c | insmod | `void → int (0/-EIO)` | GPIO 初始化 + 注册字符设备 |
| `led_open()` | led.c | open() | `inode, filp → 0` | 空实现 |
| `led_write()` | led.c | write() | `filp, buf, count, ppos → 0/-EFAULT` | 接收命令，调用 led_switch |
| `led_switch()` | led.c | 内部调用 | `u8 sta (LEDON/LEDOFF) → void` | 读-改-写 GPIO 寄存器控制引脚电平 |
| `led_release()` | led.c | close() | `inode, filp → 0` | 空实现 |
| `led_exit()` | led.c | rmmod | `void → void` | 关灯 + iounmap + 注销设备 |
| `main()` | ledAPP.c | 命令行 | `argc, argv → int` | 通过 write 发送开/关灯命令 |

### 函数调用关系图

```
insmod                   APP open()        APP write()        APP close()      rmmod
  │                         │                  │                  │               │
  ▼                         ▼                  ▼                  ▼               ▼
led_init()              led_open()        led_write()       led_release()    led_exit()
  │                                          │                                  │
  ├─ ioremap × 5                             ├─ copy_from_user                 ├─ 关灯
  ├─ CCM 时钟                               └─ led_switch()                   ├─ iounmap × 5
  ├─ SW_MUX                                     ├─ LEDON:                    └─ unregister
  ├─ SW_PAD                                     │    readl → &=~(1<<3)→writel
  ├─ GDIR                                       └─ LEDOFF:
  ├─ DR                                              readl → |=(1<<3)→writel
  └─ register_chrdev
```

### 9. 运行步骤（需要 i.MX6ULL 开发板）

```bash
# 0. 编译（WSL 上可做）
make

# 1. 将 led.ko 和 ledAPP 拷贝到开发板（通过 NFS/TFTP/scp）

# 2. 在开发板上加载驱动
insmod led.ko

# 3. 创建设备节点
mknod /dev/led c 200 0

# 4. 开灯
./ledAPP /dev/led 1

# 5. 关灯
./ledAPP /dev/led 0

# 6. 卸载
rmmod led.ko
```

### 10. 为什么 WSL 上只能编译不能运行

| | WSL (x86_64) | i.MX6ULL (ARM Cortex-A7) |
|---|---|---|
| 物理地址 0x0209C000 | **不存在**，ioremap 会失败 | 对应 GPIO1_DR 寄存器 |
| GPIO 外设 | **无** | 有 GPIO1～GPIO5 |
| LED 引脚 | 无 | GPIO1_IO03（芯片物理引脚）|

在 WSL 上 `insmod led.ko` 会直接触发内核错误（ioremap 非法地址），需要物理开发板才能实际运行。

### 11. 实验总结

本实验完成了从"虚拟字符设备"到"真实硬件驱动"的跨越：

1. **chrdevbase** 教你驱动框架（file_operations + register_chrdev + copy_to_user）
2. **led** 在此基础上教会你操作真实硬件（ioremap + readl/writel + 寄存器编程）

后续所有实验（按键、定时器、I2C、SPI 等）都是这套模式的变体：**驱动框架不变，变的是硬件寄存器的操作方式**。

### 12. 环境说明

- **开发环境**: Ubuntu 24.04 LTS on WSL2 (x86_64)，用于编译
- **运行环境**: 正点原子阿尔法 i.MX6ULL 开发板 (ARM)，用于实际运行
- **WSL 内核**: 自编译 6.6.87.2-microsoft-standard-WSL2+，仅用于模块编译验证
- **真实内核**: i.MX6ULL Linux 4.1.15，模块在此内核上加载运行

---

## 第三章 新字符设备 LED 驱动

### 1. 实验目的

在 `2_led`（真实 GPIO 硬件驱动）的基础上，引入**新字符设备驱动框架**，解决旧版 `register_chrdev` 的两个痛点：
- **主设备号硬编码**：`register_chrdev(200, ...)` 固定写死 200，如果被其他驱动占用则加载失败
- **需要手动 mknod**：每次加载后都要 `mknod /dev/xxx c 200 0` 手动创建设备节点，繁琐且易出错

核心学习点：
- `alloc_chrdev_region` / `register_chrdev_region` — 设备号的动态/静态分配
- `cdev_init` + `cdev_add` — 标准字符设备注册流程
- `class_create` + `device_create` — 自动在 `/dev` 下创建设备节点
- goto 风格的错误回滚模式

### 2. 整体架构

```
用户空间                                    内核空间
┌────────────────────────┐            ┌──────────────────────────────────────┐
│ ledAPP                  │            │ newchrled.ko                         │
│                         │ open()    │                                      │
│ fd = open(              │ ────────> │ newchrled_open()                     │
│   "/dev/newchrled")     │           │   filp->private_data = &newchrled     │
│                         │ write()   │                                      │
│ databuf[0] = 1          │ ────────> │ newchrled_write()                    │
│ write(fd, buf, 1)       │           │   copy_from_user(databuf, buf, 1)    │
│                         │           │   led_switch(databuf[0])              │
│                         │           │    ┌ readl(GPIO1_DR) ────┐           │
│                         │           │    │ val &= ~(1<<3)      │           │
│                         │           │    │ writel(val, GPIO1_DR)│           │
│                         │           │    └──────────────────────┘           │
│                         │           │              ↓                        │
│                         │ close()   │   ┌─────────────────┐                │
│                         │ ────────> │   │ i.MX6ULL 芯片    │                │
│                         │           │   │ GPIO1_IO03 引脚  │                │
│                         │           │   │ → 低电平 → LED亮 │                │
└────────────────────────┘            │   └─────────────────┘                │
                                      └──────────────────────────────────────┘

自动创建：insmod 后 /dev/newchrled 自动出现，无需 mknod
```

### 3. 与 chrdevbase 和 led 的关键区别

| | chrdevbase（实验1）| led（实验2）| **newchrled（实验3）**|
|---|---|---|---|
| 硬件依赖 | 无（纯虚拟）| i.MX6ULL 开发板 | i.MX6ULL 开发板 |
| 数据来源/去向 | `kerneldata[]` 内存数组 | GPIO1_DR 硬件寄存器 | GPIO1_DR 硬件寄存器 |
| 主设备号 | **硬编码 200** | **硬编码 200** | **动态分配**（alloc_chrdev_region）|
| 字符设备注册 | register_chrdev | register_chrdev | **cdev_init + cdev_add** |
| 设备节点创建 | 手动 mknod | 手动 mknod | **自动创建**（device_create）|
| 设备结构 | 无（零散全局变量）| 无（零散全局变量）| **struct newchrled_dev** |
| 设备号释放 | unregister_chrdev | unregister_chrdev | **unregister_chrdev_region** |
| 支持操作 | read + write | 仅 write | 仅 write |
| WSL 可运行 | 是 | 否 | 否 |

### 4. 核心新概念

### 4.1 旧 vs 新：字符设备注册方式对比

```
【旧方式】register_chrdev — 一个函数搞定
┌─────────────────────────────────────────────┐
│ register_chrdev(200, "led", &led_fops)      │
│   ├─ 内部调用 __register_chrdev_region      │  （申请设备号）│
│   ├─ 内部调用 cdev_alloc + cdev_add         │  （注册 cdev）│
│   └─ 缺点：① 主设备号固定 ② 次设备号全占   │
│             ③ 不灵活，无法精细控制          │
└─────────────────────────────────────────────┘

【新方式】alloc + cdev + class — 分三步，精细控制
┌─────────────────────────────────────────────┐
│ ① alloc_chrdev_region(&devid, 0, 1, name)   │  申请设备号（动态）│
│ ② cdev_init(&cdev, &fops)                   │  绑定 fops       │
│    cdev_add(&cdev, devid, 1)                │  注册到内核       │
│ ③ class_create(THIS_MODULE, name)            │  创建类           │
│    device_create(class, NULL, devid, ...)    │  创建 /dev 节点  │
└─────────────────────────────────────────────┘
```

### 4.2 设备号分配：静态 vs 动态

```c
/* 方式A：静态分配（主设备号已知）*/
newchrled.major = 200;   // 手动指定
newchrled.devid = MKDEV(newchrled.major, 0);
ret = register_chrdev_region(newchrled.devid, 1, "newchrled");

/* 方式B：动态分配（本实验使用的方式）*/
newchrled.major = 0;     // 0 = 让内核自动找空闲号
ret = alloc_chrdev_region(&newchrled.devid, 0, 1, "newchrled");
newchrled.major = MAJOR(newchrled.devid);  // 提取内核分配的主设备号
newchrled.minor = MINOR(newchrled.devid);  // 提取次设备号
```

**dev_t 设备号结构：**
```
dev_t (32位)
├── 高12位: 主设备号 (MAJOR) → 区分不同驱动
└── 低20位: 次设备号 (MINOR) → 区分同类不同设备

MKDEV(major, minor) → dev_t   // 合成设备号
MAJOR(dev_t) → major          // 提取主设备号
MINOR(dev_t) → minor          // 提取次设备号
```

### 4.3 cdev 结构体 — 字符设备的核心

```c
struct cdev {
    struct kobject kobj;          // 内核对象（嵌入用于引用计数/sysfs）
    struct module *owner;         // 所属模块（THIS_MODULE）
    const struct file_operations *ops;  // 操作集合指针
    struct list_head list;        // 链入内核的 cdev 全局链表
    dev_t dev;                    // 设备号
    unsigned int count;           // 此 cdev 管理的设备数量
};
```

**cdev 使用流程：**
```c
cdev_init(&cdev, &fops);    // ① 将 cdev 与 file_operations 绑定
cdev_add(&cdev, devid, 1);  // ② 将 cdev 添加到内核设备管理系统中

// 此时 APP 调用 open("/dev/newchrled") → 内核通过 devid 找到 cdev
// → 从 cdev 取出 fops → 调用 fops->open()
```

### 4.4 class + device — 自动创建设备节点

```c
/* 第1步：创建设备类 → 在 /sys/class/newchrled/ 下出现 */
newchrled.class = class_create(THIS_MODULE, "newchrled");

/* 第2步：创建设备 → 在 /dev/newchrled 自动出现设备节点 */
newchrled.device = device_create(newchrled.class, NULL,
                                 newchrled.devid, NULL, "newchrled");
```

**原理：** `device_create` 会向用户空间发送 uevent 消息，udev/mdev 守护进程接收到后自动在 `/dev` 创建对应的设备节点。这样就不需要手动 `mknod` 了。

### 4.5 goto 错误回滚 — 内核标准错误处理模式

```c
/* 正向执行：每步成功后继续 */
if (alloc_chrdev_region(...) < 0)    goto fail_devid;   // 步骤失败 → 跳转
if (cdev_add(...) < 0)               goto fail_cdev;    // 步骤失败 → 跳转+清理第1步
if (IS_ERR(class_create(...)))       goto fail_class;    // 步骤失败 → 跳转+清理第1,2步
if (IS_ERR(device_create(...)))      goto fail_device;   // 步骤失败 → 跳转+清理第1,2,3步
return 0;  // 全部成功

/* 回滚：后注册的先清理 */
fail_device:  class_destroy(class);       // 第4步失败 → 清理第3步
fail_class:   cdev_del(&cdev);            // 第3步失败 → 清理第2步
fail_cdev:    unregister_chrdev_region(); // 第2步失败 → 清理第1步
fail_devid:   return ret;                 // 第1步失败 → 直接返回
```

### 5. GPIO 硬件初始化流程（步骤1～6）

与 `2_led` 完全相同，顺序不可颠倒：

```
                    ┌─────────────────┐
                    │ ① 地址映射       │
                    │ ioremap(物理→虚拟)│
                    │ ×5个寄存器       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ ② 使能外设时钟   │
                    │ CCM_CCGR1        │
                    │ bit[27:26]=11    │
                    └────────┬────────┘
                             │ 时钟不开 = GPIO 模块不供电！
                    ┌────────▼────────┐
                    │ ③ 引脚功能复用   │
                    │ SW_MUX = 0x5    │
                    │ (ALT5 = GPIO)    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ ④ 引脚电气属性   │
                    │ SW_PAD = 0x10B0 │
                    │ (驱动/速度/上下拉)│
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ ⑤ GPIO 方向     │
                    │ GDIR bit3 = 1  │
                    │ (输出模式)       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ ⑥ GPIO 初始电平  │
                    │ DR bit3 = 1    │
                    │ (高电平, LED灭)  │
                    └─────────────────┘
```

### 各寄存器详解

| 寄存器 | 物理地址 | 作用 | 本实验设置 |
|--------|---------|------|-----------|
| CCM_CCGR1 | 0x020C406C | 外设时钟门控 | bit[27:26]=11，GPIO1 时钟开启 |
| SW_MUX | 0x020E0068 | 引脚功能选择 | 0x5 = ALT5 = GPIO1_IO03 |
| SW_PAD | 0x020E02F4 | 电气属性 | 0x10B0，配置驱动能力/速度 |
| GPIO1_GDIR | 0x0209C004 | 方向（输入/输出）| bit3=1，输出 |
| GPIO1_DR | 0x0209C000 | 数据（高低电平）| bit3=1，高电平（LED灭）|

### 6. 完整执行流程

### 6.1 模块加载 (insmod)

```
insmod newchrled.ko
  └─ newchrled_init()
       │
       │  === 第1阶段：硬件初始化（与led.c相同）===
       ├─ ioremap × 5              → 五组物理地址 → 虚拟指针
       ├─ CCM_CCGR1 使能时钟        → GPIO1 外设上电
       ├─ SW_MUX 引脚复用 = 0x5     → 选 GPIO 功能
       ├─ SW_PAD 电气属性 = 0x10B0  → 配置驱动参数
       ├─ GDIR 方向 = 输出          → 引脚设为输出模式
       ├─ DR 初始 = 高电平          → 默认 LED 灭
       │
       │  === 第2阶段：新字符设备驱动框架（与led.c不同）===
       ├─ alloc_chrdev_region      → 内核分配空闲主设备号（如 248）
       │   printk: major=248, minor=0
       ├─ cdev_init + cdev_add     → 注册字符设备到内核
       ├─ class_create             → 创建 /sys/class/newchrled/
       └─ device_create            → uevent → udev/mdev → 自动创建 /dev/newchrled
```

### 6.2 用户开灯 (write)

```
APP: databuf[0] = 1; write(fd, databuf, 1)
  → sys_write → vfs_write → newchrled_write(filp, buf, 1, ppos)
       │
       ├─ copy_from_user(databuf, buf, 1)
       │   databuf[0] = 1  （APP 传来的开灯命令）
       │
       └─ led_switch(LEDON)
            ├─ val = readl(GPIO1_DR)       // 读当前 GPIO 电平状态
            ├─ val &= ~(1 << 3)             // bit3 清零 = 低电平
            └─ writel(val, GPIO1_DR)        // 写回 → 引脚变低 → LED 亮
```

### 6.3 用户关灯 (write)

```
APP: databuf[0] = 0; write(fd, databuf, 1)
  → newchrled_write → led_switch(LEDOFF)
       ├─ val = readl(GPIO1_DR)
       ├─ val |= (1 << 3)              // bit3 置1 = 高电平
       └─ writel(val, GPIO1_DR)        // → 引脚变高 → LED 灭
```

### 6.4 模块卸载 (rmmod)

```
rmmod newchrled
  └─ newchrled_exit()
       ├─ 关灯（安全状态）       → GPIO 高电平，LED 灭
       ├─ iounmap × 5            → 释放 ioremap 映射
       ├─ cdev_del               → 删除字符设备
       ├─ unregister_chrdev_region → 释放设备号
       ├─ device_destroy         → 删除 /dev/newchrled 节点
       └─ class_destroy          → 删除 /sys/class/newchrled/
```

### 7. 全部函数速查表

| 函数 | 文件 | 触发 | 作用 |
|------|------|------|------|
| `newchrled_init()` | newchrled.c | insmod | GPIO 初始化 + 新字符设备框架注册 |
| `newchrled_exit()` | newchrled.c | rmmod | 关灯 + iounmap + cdev_del + 释放设备号 |
| `newchrled_open()` | newchrled.c | open() | 设置 filp->private_data 指向设备结构体 |
| `newchrled_write()` | newchrled.c | write() | copy_from_user 接收命令 → led_switch 控制 GPIO |
| `led_switch()` | newchrled.c | 内部调用 | 读-改-写 GPIO1_DR 寄存器，控制引脚电平 |
| `newchrled_release()` | newchrled.c | close() | 空实现（本实验无需清理）|
| `main()` | ledAPP.c | 命令行 | 打开设备 → 写入 0/1 命令 → 关闭设备 |

### 函数调用关系图

```
insmod                         rmmod
  │                               │
  ▼                               ▼
newchrled_init()              newchrled_exit()
  │                               │
  ├─ ioremap × 5                  ├─ 关灯
  ├─ CCM 时钟使能                  ├─ iounmap × 5
  ├─ SW_MUX 复用                  ├─ cdev_del
  ├─ SW_PAD 电气                  ├─ unregister_chrdev_region
  ├─ GDIR 方向                    ├─ device_destroy
  ├─ DR 初始电平                  └─ class_destroy
  ├─ alloc_chrdev_region
  ├─ cdev_init + cdev_add
  ├─ class_create
  └─ device_create

APP open()        APP write()         APP close()
  │                  │                   │
  ▼                  ▼                   ▼
newchrled_open()  newchrled_write()   newchrled_release()
  │                  │                   │
  └─ private_data    ├─ copy_from_user    (空)
                     └─ led_switch()
                          ├─ LEDON:  val &= ~(1<<3) → writel
                          └─ LEDOFF: val |=  (1<<3) → writel
```

### 8. 运行步骤（需要 i.MX6ULL 开发板）

```bash
# 0. 编译（WSL 上可做，需配置好交叉编译工具链和内核源码路径）
make

# 1. 将 newchrled.ko 和 ledAPP 拷贝到开发板（通过 NFS/TFTP/scp）

# 2. 在开发板上加载驱动
insmod newchrled.ko
# 输出: newchrled major=248, minor=0   （设备号由内核动态分配）

# 3. 检查设备节点自动创建
ls -l /dev/newchrled
# 输出: crw------- 1 root root 248, 0 Jan 1 00:00 /dev/newchrled

# 4. 开灯
./ledAPP /dev/newchrled 1

# 5. 关灯
./ledAPP /dev/newchrled 0

# 6. 卸载驱动（设备节点自动消失）
rmmod newchrled.ko
```

**注意：** 与 `2_led` 不同，**不需要手动执行 `mknod`**。`insmod` 后设备节点自动出现在 `/dev/` 下，`rmmod` 后自动消失。

### 9. 新旧框架代码对比

### 初始化对比

```c
/* ======= 旧版（led.c）======= */
static int __init led_init(void)
{
    // ... 硬件初始化相同 ...

    ret = register_chrdev(200, "led", &led_fops);  // 一个函数，主设备号固定
    // 之后需要手动 mknod /dev/led c 200 0
    return 0;
}

/* ======= 新版（newchrled.c）======= */
static int __init newchrled_init(void)
{
    // ... 硬件初始化相同 ...

    // ① 申请设备号（动态分配）
    alloc_chrdev_region(&newchrled.devid, 0, 1, "newchrled");

    // ② 注册字符设备
    cdev_init(&newchrled.cdev, &newchrled_fops);
    cdev_add(&newchrled.cdev, newchrled.devid, 1);

    // ③ 自动创建设备节点
    newchrled.class = class_create(THIS_MODULE, "newchrled");
    newchrled.device = device_create(newchrled.class, NULL,
                                     newchrled.devid, NULL, "newchrled");
    // /dev/newchrled 自动出现！
    return 0;
}
```


### 卸载对比

```c
/* ======= 旧版（led.c）======= */
static void __exit led_exit(void)
{
    // ... 关灯 + iounmap ...
    unregister_chrdev(200, "led");  // 一个函数搞定
}

/* ======= 新版（newchrled.c）======= */
static void __exit newchrled_exit(void)
{
    // ... 关灯 + iounmap ...
    cdev_del(&newchrled.cdev);
    unregister_chrdev_region(newchrled.devid, 1);
    device_destroy(newchrled.class, newchrled.devid);
    class_destroy(newchrled.class);
    // 加载时做了多少步，卸载时就逆向清理多少步
}
```

### 10. 实验总结

本实验在 `2_led` 的真实硬件驱动基础上，完成了**驱动框架的升级**：

1. **chrdevbase** — 学会驱动框架（file_operations + register_chrdev + copy_to/from_user）
2. **led** — 学会操作真实硬件（ioremap + readl/writel + 寄存器编程）
3. **newchrled** — 学会标准的新字符设备驱动模型（alloc_chrdev_region + cdev + class）

**三个实验的递进关系：**

- 框架能力：虚拟 → 真实硬件 → 真实硬件 + 完善的驱动框架
- 设备号：硬编码 → 硬编码 → 动态分配
- 设备节点：手动 mknod → 手动 mknod → 自动创建

后续所有实验（按键、定时器、I2C、SPI 等）都将基于这个"新字符设备驱动框架 + 硬件寄存器操作"的模式，只是硬件操作的具体寄存器不同。

### 11. 环境说明

- **开发环境**: Ubuntu 24.04 LTS on WSL2 (x86_64)，用于编写和交叉编译
- **运行环境**: 正点原子阿尔法 i.MX6ULL 开发板 (ARM Cortex-A7)
- **交叉编译器**: arm-linux-gnueabihf-gcc
- **目标内核**: i.MX6ULL Linux 4.1.15

---

## 第四章 设备树与 OF 函数

> 基于正点原子阿尔法Linux开发板 (I.MX6ULL) 驱动开发教程  
> 配套代码：`dtsof.c` — 演示设备树 OF API 的基本使用

---

### 一、什么是设备树 (Device Tree)？

### 1.1 背景：没有设备树之前

在 ARM Linux 早期，硬件的描述信息（如外设地址、中断号、GPIO 引脚等）都是**硬编码在内核源码的"板级文件"**中的（`arch/arm/mach-xxx/`）。每新增一块开发板就要写大量重复代码，导致内核臃肿不堪，Linus Torvalds 对此非常不满。

### 1.2 设备树的引入

设备树借鉴了 PowerPC 架构中 Open Firmware 的做法，将**硬件描述从内核代码中分离**出来。设备树本身是一个独立于内核的规范，源文件是 `.dts`（Device Tree Source），编译后生成 `.dtb`（Device Tree Blob）。

```
.dts (源文件，文本，人可读)
   │  编译工具: dtc (Device Tree Compiler)
   │  命令: dtc -I dts -O dtb -o xxx.dtb xxx.dts
   ▼
.dtb (二进制文件，内核可读)
   │  启动流程: U-Boot → 加载 dtb 到内存 → 启动内核
   ▼
Linux 内核解析设备树，匹配驱动并初始化硬件
```

### 1.3 核心思想

**同一个内核镜像 + 不同的设备树文件 = 适配不同的硬件板卡**

设备树就像一份"硬件清单"，告诉内核：这块板子上有什么芯片、接在哪个总线上、用哪个中断、寄存器地址是什么...

---

### 二、设备树的基本语法结构

### 2.1 树形结构

```dts
/ {
    node1@0 {
        property1 = "string";
        property2 = <123>;
    };

    node2@1 {
        property3 = <&node1>;   /* &引用其他节点（句柄 phandle） */
    };
};
```

| 要素 | 说明 | 示例 |
|------|------|------|
| **根节点** | `/` 表示整棵树 | `/ {}` |
| **节点** | 代表一个硬件设备或总线 | `backlight {}`, `i2c@021a0000 {}` |
| **属性** | 键值对，描述节点特性 | `compatible = "pwm-backlight"` |
| **标签** | 给节点起名，方便引用 | `pwm1: pwm@02088000 {}` |
| **引用** | `&标签` 引用另一个节点 | `pwms = <&pwm1 0 5000000>` |

### 2.2 节点命名规则

```
node-name@unit-address
```

- `node-name`：功能名称，如 `backlight`、`i2c`
- `@unit-address`：寄存器基地址（可选），如 `i2c@021a0000`

### 2.3 标准属性详解

#### (1) `compatible` —— **最重要的属性**

```dts
compatible = "manufacturer,model";
```

驱动和设备的匹配就是靠这个属性。内核驱动中声明自己支持的 `compatible` 列表，设备树中设置设备的 `compatible`，两者匹配成功则驱动被加载。

#### (2) `status` —— 设备状态

| 值 | 含义 |
|----|------|
| `"okay"` | 设备可用 |
| `"disabled"` | 设备不可用（硬件存在但不使用） |
| `"fail"` | 设备故障 |
| `"fail-sss"` | 设备故障且带具体错误码 |

#### (3) `reg` —— 寄存器地址范围

```dts
reg = <0x02088000 0x4000>;  /* 起始地址 0x02088000, 长度 0x4000 */
```

通常配合 `#address-cells` 和 `#size-cells` 使用，分别指定地址和长度各占几个 u32。

#### (4) `#address-cells` / `#size-cells`

```dts
#address-cells = <1>;  /* 子节点的 reg 中，地址占 1 个 u32 */
#size-cells    = <1>;  /* 子节点的 reg 中，长度占 1 个 u32 */
```

---

### 三、OF (Open Firmware) API 函数详解

> **这是本课程的核心内容。** 在驱动代码中，所有以 `of_` 开头的函数都来自 `linux/of.h` 头文件，用于在驱动中解析设备树节点的属性。

### 3.1 函数分类

| 类别 | 函数 | 用途 |
|------|------|------|
| **查找节点** | `of_find_node_by_path()` | 按设备树路径查找节点 |
| | `of_find_node_by_name()` | 按节点名称查找 |
| | `of_find_node_by_type()` | 按设备类型查找 |
| | `of_find_compatible_node()` | 按 compatible 属性查找 |
| | `of_get_parent()` | 获取父节点 |
| | `of_get_next_child()` | 遍历子节点 |
| **提取属性值** | `of_find_property()` | 查找属性（返回原始数据结构） |
| | `of_property_read_string()` | 读取字符串属性 |
| | `of_property_read_u32()` | 读取单个 u32 值 |
| | `of_property_read_u32_array()` | 读取 u32 数组 |
| | `of_property_read_u64()` | 读取 u64 值 |
| | `of_property_read_variable_u8_array()` | 读取可变长度 u8 数组 |
| | `of_property_count_elems_of_size()` | 获取数组元素个数 |
| **地址/中断** | `of_address_to_resource()` | 将 reg 属性转换为 resource |
| | `of_iomap()` | 从 reg 属性获取地址并做内存映射 |
| | `of_irq_get()` | 获取中断号 |
| **GPIO** | `of_get_named_gpio()` | 从设备树获取 GPIO 编号 |

### 3.2 核心函数详解

#### `of_find_node_by_path()`

```c
struct device_node *of_find_node_by_path(const char *path);
```

- **作用**：按设备树中的**绝对路径**查找节点
- **参数**：如 `"/backlight"` 表示根节点下的 backlight 子节点
- **返回**：成功返回 `device_node` 指针，失败返回 `NULL`
- **重点**：路径必须是从根节点 `/` 开始的完整路径

#### `of_find_property()`

```c
struct property *of_find_property(const struct device_node *np,
                                  const char *name, int *lenp);
```

- **作用**：查找指定名称的属性，返回完整的 property 结构体
- **重点**：`property->value` 是属性值（void*），需要**强转为对应类型**
- `lenp` 可传入 `NULL` 表示不关心长度

#### `of_property_read_string()`

```c
int of_property_read_string(const struct device_node *np,
                            const char *propname, const char **out_string);
```

- **作用**：读取字符串类型的属性值，**更安全、更方便**
- **重点**：不需要自己转换类型，直接返回 `const char *` 指针

#### `of_property_read_u32()`

```c
int of_property_read_u32(const struct device_node *np,
                         const char *propname, u32 *out_value);
```

- **作用**：读取一个 u32 整数属性值

#### `of_property_count_elems_of_size()`

```c
int of_property_count_elems_of_size(const struct device_node *np,
                                    const char *propname, int elem_size);
```

- **作用**：获取数组中元素的数量（不读取数据，只获取长度）
- **参数**：`elem_size` 为每个元素的大小，如 `sizeof(u32)`

#### `of_property_read_u32_array()`

```c
int of_property_read_u32_array(const struct device_node *np,
                               const char *propname,
                               u32 *out_values, size_t sz);
```

- **作用**：读取 u32 类型的数组属性
- **重点**：需要先通过 `of_property_count_elems_of_size()` 获取长度，再 `kmalloc` 分配内存，最后读取

### 3.3 通用返回值约定

所有 `of_property_read_*` 系列函数：

- **返回值**：成功返回 `0`，失败返回负的错误码（`-EINVAL` 等）
- **返回值 < 0** 即表示失败，这是惯用写法

---

### 四、结合 dtsof.c 的完整分析

### 4.1 分析的目标设备树节点

```dts
backlight {
    compatible = "pwm-backlight";
    pwms = <&pwm1 0 5000000>;
    brightness-levels = <0 4 8 16 32 64 128 255>;
    default-brightness-level = <6>;
    status = "okay";
};
```

这是一个 **PWM 背光控制设备**的节点。

| 属性 | 说明 |
|------|------|
| `compatible` | `"pwm-backlight"` — 驱动匹配标识 |
| `pwms` | PWM 配置：使用 pwm1、通道 0、周期 5ms |
| `brightness-levels` | 8 级亮度阶梯：0~255 |
| `default-brightness-level` | 默认亮度为第 6 级（= 128） |
| `status` | 设备可用 |

### 4.2 代码逻辑流程图

```
dtsof_init() 入口
    │
    ├─ 步骤1: of_find_node_by_path("/backlight")
    │   找到设备树中的 backlight 节点
    │   └─ 失败 → fail_findnd → 返回 -EINVAL
    │
    ├─ 步骤2: of_find_property(bl_nd, "compatible", NULL)
    │   查找 compatible 属性
    │   └─ 成功 → printk 打印 "compatible=pwm-backlight"
    │   └─ 失败 → fail_finpro
    │
    ├─ 步骤3: of_property_read_string(bl_nd, "status", &str)
    │   读取 status 字符串属性
    │   └─ 成功 → printk 打印 "status=okay"
    │   └─ 失败 → fail_rs
    │
    ├─ 步骤4: of_property_read_u32(bl_nd, "default-brightness-level", &def_value)
    │   读取单个 u32 数字
    │   └─ 成功 → printk 打印 "default-brightness-level=6"
    │   └─ 失败 → fail_read32
    │
    ├─ 步骤5: of_property_count_elems_of_size(bl_nd, "brightness-levels", sizeof(u32))
    │   获取数组元素个数 → elemsize = 8
    │   └─ 失败 → fail_readele
    │
    ├─ 步骤6: kmalloc(elemsize * sizeof(u32), GFP_KERNEL)
    │   动态申请内存存放数组
    │   └─ 失败 → faile_mem
    │
    ├─ 步骤7: of_property_read_u32_array(bl_nd, "brightness-levels", brival, elemsize)
    │   读取整个亮度数组：<0 4 8 16 32 64 128 255>
    │   └─ 成功 → for 循环逐项打印
    │   └─ 失败 → fail_read32array → kfree 释放内存
    │
    ├─ 步骤8: kfree(brival)  释放申请的内存
    │
    └─ return 0    模块加载成功
```

### 4.3 错误处理机制分析

代码使用了 **goto 链式错误处理**，这是 Linux 内核中非常经典的模式：

```
                            正常路径
        ┌───────────────────────────────► return 0
        │
fail_findnd ──► fail_finpro ──► fail_rs ──► fail_read32 ──► fail_readele ──► faile_mem
                                                                                  │
                    ┌─────────────────────────────────────────────────────────────┘
                    │  fail_read32array
                    │      │
                    │      ├─ kfree(brival)  ← 只有这里需要释放内存
                    │      │
                    ▼      ▼
                return ret  ← 统一返回错误码
```

**关键设计思想：**
- 越晚失败，越靠近底部的标签
- 只有分配了内存的那一步（kmalloc 之后）失败时才需要 `kfree`
- 早期步骤失败直接跳到最后 `return ret`，无需清理资源

---

### 五、必须掌握的核心知识点总结

### 5.1 概念层面

| 序号 | 知识点 | 重要程度 |
|------|--------|----------|
| 1 | 设备树的作用：分离硬件描述和内核代码 | ★★★★★ |
| 2 | .dts → .dtb → 内核解析 的完整流程 | ★★★★★ |
| 3 | compatible 属性的匹配机制 | ★★★★★ |
| 4 | 节点、属性、标签、引用的概念 | ★★★★ |
| 5 | status 属性控制设备的启用/禁用 | ★★★ |
| 6 | 设备树中 #address-cells 和 #size-cells 的含义 | ★★★★ |
| 7 | reg 属性与内存映射的关系 | ★★★★ |
| 8 | dtc 编译工具的基本使用 | ★★★ |

### 5.2 API 函数层面

| 序号 | 函数 | 使用频率 | 说明 |
|------|------|----------|------|
| 1 | `of_find_node_by_path()` | ★★★★★ | 最常用的节点查找方式 |
| 2 | `of_property_read_string()` | ★★★★★ | 读字符串属性 |
| 3 | `of_property_read_u32()` | ★★★★★ | 读单个整数 |
| 4 | `of_property_read_u32_array()` | ★★★★ | 读整数数组 |
| 5 | `of_property_count_elems_of_size()` | ★★★★ | 配合数组读取使用 |
| 6 | `of_find_property()` | ★★★ | 底层 API，直接返回 property 结构 |
| 7 | `of_find_compatible_node()` | ★★★ | 按 compatible 查找 |
| 8 | `of_iomap()` | ★★★★★ | 实际驱动开发中极其常用 |
| 9 | `of_get_named_gpio()` | ★★★★★ | GPIO 子系统的设备树接口 |
| 10 | `of_irq_get()` | ★★★★ | 中断号的设备树接口 |

### 5.3 编程模式层面

| 序号 | 知识点 |
|------|--------|
| 1 | goto 链式错误处理的标准写法 |
| 2 | 内存申请与释放的对称性：kmalloc ↔ kfree |
| 3 | 返回值约定：成功返回 0，失败返回负值 |
| 4 | printk 的使用（驱动中无法使用 printf） |
| 5 | `module_init()` / `module_exit()` 注册入口出口 |
| 6 | `MODULE_LICENSE("GPL")` 等模块声明宏 |

---

### 六、延伸：实际驱动开发中的典型模式

`dtsof.c` 演示的是 OF API 的基本使用，但在**真正的驱动开发**中，更常见的是以下模式：

### 6.1 典型的 platform 驱动 + 设备树匹配

```c
/* 1. 定义 compatible 匹配表 */
static const struct of_device_id xxx_of_match[] = {
    { .compatible = "alientek,xxx" },
    { /* sentinel */ }
};
MODULE_DEVICE_TABLE(of, xxx_of_match);

/* 2. 在 probe 函数中解析设备树 */
static int xxx_probe(struct platform_device *pdev)
{
    struct device_node *nd = pdev->dev.of_node;

    /* 获取 GPIO */
    int gpio = of_get_named_gpio(nd, "enable-gpios", 0);

    /* 获取中断号 */
    int irq = of_irq_get(nd, 0);

    /* 内存映射 */
    void __iomem *base = of_iomap(nd, 0);

    /* ... */
}

/* 3. 注册 platform 驱动 */
static struct platform_driver xxx_driver = {
    .probe  = xxx_probe,
    .remove = xxx_remove,
    .driver = {
        .name           = "xxx",
        .of_match_table = xxx_of_match,
    },
};
module_platform_driver(xxx_driver);
```

### 6.2 dtsof.c  vs  真实驱动

| 对比维度 | dtsof.c (本代码) | 真实驱动 |
|----------|-------------------|----------|
| 调用时机 | 模块加载 `init` 时 | 驱动 `probe` 函数中 |
| 节点来源 | 硬编码路径 `"/backlight"` | `pdev->dev.of_node` 自动传入 |
| 用途 | 学习 OF API | 实际初始化硬件、注册字符设备等 |
| 资源管理 | 简单的 kfree | devm_ 系列托管函数 |

---

### 七、常见问题 FAQ

### Q1: `of_find_node_by_path()` 和 `of_find_compatible_node()` 有什么区别？

- `of_find_node_by_path`：按设备树中的**路径**查找，如 `"/backlight"`
- `of_find_compatible_node`：按 **compatible 属性值**查找，如 `of_find_compatible_node(NULL, NULL, "pwm-backlight")`

### Q2: `of_property_read_string()` 和 `of_find_property()` 的区别？

- `of_find_property` 返回原始 `struct property*`，需要自己从 `property->value` 解析
- `of_property_read_string` 是封装好的辅助函数，直接返回 `const char *`，更方便安全

### Q3: 为什么要先用 `of_property_count_elems_of_size()` 再分配内存？

因为设备树中的数组长度不固定，必须先获取元素个数，再根据个数动态分配内存，最后读取数据。这是标准的 **"先问大小，再要数据"** 模式。

### Q4: 设备树中 `<>` 和 `""` 的区别？

- `<>` 括起来的是**数字**（u32），如 `<0 4 8 16>`
- `""` 括起来的是**字符串**，如 `"okay"`, `"pwm-backlight"`
- 字符串数组也可以写成 `"string1","string2"`

---

### 八、学习建议

1. **先理解设备树语法**，能看懂 `.dts` 文件中的节点和属性
2. **掌握 5 个核心 OF 函数**：`of_find_node_by_path`、`of_property_read_string`、`of_property_read_u32`、`of_property_read_u32_array`、`of_iomap`
3. **理解 dtsof.c 的代码流程**，这是后续所有驱动 OF 解析的基础
4. **动手写**：尝试在设备树中添加一个新节点，然后在驱动中读取它的属性
5. **进阶**：学习 `platform_driver` 框架中如何结合设备树，这是实际驱动开发的标配

---

> 📖 参考资料：Linux 内核源码 `Documentation/devicetree/` 目录  
> 💻 配套代码：`dtsof.c` — 正点原子 I.MX6ULL 阿尔法开发板 驱动教程

---

## 第五章 设备树 LED 驱动

> 基于正点原子阿尔法Linux开发板（IMX6ULL），结合 `dtsled.c` / `ledAPP.c` / `Makefile` 代码实例分析。

---

## 目录

1. [设备树（Device Tree）基础概念](#1-设备树device-tree基础概念)
   - [什么是设备树](#什么是设备树)
   - [设备树的树形结构](#设备树的树形结构)
   - [设备树关键语法](#设备树关键语法)
   - [★ 设备节点、设备号、设备树节点——三者的区别与联系](#设备节点设备号设备树节点三者的区别与联系)
2. [为什么需要设备树](#2-为什么需要设备树)
3. [设备树在 Linux 驱动中的角色与工作流程](#3-设备树在-linux-驱动中的角色与工作流程)
4. [驱动中使用的设备树核心 API](#4-驱动中使用的设备树核心-api)
5. [dtsled.c 驱动源码完整流程分析](#5-dtsledc-驱动源码完整流程分析)
6. [ledAPP.c 应用程序分析](#6-ledappc-应用程序分析)
7. [Makefile 分析](#7-makefile-分析)
8. [传统驱动 vs 设备树驱动对比](#8-传统驱动-vs-设备树驱动对比)
9. [关键知识点总结与面试要点](#9-关键知识点总结与面试要点)
10. [实验操作步骤](#10-实验操作步骤)

---

### 1. 设备树（Device Tree）基础概念

### 什么是设备树？

设备树（Device Tree，简称 DT）是一种**描述硬件信息的数据结构**，它以一种树形结构把硬件资源（寄存器地址、中断号、引脚配置等）从内核源码中分离出来，存放在独立的 `.dts`/`.dtsi` 文件中。

**设备树是存放操作系统"配置信息"的文件，存在开发板的外部存储器（SD卡/eMMC）中**，和内核镜像、根文件系统放在一起，不在 IMX6ULL 芯片内部，更不在 LED 灯里。

```
设备树源文件:
  .dts   → 板级设备树源文件（如 imx6ull-alientek-emmc.dts）
  .dtsi  → SoC 级设备树包含文件（如 imx6ull.dtsi）
      ↓  编译（dtc 编译器）
  .dtb   → 设备树二进制文件（bootloader 加载到内存传给内核）
```

### 设备树的树形结构

```
/ (根节点)
├── aliases
├── cpus
├── soc
│   ├── aips1 (外设总线1)
│   │   ├── gpio1: gpio@0209C000
│   │   ├── gpio2: gpio@020A0000
│   │   ├── uart1: serial@02020000
│   │   └── ...
│   ├── aips2
│   └── aips3
├── memory
├── chosen
└── alphaled {           ← 自定义设备节点（本实验重点）
    compatible = "alientek,alphaled";
    status = "okay";
    reg = <0x020C406C 0x04    // CCM_CCGR1
           0x020E0068 0x04    // SW_MUX_GPIO1_IO03
           0x020E02F4 0x04    // SW_PAD_GPIO1_IO03
           0x0209C000 0x04    // GPIO1_DR
           0x0209C004 0x04>;  // GPIO1_GDIR
}
```

### 设备树关键语法

| 语法元素 | 说明 | 示例 |
|----------|------|------|
| `/dts-v1/;` | 设备树版本声明 | 文件开头必须 |
| `/ { ... };` | 根节点 | 所有节点的祖先 |
| `node_name@address` | 节点名称+地址 | `gpio1: gpio@0209C000` |
| `compatible` | 兼容性字符串（驱动匹配关键） | `"alientek,alphaled"` |
| `status` | 设备状态 | `"okay"`, `"disabled"`, `"fail"` |
| `reg` | 寄存器地址+长度（CPU地址空间） | `<0x020C406C 0x04>` |
| `#address-cells` | reg 中地址占用几个 u32 | 通常为 1 |
| `#size-cells` | reg 中长度占用几个 u32 | 通常为 1 |
| `label:` | 节点标签（方便引用） | `&gpio1` |

### ★ 设备节点、设备号、设备树节点——三者的区别与联系

> ⚠️ **最容易混淆的三个概念**：名字都带"节点"或"设备"，但完全不是一回事。用你敲下 `./ledAPP /dev/dtsled 1` 的一次完整操作来理解。

#### 一张图，三个角色各就各位

```
./ledAPP /dev/dtsled 1
        │
        │  ① 打开设备节点 "/dev/dtsled"
        ▼
┌──────────────────┐
│   /dev 设备节点    │   /dev/dtsled  (文件系统里的文件)
│   作用: 用户找驱动  │   用户 open() 它，就像打开普通文件
│   里面存的是: 设备号 │   内核读取它的 inode，取出设备号 (244,0)
└──────┬───────────┘
       │  设备号 (244, 0)
       ▼
┌──────────────────┐
│   设备号 dev_t     │   MKDEV(244, 0)
│   作用: 匹配驱动    │   主设备号→找到 cdev
│   是一个 32位数字   │   次设备号→驱动内区分具体设备
└──────┬───────────┘
       │  找到 cdev → dtsled_fops
       ▼
         dtsled_open()  →  dtsled_write()
                                │
       ┌────────────────────────┘
       ▼
┌──────────────────┐
│   设备树节点 nd    │   /alphaled  (.dtb解析而来，存在内存里)
│   作用: 描述硬件    │   reg = <0x0209C000 0x04 ...>
│   里面存的是:       │   of_iomap(nd, 3) → 虚拟地址
│   寄存器物理地址     │
└──────┬───────────┘
       │  返回虚拟地址
       ▼
┌──────────────────┐
│  GPIO1_DR 寄存器   │  芯片上真实的硬件电路
│  (物理 0x0209C000) │  readl/writel → 💡亮!
└──────────────────┘
```

#### 联系：整条链上各司其职

| | /dev 设备节点 | 设备号 | 设备树节点 |
|------|-------------|--------|-----------|
| **阶段** | open 时，用户打开这个文件 | open 时，内核根据号找驱动 | insmod 时，驱动读取硬件信息 |
| **谁用** | **用户程序**用 | **内核**用 | **驱动**用 |
| **实质** | `/dev/` 下的一个文件 | 一个数字 `(244, 0)` | 内存中的结构体，存了 `reg` 数组 |
| **创建方式** | `device_create()` | `alloc_chrdev_region()` | `of_find_node_by_path()` |
| **存在位置** | 文件系统 `/dev/dtsled` | 内核设备号全局表 | 内核内存（dtb 解析而来） |

#### 类比：打电话

```
设备节点 /dev/dtsled    =  通讯录里的名字 "张三"
设备号 (244, 0)         =  张三的电话号码 13800138000
字符设备 cdev + fops    =  张三本人（接电话，干活）
设备树节点 /alphaled    =  张三手里的操作手册（"开关在左边第三个"）
寄存器 GPIO1_DR         =  实际的那个开关

你拨 "张三" → 查通讯录得 13800138000 → 拨号 → 张三接电话
→ 张三翻操作手册 → 走到左边 → 按下第三个开关 → 💡亮
```

#### 在你的代码中对应的位置

```c
// ===== insmod 时: 设备树节点 =====
// dtsled_init() 中
dtsled.nd = of_find_node_by_path("/alphaled");   // ← 获取设备树节点
GPIO1_DR  = of_iomap(dtsled.nd, 3);              // ← 从节点读取硬件地址

// ===== insmod 时: 设备号 =====
// dtsled_init() 中
alloc_chrdev_region(&dtsled.devid, 0, DTSLED_CNT, DTSLED_NAME);  // ← 分配设备号
dtsled.major = MAJOR(dtsled.devid);   // 拿到主设备号

// ===== insmod 时: 设备节点 =====
// dtsled_init() 中
dtsled.class  = class_create(DTSLED_NAME);                            // 建类
dtsled.device = device_create(dtsled.class, NULL, dtsled.devid, ...); // 创建 /dev/dtsled
//                                       ↑ 绑定了设备号

// ===== 用户 open 时: 链条启动 =====
// ./ledAPP 调用 open("/dev/dtsled")        ← 用户操作设备节点
//   → 内核从 /dev/dtsled 读出设备号 (244,0)  ← 设备号匹配
//   → 找到 dtsled.cdev → dtsled_open()      ← 进入驱动
//   → write 时 GPIO1_DR 的地址来自            ← 设备树节点给的
```

#### 关键理解

- **设备树节点** = 给**驱动**看的硬件说明书："GPIO1_DR 在物理地址 0x0209C000"
- **设备号** = 给**内核**看的身份证号："主设备号 244 对应的驱动是 dtsled"
- **/dev 设备节点** = 给**用户**看的门把手："你要操作 LED，打开 /dev/dtsled"

**名字都叫"节点"，但一个对内（驱动↔硬件）、一个对中（内核匹配）、一个对外（用户↔驱动），各管各的，三个串起来才跑通整个流程。**

---

### 2. 为什么需要设备树？

### 背景 —— 驱动硬编码问题

在设备树引入之前（比如本教程第 3 章 `3_newchrled`），驱动中充斥着"硬编码"的寄存器地址：

```c
/* 旧方式：寄存器地址硬编码在驱动中（3_newchrled 的做法） */
#define CCM_CCGR1_BASE          (0x020C406C)
#define SW_MUX_GPIO1_IO03_BASE  (0x020E0068)
// ...
IMX6U_CCM_CCGR1 = ioremap(CCM_CCGR1_BASE, 4);
```

**问题**：
- 每个板子需要各自的驱动，即使操作相同的外设
- 驱动代码量随板子数量爆炸式增长（ARM 生态的特点）
- 违反了"驱动=逻辑，硬件=数据"的设计原则

### 设备树解决了什么

| 痛点 | 设备树的解决方案 |
|------|-----------------|
| 硬件信息硬编码在驱动中 | 硬件信息从代码分离，放入 .dts 文件 |
| 一个板子一个驱动 | **一个驱动 + 多个设备树 = 多板支持** |
| 驱动不可移植 | 驱动只关注逻辑，硬件描述交给设备树 |
| 板级配置难以管理 | 设备树源文件清晰、可读、版本可管理 |

### 设备树的核心哲学

> **"驱动代码 = 逻辑，设备树 = 数据"**  
> 操作系统通过读取设备树来"认识"硬件，类似于 BIOS 告诉 Windows 你插了什么硬件。

---

### 3. 设备树在 Linux 驱动中的角色与工作流程

### 整体数据流

```
┌─────────────────────────────────────────────────────────────────┐
│                       开发阶段                                    │
│                                                                  │
│  硬件原理图 ──→ 编写 .dts 文件 ──→ dtc 编译 → .dtb 文件          │
│                     ↑                                            │
│              描述寄存器、中断、引脚                               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                       运行阶段                                    │
│                                                                  │
│  U-Boot 加载 .dtb ──→ 传给内核 ──→ 内核解析为 device_node 树    │
│                                          │                       │
│                                          ↓                       │
│                             驱动通过 of_xxx() API 读取           │
│                                          │                       │
│                                          ↓                       │
│                             得到寄存器地址 → ioremap → 操作硬件   │
└─────────────────────────────────────────────────────────────────┘
```

### 驱动中使用设备树的标准流程（dtsled.c 的实际流程）

```
步骤1: of_find_node_by_path("/alphaled")
        ↓  在设备树中查找名为 "alphaled" 的节点
        ↓  返回 struct device_node *nd
        
步骤2: of_property_read_string(nd, "status", &str)
        of_property_read_string(nd, "compatible", &str)
        ↓  读取节点中的字符串属性（调试/验证用）

步骤3: of_iomap(nd, 0)  → 映射 reg[0]  (CCM_CCGR1)
        of_iomap(nd, 1)  → 映射 reg[1]  (SW_MUX_GPIO1_IO03)
        of_iomap(nd, 2)  → 映射 reg[2]  (SW_PAD_GPIO1_IO03)
        of_iomap(nd, 3)  → 映射 reg[3]  (GPIO1_DR)
        of_iomap(nd, 4)  → 映射 reg[4]  (GPIO1_GDIR)
        ↓  将 reg 属性中的物理地址映射为虚拟地址
        ↓  返回 void __iomem *（可直接 readl/writel）

步骤4: readl/writel 操作硬件寄存器
        ↓  控制 GPIO 时钟、复用、方向、输出值
```

---

### 4. 驱动中使用的设备树核心 API

### 查找设备节点 `of_find_node_by_path()`

```c
struct device_node *of_find_node_by_path(const char *path);
```

| 参数 | 说明 |
|------|------|
| `path` | 设备树中的节点路径，如 `"/alphaled"`（根节点下的 alphaled） |
| **返回值** | 成功返回 `device_node` 指针，失败返回 `NULL` |

**关键理解**：`device_node` 是内核中表示设备树节点的数据结构。每个设备树节点在内存中都对应一个 `device_node`。这个函数**通过绝对路径**查找节点。

### 读取字符串属性 `of_property_read_string()`

```c
int of_property_read_string(const struct device_node *np,
                            const char *propname,
                            const char **out_string);
```

| 参数 | 说明 |
|------|------|
| `np` | 设备节点指针 |
| `propname` | 属性名（如 `"compatible"`, `"status"`） |
| `out_string` | 输出：读取到的字符串 |
| **返回值** | 成功返回 0，失败返回负错误码 |

### 地址映射 `of_iomap()` ⭐ 核心函数

```c
void __iomem *of_iomap(struct device_node *np, int index);
```

| 参数 | 说明 |
|------|------|
| `np` | 设备节点指针 |
| `index` | reg 属性中的第几个地址组（从 0 开始） |
| **返回值** | 成功返回映射后的虚拟地址，失败返回 `NULL` |

**这是设备树驱动最重要的改进！**

**对比**：
```c
/* 旧方式（3_newchrled）：手动指定物理地址 + 手动指定长度 */
IMX6U_CCM_CCGR1 = ioremap(0x020C406C, 4);

/* 新方式（5_dtsled）：只需指定 reg 属性中的索引 */
IMX6U_CCM_CCGR1 = of_iomap(dtsled.nd, 0);  // 自动从 reg 中获取第0组地址
```

```c
/* 对应设备树中的 reg 属性（理解 index 的含义） */
reg = <0x020C406C 0x04    // index=0 → CCM_CCGR1
       0x020E0068 0x04    // index=1 → SW_MUX_GPIO1_IO03
       0x020E02F4 0x04    // index=2 → SW_PAD_GPIO1_IO03
       0x0209C000 0x04    // index=3 → GPIO1_DR
       0x0209C004 0x04>;  // index=4 → GPIO1_GDIR
```

### 读取 u32 数组属性 `of_property_read_u32_array()`

```c
int of_property_read_u32_array(const struct device_node *np,
                                const char *propname,
                                u32 *out_values,
                                size_t sz);
```

在本代码中被 `#if 0 ... #endif` 禁用，展示了如何手动读取 reg 属性值。实际上 `of_iomap()` 内部就是封装了这个操作。

### 设备树 API 速查表

| API 函数 | 功能 | 返回值 |
|----------|------|--------|
| `of_find_node_by_path()` | 通过绝对路径查找节点 | `device_node*` / `NULL` |
| `of_find_node_by_name()` | 通过节点名查找节点 | `device_node*` / `NULL` |
| `of_find_compatible_node()` | 通过 compatible 查找节点 | `device_node*` / `NULL` |
| `of_iomap()` | 映射 reg 属性中的地址 | `void __iomem*` / `NULL` |
| `of_property_read_string()` | 读取字符串属性 | 0 成功 / 负值失败 |
| `of_property_read_u32()` | 读取单个 u32 属性 | 0 成功 / 负值失败 |
| `of_property_read_u32_array()` | 读取 u32 数组属性 | 0 成功 / 负值失败 |
| `of_get_named_gpio()` | 获取 GPIO 编号 | GPIO 编号 / 负值失败 |
| `iounmap()` | 取消地址映射（配对使用） | 无 |

---

### 5. dtsled.c 驱动源码完整流程分析

### 整体架构

```
dtsled.c (驱动模块)
│
├── 头文件引用 (line 1-12)          ← 包含设备树、字符设备、IO映射等
├── 宏定义 (line 14-18)              ← 设备号个数、名字、LED状态
├── 全局变量 (line 22-26)            ← 映射后的虚拟地址指针
├── 设备结构体 (line 29-39)          ← 封装所有设备信息
│
├── led_switch() (line 42-55)        ← ★ 硬件操作层：控制LED亮灭
├── dtsled_open() (line 57-61)       ← file_operations 的 .open
├── dtsled_release() (line 63-68)    ← file_operations 的 .release
├── dtsled_write() (line 70-87)      ← ★ file_operations 的 .write（核心逻辑）
│
├── dtsled_fops (line 90-95)         ← 字符设备操作集
│
├── dtsled_init() (line 98-221)      ← ★★★ 模块入口（核心！）
│   ├── 步骤1: 申请设备号 (line 109-119)
│   ├── 步骤2: 添加字符设备 (line 122-126)
│   ├── 步骤3: 自动创建设备节点 (line 129-139)
│   ├── 步骤4: 查找设备树节点 (line 142-146)
│   ├── 步骤5: 读取设备树属性 (line 149-161)
│   ├── 步骤6: of_iomap 地址映射 (line 184-188) ← 设备树关键！
│   └── 步骤7: 初始化 GPIO 寄存器 (line 191-207)
│
├── dtsled_exit() (line 224-251)     ← ★ 模块出口
│   ├── 关闭LED
│   ├── iounmap 取消映射
│   ├── 删除字符设备
│   ├── 释放设备号
│   └── 销毁设备/类
│
├── module_init/exit (line 254-255)  ← 模块注册宏
└── MODULE_LICENSE/AUTHOR (line 256-257)
```

### 模块入口 dtsled_init() 分步详解

#### 步骤1：申请设备号（line 109-119）

```c
dtsled.major = 0;   // 设置为0，让内核自动分配主设备号

if (dtsled.major) {  // major != 0：用户指定了设备号
    // register_chrdev_region() —— 静态注册
    dtsled.devid = MKDEV(dtsled.major, 0);
    ret = register_chrdev_region(dtsled.devid, DTSLED_CNT, DTSLED_NAME);
} else {             // major == 0：让内核自动分配
    // alloc_chrdev_region() —— 动态分配
    ret = alloc_chrdev_region(&dtsled.devid, 0, DTSLED_CNT, DTSLED_NAME);
    dtsled.major = MAJOR(dtsled.devid);  // 从 devid 中提取主设备号
    dtsled.minor = MINOR(dtsled.devid);  // 从 devid 中提取次设备号
}
```

> **知识点**：`MKDEV(major, minor)` 将主次设备号合成为一个 `dev_t` 类型的设备号；`MAJOR()`/`MINOR()` 则反向提取。

#### 步骤2：添加字符设备（line 122-126）

```c
dtsled.cdev.owner = THIS_MODULE;
cdev_init(&dtsled.cdev, &dtsled_fops);   // 绑定 file_operations
ret = cdev_add(&dtsled.cdev, dtsled.devid, DTSLED_CNT);  // 注册到内核
```

> `cdev_init()` 负责将 `file_operations` 结构体绑定到字符设备上。

#### 步骤3：自动创建设备节点（line 129-139）

```c
/* ★ 注意: Linux 6.x 内核 class_create() 只需一个参数(名称) */
dtsled.class = class_create(DTSLED_NAME);     // 在 /sys/class/ 下创建类
dtsled.device = device_create(dtsled.class, NULL, dtsled.devid, NULL, DTSLED_NAME);
// 自动在 /dev/ 下创建设备节点 → /dev/dtsled
```

> **关键**：这一步是通过 udev/mdev 机制**自动**创建设备文件，不再需要手动 `mknod`！

#### 步骤4+5：设备树操作（line 142-161）

```c
// 查找设备树节点
dtsled.nd = of_find_node_by_path("/alphaled");

// 读取并打印 status 属性
ret = of_property_read_string(dtsled.nd, "status", &str);
printk("status = %s\r\n", str);

// 读取并打印 compatible 属性
ret = of_property_read_string(dtsled.nd, "compatible", &str);
printk("compatible = %s\r\n", str);
```

> **调试技巧**：用 `printk` 打印设备树属性值，可以确认设备树是否正确加载。

#### 步骤6：地址映射 —— 设备树核心！（line 184-188）

```c
// of_iomap 内部自动从 reg 属性中读取地址和长度进行映射
IMX6U_CCM_CCGR1     = of_iomap(dtsled.nd, 0);  // reg第0组
SW_MUX_GPIO1_IO03   = of_iomap(dtsled.nd, 1);  // reg第1组
SW_PAD_GPIO1_IO03   = of_iomap(dtsled.nd, 2);  // reg第2组
GPIO1_DR            = of_iomap(dtsled.nd, 3);  // reg第3组
GPIO1_GDIR          = of_iomap(dtsled.nd, 4);  // reg第4组
```

> **核心理解**：`of_iomap()` = `ioremap()` + 自动从设备树 reg 属性读取地址。每个 `index` 对应 `reg = <addr length, addr length, ...>` 中的一组。此处每个 reg 的大小都是 4 字节（一个 32 位寄存器）。

#### 步骤7：初始化 GPIO 寄存器（line 191-207）

```c
// ① 使能 GPIO1 时钟（CCM_CCGR1 的 bit26,27）
val = readl(IMX6U_CCM_CCGR1);
val &= ~(3 << 26);    // 先清除 bit26,27
val |= (3 << 26);     // 两位置1（GPIO1 时钟开启）
writel(val, IMX6U_CCM_CCGR1);

// ② 设置 GPIO1_IO03 为 GPIO 功能（复用选择）
writel(0x5, SW_MUX_GPIO1_IO03);    // ALT5 = GPIO1_IO03

// ③ 设置电气属性（驱动能力、速度、上下拉等）
writel(0x10B0, SW_PAD_GPIO1_IO03);

// ④ 设置 GPIO1_IO03 为输出方向
val = readl(GPIO1_GDIR);
val |= (1 << 3);      // bit3=1 → 输出模式
writel(val, GPIO1_GDIR);

// ⑤ 默认输出高电平（LED灭）
val = readl(GPIO1_DR);
val |= (1 << 3);      // bit3=1 → 高电平 → LED灭
writel(val, GPIO1_DR);
```

### 写操作 dtsled_write() 分析（line 70-87）

```c
static ssize_t dtsled_write(struct file *filp, const char __user *buf,
                             size_t count, loff_t *ppos)
{
    struct dtsled_dev *dev = (struct dtsled_dev *)filp->private_data;
    int retvalue;
    unsigned char databuf[1];

    // ① 从用户空间拷贝数据（内核空间不能直接访问用户空间指针）
    retvalue = copy_from_user(databuf, buf, count);
    if (retvalue < 0) {
        return -EFAULT;   // 拷贝失败
    }

    // ② 根据用户传入的值控制LED
    led_switch(databuf[0]);  // 0=关灯, 1=开灯

    return 0;
}
```

> **关键知识点 `copy_from_user()`**：Linux 内核和用户空间有地址隔离，内核不能直接解引用用户空间指针（安全风险+可能缺页），必须通过 `copy_from_user()`/`copy_to_user()` 完成数据传递。

### GPIO 硬件操作 led_switch() 分析（line 42-55）

```c
static void led_switch(u8 sta)
{
    u32 val = 0;

    if (sta == LEDON) {
        val = readl(GPIO1_DR);
        val &= ~(1 << 3);    // bit3 = 0 → 低电平 → LED点亮
        writel(val, GPIO1_DR);
    } else if (sta == LEDOFF) {
        val = readl(GPIO1_DR);
        val |= (1 << 3);     // bit3 = 1 → 高电平 → LED熄灭
        writel(val, GPIO1_DR);
    }
}
```

> **硬件原理**（IMX6ULL ALPHA 开发板）：GPIO1_IO03 连接 LED0，**低电平点亮，高电平熄灭**。

### 模块出口 dtsled_exit() 分析（line 224-251）

卸载顺序**与初始化相反**（后进先出原则）：

```
初始化: 申请设备号 → 添加cdev → 创建设备 → of_iomap → 初始化GPIO
卸载:   关闭LED → iounmap → 删除cdev → 释放设备号 → 销毁设备
```

```c
// ① 关闭LED（安全退出）
val = readl(GPIO1_DR);
val |= (1 << 3);           // 熄灭LED
writel(val, GPIO1_DR);

// ② 取消所有地址映射（与 of_iomap 配对，必须一一对应！）
iounmap(IMX6U_CCM_CCGR1);
iounmap(SW_MUX_GPIO1_IO03);
iounmap(SW_PAD_GPIO1_IO03);
iounmap(GPIO1_DR);
iounmap(GPIO1_GDIR);

// ③ 删除字符设备
cdev_del(&dtsled.cdev);

// ④ 释放设备号
unregister_chrdev_region(dtsled.devid, DTSLED_CNT);

// ⑤ 销毁设备节点和类
device_destroy(dtsled.class, dtsled.devid);
class_destroy(dtsled.class);
```

> **关键**：`iounmap` 必须与 `of_iomap`/`ioremap` 一一配对，否则会导致内存泄漏。

### 错误处理 —— goto 链式回退

代码使用经典的 Linux 内核 `goto` 错误处理模式：

```c
    if (ret < 0) goto fail_devid;    // 设备号注册失败
    // ...
    if (ret < 0) goto fail_cdev;      // cdev_add 失败 → 回退设备号
    // ...
    if (IS_ERR(...)) goto fail_class; // class_create 失败 → 回退cdev
    // ...
    if (IS_ERR(...)) goto fail_device;// device_create 失败 → 回退class
    // ...
    if (...) goto fail_findnd;        // 找不到节点/属性 → 回退device

fail_rs:
fail_findnd:
    device_destroy(dtsled.class, dtsled.devid);
fail_device:
    class_destroy(dtsled.class);
fail_class:
    cdev_del(&dtsled.cdev);
fail_cdev:
    unregister_chrdev_region(dtsled.devid, DTSLED_CNT);
fail_devid:
    return ret;
```

> **模式优点**：无论在任何步骤失败，都能保证已申请的资源被正确释放，这是内核驱动编程的标准做法。

---

### 6. ledAPP.c 应用程序分析

### 代码逻辑

```c
// 用法: ./ledAPP /dev/dtsled 0|1
int main(int argc, char *argv[])
{
    int fd, retvalue;
    char *filename;
    unsigned char databuf[1];

    // ① 参数检查（需要3个参数）
    if (argc != 3) {
        printf("Error Usage!\r\n");
        return -1;
    }

    // ② 打开设备文件
    filename = argv[1];
    fd = open(filename, O_RDWR);        // 可读可写方式打开
    if (fd < 0) {
        printf("file %s open failed!\r\n", filename);
        return -1;
    }

    // ③ 准备数据并写入
    databuf[0] = atoi(argv[2]);          // "0"→0, "1"→1
    retvalue = write(fd, databuf, sizeof(databuf));
    if (retvalue < 0) {
        printf("LED Control Failed!\r\n");
        close(fd);
        return -1;
    }

    // ④ 关闭设备
    close(fd);
    return 0;
}
```

### 用户空间→内核空间完整调用链

```
用户空间                       内核空间
──────────                    ──────────
./ledAPP /dev/dtsled 1
    │
    ├─ open("/dev/dtsled")  ──→  dtsled_open()
    │                            └─ filp->private_data = &dtsled
    │
    ├─ write(fd, [1], 1)    ──→  dtsled_write()
    │                            ├─ copy_from_user(databuf, buf, count)
    │                            │   └─ databuf[0] = 1
    │                            └─ led_switch(LEDON)
    │                                └─ GPIO1_DR bit3 = 0 → LED亮
    │
    └─ close(fd)            ──→  dtsled_release()
```

---

### 7. Makefile 分析

```makefile
# 内核源码目录（根据实际环境修改）
# 原开发板路径: /home/zzk/linux/IMX6ULL/linux/linux-imx-rel_imx_4.1.15_2.1.0_ga_alientek
# 当前 WSL 环境: 使用 WSL2 内核源码编译验证
KERNELDIR := $(HOME)/wsl2-kernel
# 也可用系统内核头文件: KERNELDIR := /lib/modules/$(shell uname -r)/build

# 当前路径
CURRENT_PATH := $(shell pwd)

# 编译目标：dtsled.o → dtsled.ko
obj-m := dtsled.o

# make 命令 → 进入内核目录执行模块编译
build: kernel_modules

kernel_modules:
    $(MAKE) -C $(KERNELDIR) M=$(CURRENT_PATH) modules
    #   ↑              ↑              ↑
    # make 命令  -C:切换目录  M:模块源码目录

clean:
    $(MAKE) -C $(KERNELDIR) M=$(CURRENT_PATH) clean
```

> **关键理解**：驱动模块**必须在内核源码树的环境下编译**。`-C $(KERNELDIR)` 切换到内核目录使用内核顶层 Makefile，`M=$(CURRENT_PATH)` 告诉内核构建系统模块源码在哪个目录。

---

### 8. 传统驱动 vs 设备树驱动对比

| 对比维度 | 传统方式（3_newchrled） | 设备树方式（5_dtsled） |
|----------|------------------------|------------------------|
| **寄存器地址** | `#define` 宏硬编码 | 设备树 `reg` 属性描述 |
| **地址映射** | `ioremap(phy_addr, size)` | `of_iomap(nd, index)` |
| **硬件信息位置** | 驱动 .c 文件中 | 设备树 .dts 文件中 |
| **板级移植** | 修改驱动代码 | **只修改设备树** |
| **驱动通用性** | 一个板子一个驱动 | **一个驱动适配多板** |
| **设备匹配** | 无（编译时绑定） | 可通过 `compatible` 动态匹配 |
| **代码维护** | 改动硬件需改驱动 | 改动硬件只改设备树 |

### 代码级对比

```c
/* ───────── 传统方式（3_newchrled）───────── */
#define CCM_CCGR1_BASE          (0x020C406C)  // 硬编码！
#define SW_MUX_GPIO1_IO03_BASE  (0x020E0068)
// ...
IMX6U_CCM_CCGR1 = ioremap(CCM_CCGR1_BASE, 4);

/* ───────── 设备树方式（5_dtsled）───────── */
// 驱动中：无硬编码地址！
dtsled.nd = of_find_node_by_path("/alphaled");  // 从设备树找节点
IMX6U_CCM_CCGR1 = of_iomap(dtsled.nd, 0);       // 从设备树读地址映射

// 设备树 .dts 中：
// alphaled {
//     reg = <0x020C406C 0x04 ...>;
// };
```

---

### 9. 关键知识点总结与面试要点

### 必须掌握的 10 个核心知识点

| # | 知识点 | 掌握程度 |
|---|--------|---------|
| 1 | 设备树的作用：分离硬件描述和驱动代码 | ⭐⭐⭐⭐⭐ |
| 2 | `of_find_node_by_path()` 查找设备节点 | ⭐⭐⭐⭐⭐ |
| 3 | `of_iomap()` 地址映射（理解 index 与 reg 的关系） | ⭐⭐⭐⭐⭐ |
| 4 | 字符设备注册流程：`alloc_chrdev_region → cdev_init → cdev_add` | ⭐⭐⭐⭐⭐ |
| 5 | 自动创建设备节点：`class_create → device_create` | ⭐⭐⭐⭐⭐ |
| 6 | `copy_from_user()` 用户/内核空间数据传递 | ⭐⭐⭐⭐ |
| 7 | `readl()`/`writel()` 寄存器读写操作 | ⭐⭐⭐⭐ |
| 8 | 内核 goto 错误处理链 | ⭐⭐⭐⭐ |
| 9 | `struct file_operations` 与系统调用的对应关系 | ⭐⭐⭐⭐ |
| 10 | 模块退出时的资源释放顺序（与初始化相反） | ⭐⭐⭐⭐ |

### 常见面试追问

**Q1：`of_iomap()` 和 `ioremap()` 有什么区别？**
> `ioremap()` 需要手动传入物理地址和长度；`of_iomap()` 自动从设备树的 `reg` 属性中读取地址和长度，通过 `index` 参数指定第几组地址。

**Q2：`copy_from_user()` 为什么不直接用 `memcpy()`？**
> 1) 安全性：`copy_from_user()` 会检查用户空间指针的合法性，防止内核越界访问。
> 2) 缺页处理：用户空间内存可能被换出，`copy_from_user()` 能正确处理缺页异常。

**Q3：为什么模块初始化用 `goto` 链式回退而不是每个步骤单独判断？**
> 内核代码追求简洁高效。`goto` 链式回退确保在任何步骤失败时，已申请的资源全部被正确释放，避免内存泄漏。这是 Linux 内核的惯用模式。

**Q4：设备树的 `compatible` 属性有什么用？**
> `compatible` 是设备与驱动的"匹配关键字"。当总线枚举设备时，内核根据 `compatible` 字符串找到对应的驱动。在 OF 风格的 platform 驱动中（下一章会学到），`compatible` 是驱动匹配的核心。

### 数据流向图（从用户到硬件的完整路径）

```
┌──────────────────────────────────────────────────────────┐
│ ./ledAPP /dev/dtsled 1                                   │
│     │                                                    │
│     │ write(fd, "1", 1)       用户空间                    │
│     │                                                    │
│ ────┼─ 系统调用边界 ──────────────────────────────────    │
│     │                                                    │
│     ▼ dtsled_write()          内核空间                    │
│     │                                                    │
│     ├─ copy_from_user()       从用户空间获取数据          │
│     │                                                    │
│     ├─ led_switch(LEDON)      判断开关逻辑                │
│     │   │                                                │
│     │   ├─ readl(GPIO1_DR)    读取当前 GPIO 状态          │
│     │   ├─ val &= ~(1<<3)     bit3 清零（低电平）         │
│     │   └─ writel(val, GPIO1_DR)  写入 GPIO 寄存器        │
│     │                                                    │
│ ────┼─ 硬件总线 ─────────────────────────────────────    │
│     │                                                    │
│     ▼ GPIO1_DR 寄存器 (@0x0209C000)    硬件层             │
│       GPIO1_IO03 引脚输出低电平 → LED灯点亮               │
└──────────────────────────────────────────────────────────┘
```

---

### 10. 实验操作步骤

### 编译驱动模块

```bash
# 在驱动源码目录下
make
# 生成 dtsled.ko
```

### 复制到开发板并加载

```bash
# 将 dtsled.ko 和 ledAPP 复制到开发板根文件系统
# 然后：

# 加载驱动模块
insmod dtsled.ko

# 查看是否加载成功（查看内核日志）
dmesg | tail
# 应该看到: status = okay
#          compatible = alientek,alphaled

# 查看自动创建的设备节点
ls /dev/dtsled

# 查看主设备号
cat /proc/devices | grep dtsled
```

### 测试 LED 控制

```bash
./ledAPP /dev/dtsled 1   # 打开 LED
./ledAPP /dev/dtsled 0   # 关闭 LED
```

### 卸载

```bash
rmmod dtsled.ko
```

---

### 附录：完整文件关系图

```
5_dtsled/
│
├── dtsled.c        ← 驱动源码（核心）
│   ├── dtsled_init()    模块入口：注册设备+映射地址+初始化GPIO
│   ├── dtsled_exit()    模块出口：关闭LED+释放资源
│   ├── dtsled_write()   写操作：接收用户数据→控制LED
│   ├── dtsled_open()    打开操作
│   ├── dtsled_release() 关闭操作
│   └── led_switch()     硬件操作：实际控制GPIO电平
│
├── ledAPP.c        ← 应用程序（测试）
│   └── main()           打开设备文件→发送控制命令→关闭
│
├── Makefile        ← 编译配置
│   └── 指定内核源码路径，编译 dtsled.ko
│
├── dtsled.ko       ← 编译出的内核模块（insmod 加载）
└── ledAPP          ← 编译出的用户程序
```

---

> **建议学习路径**：
> 1. 先理解 `3_newchrled`（新字符设备驱动，无设备树）→ 掌握字符设备基础
> 2. 再理解 `4_dtsof`（设备树 OF 函数）→ 掌握设备树 API
> 3. 最后学习本章 `5_dtsled` → 将前两者结合，**这是真正的现代 Linux 驱动开发模式**

---

*文档通过代码实际分析生成，结合正点原子阿尔法Linux开发板视频教程 5_dtsled 实验。*

---

## 第六章 Pinctrl 与 GPIO 子系统

> 基于正点原子阿尔法Linux开发板（IMX6ULL），结合 `gpioled.c` / `ledAPP.c` / `Makefile` 代码实例分析。

---

## 目录

1. [为什么需要 pinctrl 和 GPIO 子系统](#1-为什么需要-pinctrl-和-gpio-子系统)
2. [pinctrl 子系统](#2-pinctrl-子系统)
3. [GPIO 子系统](#3-gpio-子系统)
4. [gpioled.c 驱动源码完整流程分析](#4-gpioledc-驱动源码完整流程分析)
5. [ledAPP.c 应用程序分析](#5-ledappc-应用程序分析)
6. [5_dtsled vs 6_gpioled 核心对比](#6-5_dtsled-vs-6_gpioled-核心对比)
7. [关键知识点总结](#7-关键知识点总结)

---

### 1. 为什么需要 pinctrl 和 GPIO 子系统

### 回顾 5_dtsled 的痛点

在上一章 `5_dtsled` 中，驱动为了点亮一颗 LED，需要手动操作 5 个寄存器：

```c
/* 5_dtsled 的做法 —— 驱动做了大量硬件细节工作 */
writel(0x5, SW_MUX_GPIO1_IO03);     // ① 手动设置引脚复用
writel(0x10B0, SW_PAD_GPIO1_IO03);  // ② 手动设置电气属性
IMX6U_CCM_CCGR1 = of_iomap(nd, 0);  // ③ 手动映射时钟寄存器
// ... ④ 设置方向, ⑤ 设置电平
```

**问题**：
- 驱动要知道每个引脚的复用值（0x5 是什么？）
- 驱动要知道电气属性的完整位含义
- 换个引脚？改代码。换个板子？改更多代码
- 这些工作每个 GPIO 驱动都要做一遍

### 解决思路

```
┌─────────────────────────────────────────────────────────────┐
│  不用子系统之前:                                               │
│                                                              │
│  驱动 ──→ 直接操作寄存器 ──→ 硬件                              │
│         (驱动必须知道所有硬件细节)                              │
│                                                              │
│  用了子系统之后:                                               │
│                                                              │
│  驱动 ──→ GPIO子系统 ──→ Pinctrl子系统 ──→ 硬件                │
│         (驱动只说"我要GPIO1_03输出低电平")                      │
│         (子系统帮你查表、写寄存器)                              │
└─────────────────────────────────────────────────────────────┘
```

> **核心思想**：硬件细节从驱动中剥离，交给子系统。驱动只描述"要什么"，子系统负责"怎么做"。

---

### 2. Pinctrl 子系统

### 2.1 它管什么

Pinctrl = Pin Controller，管理引脚的**复用**和**电气属性**。

```
一个引脚能做什么？
                          
  IMX6ULL 的 GPIO1_IO03 ──→ ALT0: SAI1_RX_DATA0        (音频)
                       ──→ ALT1: ENET2_REF_CLK2        (以太网)
                       ──→ ALT2: CSI_DATA03            (摄像头)
                       ──→ ALT3: UART4_RTS             (串口)
                       ──→ ALT4: ENET1_1588_EVENT3     (以太网)
                  ★ ──→ ALT5: GPIO1_IO03              (GPIO)
                       ──→ ALT8: SRC_BT_CFG3

Pinctrl 子系统负责:
  ① 功能选择:  让引脚工作在哪个模式 (复用)
  ② 电气配置:  驱动能力、速度、上下拉、开漏等
```

### 2.2 在设备树中怎么配置

Pinctrl 的配置不在驱动代码里，而是在设备树中：

```dts
/* 设备树中的 pinctrl 节点 */
&iomuxc {                                    /* IMX6ULL 的 IOMUX 控制器 */
    pinctrl_gpioled: ledgrp {                /* 给 LED 用的引脚配置组 */
        fsl,pins = <
            MX6UL_PAD_GPIO1_IO03__GPIO1_IO03  0x10B0
            /*  ↑ 宏定义：引脚名 + 功能名           ↑ 电气属性值 */
        >;
    };
};
```

| 配置项 | 是谁在做 | 开发者需要做什么 |
|--------|---------|-----------------|
| **复用选择** | Pinctrl | 在设备树写 `MX6UL_PAD_GPIO1_IO03__GPIO1_IO03` |
| **电气属性** | Pinctrl | 在设备树写 `0x10B0` |
| **调用时机** | 内核自动 | 驱动 `probe` 时自动配置，卸载时自动恢复 |

### 2.3 和 5_dtsled 的区别

```c
/* ===== 5_dtsled: 驱动里手动操作 pinctrl ===== */
writel(0x5, SW_MUX_GPIO1_IO03);     // 手动写复用寄存器
writel(0x10B0, SW_PAD_GPIO1_IO03);  // 手动写电气属性寄存器

/* ===== 6_gpioled: pinctrl 子系统接管 ===== */
// 驱动里一行都不用写！
// 设备树里配置好，内核在加载驱动前自动完成 pinctrl 配置
```

> **关键理解**：`6_gpioled` 驱动代码里没有一行 pinctrl 操作。但引脚已经被正确配置了——因为 pinctrl 子系统在设备树→驱动的匹配过程中自动完成了配置。驱动只关心"拿到 GPIO 编号后怎么用"。

---

### 3. GPIO 子系统

### 3.1 它管什么

```
                  GPIO 子系统
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
    申请/释放     方向控制      电平控制
    gpio_request   gpio_direction  gpio_set_value
    gpio_free      _output/_input  gpio_get_value
                      │
                      ▼
              底层硬件寄存器操作
              (驱动不需要知道)
```

### 3.2 核心 API

| API | 作用 | 类比 |
|-----|------|------|
| `of_get_named_gpio()` | 从设备树读取 GPIO 编号 | 查电话本："LED 用几号引脚？" |
| `gpio_request()` | 申请使用这个 GPIO | "这个引脚我占用了，别人别碰" |
| `gpio_direction_output()` | 设为输出模式，同时设初始值 | "我要输出，初始给高电平" |
| `gpio_set_value()` | 输出高/低电平 | "现在输出低电平" |
| `gpio_free()` | 释放 GPIO | "我用完了，还回去" |

### 3.3 在你的代码里怎么用

```c
// ① 从设备树拿到 GPIO 编号
gpioled.led_gpio = of_get_named_gpio(gpioled.nd, "led-gpios", 0);
//                                                ↑ 属性名     ↑ 第0个GPIO
//  返回: GPIO 编号（比如 3，表示 GPIO1_IO03）

// ② 申请这个 GPIO
gpio_request(gpioled.led_gpio, "led-gpio");

// ③ 设为输出 + 初始输出高电平（LED灭）
gpio_direction_output(gpioled.led_gpio, 1);

// ④ 控制 LED：输出低电平 = 亮
gpio_set_value(gpioled.led_gpio, 0);   // LED ON
gpio_set_value(gpioled.led_gpio, 1);   // LED OFF
```

### 3.4 设备树中怎么配

和 `5_dtsled` 的设备树完全不同：

```dts
/* ===== 5_dtsled 的设备树: 手写寄存器地址 ===== */
alphaled {
    reg = <0x020C406C 0x04    // 要手动映射 5 个寄存器
           0x020E0068 0x04
           0x020E02F4 0x04
           0x0209C000 0x04
           0x0209C004 0x04>;
};

/* ===== 6_gpioled 的设备树: 只需一个 GPIO 属性 ===== */
gpioled {
    compatible = "alientek,gpioled";
    status = "okay";
    pinctrl-0 = <&pinctrl_gpioled>;    /* 引用 pinctrl 配置 */
    led-gpios = <&gpio1 3 GPIO_ACTIVE_LOW>;
    /*           ↑      ↑  ↑
         GPIO 控制器  引脚号  有效电平(低电平点亮) */
};
```

### 3.5 `of_get_named_gpio()` 内部干了什么

```
of_get_named_gpio(nd, "led-gpios", 0)
        │
        │  ① 从设备树节点 nd 中查找属性 "led-gpios"
        │  ② 读取该属性的第 0 个 GPIO 描述: <&gpio1 3 GPIO_ACTIVE_LOW>
        │  ③ 解析: GPIO控制器 = gpio1
        │          引脚号     = 3
        │          有效电平   = ACTIVE_LOW (低电平有效)
        │  ④ 通过 GPIO 子系统内部映射，返回一个整数编号
        │
        ▼
     返回: 3 (代表 GPIO1_IO03)
```

---

### 4. gpioled.c 驱动源码完整流程分析

### 4.1 整体架构（事件驱动视角）

```
insmod gpioled.ko
        │
        ▼
led_init()
  ├── 步骤1: 注册字符设备 (申请设备号→初始化cdev→添加cdev)
  ├── 步骤2: 自动创建设备节点 (class_create + device_create)
  ├── ★步骤3: 获取设备树 GPIO 信息
  │     ├── of_find_node_by_path("/gpioled")      找设备树节点
  │     ├── of_get_named_gpio(nd, "led-gpios", 0)  读 GPIO 编号
  │     └── gpio_request(gpio, "led-gpio")         申请 GPIO
  ├── ★步骤4: 配置 GPIO 为输出
  │     └── gpio_direction_output(gpio, 1)         输出模式 + 初始高电平(LED灭)
  └── 步骤5: 点亮 LED (验证硬件)
        └── gpio_set_value(gpio, 0)                LED 亮

★ 模块就绪，等待用户操作

./ledAPP /dev/gpioled 1
        │
        ▼
led_open() → filp->private_data = &gpioled
        │
        ▼
led_write()
  ├── copy_from_user(databuf, buf, count)     从用户空间拿数据
  └── gpio_set_value(dev->led_gpio, 0/1)      ★ 一句搞定，不再 readl/writel

rmmod gpioled.ko
        │
        ▼
led_exit()
  ├── gpio_set_value(gpioled.led_gpio, 1)    先关 LED
  ├── cdev_del + unregister_chrdev_region    注销字符设备
  ├── device_destroy + class_destroy          销毁设备节点
  └── gpio_free(gpioled.led_gpio)            ★ 释放 GPIO
```

### 4.2 和 5_dtsled 的数据流对比

```
5_dtsled:  用户write → copy_from_user → readl(GPIO1_DR) → 改bit3 → writel
            ↑ 依赖 of_iomap 映射的寄存器地址

6_gpioled: 用户write → copy_from_user → gpio_set_value(gpio, 0/1)
            ↑ GPIO 子系统内部帮你 readl/writel
```

---

### 5. ledAPP.c 应用程序分析

与 `5_dtsled` 的 ledAPP.c 几乎完全相同，唯一的区别是设备文件路径不同：

| 项目 | 5_dtsled | 6_gpioled |
|------|----------|-----------|
| 设备文件 | `/dev/dtsled` | `/dev/gpioled` |
| 用法 | `./ledAPP /dev/dtsled 0/1` | `./ledAPP /dev/gpioled 0/1` |

应用程序不关心里面是 `of_iomap` 还是 GPIO 子系统，它只管 `open → write → close`。

---

### 6. 5_dtsled vs 6_gpioled 核心对比

### 6.1 代码量对比

| | 5_dtsled | 6_gpioled |
|------|----------|-----------|
| 总行数 | 259 行 | 174 行 |
| 头文件 | 12 个 | 14 个（多 2 个 gpio 头文件） |
| 寄存器操作行 | ~30 行 | **0 行** |
| GPIO 操作 | readl/writel 手写 | gpio_xxx() API |
| 全局变量 | 5 个 `void __iomem *` | 0 个（不需要了！） |

### 6.2 关键差异速览

| 对比维度 | 5_dtsled | 6_gpioled |
|----------|----------|-----------|
| **寄存器地址** | 设备树 reg 属性，of_iomap 映射 | **不需要！GPIO 子系统内部处理** |
| **GPIO 信息** | 驱动自己知道是 GPIO1_IO03 | 设备树 `led-gpios` 属性 |
| **控制 LED** | `readl/writel(GPIO1_DR)` 操作寄存器 | `gpio_set_value(dev->led_gpio, 0/1)` |
| **引脚复用** | 驱动里手动 `writel(0x5, MUX)` | **Pinctrl 子系统+设备树 自动完成** |
| **电气属性** | 驱动里手动 `writel(0x10B0, PAD)` | **Pinctrl 子系统+设备树 自动完成** |
| **时钟** | 驱动里手动操作 CCM_CCGR1 | **GPIO 子系统内部处理** |
| **移植性** | 换引脚要改驱动代码 | 换引脚只改设备树 |
| **资源管理** | ioremap/iounmap 手动管理 | gpio_request/gpio_free |

### 6.3 同一件事，代码怎么变

```c
// ==================== 初始化 GPIO ====================

/* 5_dtsled: 需要 5 次 of_iomap + 5 次寄存器操作 */
IMX6U_CCM_CCGR1     = of_iomap(dtsled.nd, 0);    // 时钟
SW_MUX_GPIO1_IO03   = of_iomap(dtsled.nd, 1);    // 复用
SW_PAD_GPIO1_IO03   = of_iomap(dtsled.nd, 2);    // 电气
GPIO1_DR            = of_iomap(dtsled.nd, 3);    // 数据
GPIO1_GDIR          = of_iomap(dtsled.nd, 4);    // 方向
// 然后还要写 5 段寄存器初始化代码...

/* 6_gpioled: 只需 3 个 API 调用 */
gpioled.led_gpio = of_get_named_gpio(gpioled.nd, "led-gpios", 0);
gpio_request(gpioled.led_gpio, "led-gpio");
gpio_direction_output(gpioled.led_gpio, 1);


// ==================== 控制 LED ====================

/* 5_dtsled: 读-改-写 模式操作寄存器 */
val = readl(GPIO1_DR);
val &= ~(1 << 3);
writel(val, GPIO1_DR);

/* 6_gpioled: 一句话 */
gpio_set_value(dev->led_gpio, 0);


// ==================== 清理 ====================

/* 5_dtsled: 5 次 iounmap */
iounmap(IMX6U_CCM_CCGR1);
iounmap(SW_MUX_GPIO1_IO03);
iounmap(SW_PAD_GPIO1_IO03);
iounmap(GPIO1_DR);
iounmap(GPIO1_GDIR);

/* 6_gpioled: 一次 gpio_free */
gpio_free(gpioled.led_gpio);
```

---

### 7. 关键知识点总结

### 7.1 必须掌握

| # | 知识点 | 说明 |
|---|--------|------|
| 1 | **Pinctrl 的作用** | 管理引脚复用和电气属性，配置写在设备树 |
| 2 | **GPIO 子系统的作用** | 封装 GPIO 操作，驱动不再直接操作寄存器 |
| 3 | `of_get_named_gpio()` | 从设备树读 GPIO 信息，返回 GPIO 编号 |
| 4 | `gpio_request/free` | 申请/释放 GPIO 资源 |
| 5 | `gpio_direction_output/input` | 设置 GPIO 方向 |
| 6 | `gpio_set_value/get_value` | 读写 GPIO 电平 |
| 7 | 设备树 `led-gpios` 属性 | 替代 `reg`，描述 GPIO 引脚 |
| 8 | 设备树 pinctrl 配置 | `pinctrl-0 = <&pinctrl_xxx>` |
| 9 | 分层思想 | 驱动→GPIO子系统→Pinctrl子系统→硬件 |

### 7.2 驱动进化路线

```
1_chrdevbase     → 字符设备驱动基础 (手动 mknod)
3_newchrled      → 新字符设备 (自动创建设备节点)
4_dtsof          → 添加设备树 OF 函数
5_dtsled         → 设备树 reg 属性 + of_iomap (仍然手写寄存器)
6_gpioled   ← 你在这里  → ★ GPIO 子系统，不再操作寄存器
```

### 7.3 分层架构图

```
┌─────────────────────────────────────────┐
│  用户程序 (ledAPP.c)                      │
│  open → write → close                    │
└────────────────┬────────────────────────┘
                 │ 系统调用
┌────────────────▼────────────────────────┐
│  驱动 (gpioled.c)                        │
│  led_open, led_write, led_release       │
│  不碰寄存器，只调用 GPIO API              │
└────────────────┬────────────────────────┘
                 │ gpio_set_value()
┌────────────────▼────────────────────────┐
│  GPIO 子系统 (内核提供)                    │
│  管理 GPIO 编号、方向、电平               │
│  调用 pinctrl 完成底层硬件操作             │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│  Pinctrl 子系统 (内核提供)                │
│  操作 IOMUX 寄存器：复用选择 + 电气属性     │
│  配置来自设备树，驱动不感知                │
└────────────────┬────────────────────────┘
                 │ 总线
┌────────────────▼────────────────────────┐
│  IMX6ULL 硬件                            │
│  GPIO1 控制器、LED 灯                     │
└─────────────────────────────────────────┘
```

---

> **建议学习路径**：
> 1. `5_dtsled`（手写寄存器）→ 理解 GPIO 硬件工作原理
> 2. `6_gpioled`（GPIO 子系统）→ 理解 Linux 内核的分层抽象思想
> 3. 对比两者 → 理解"驱动不应该知道硬件细节"的工程哲学

---

*文档通过代码实际分析生成，结合正点原子阿尔法Linux开发板视频教程 6_gpioled 实验。*

---

## 第七章 蜂鸣器驱动

> 基于正点原子阿尔法Linux开发板（IMX6ULL），结合 `beep.c` / `ledAPP.c` / `Makefile` 代码实例分析。

---

## 目录

1. [实验背景：蜂鸣器 vs LED](#1-实验背景蜂鸣器-vs-led)
2. [硬件工作原理](#2-硬件工作原理)
3. [设备树配置](#3-设备树配置)
4. [beep.c 驱动源码完整流程分析](#4-beepc-驱动源码完整流程分析)
5. [ledAPP.c 应用程序分析](#5-ledappc-应用程序分析)
6. [重点函数深度解析](#6-重点函数深度解析)
7. [6_gpioled vs 7_beep 对比](#7-6_gpioled-vs-7_beep-对比)
8. [错误处理与 goto 回滚链](#8-错误处理与-goto-回滚链)
9. [Makefile 解析](#9-makefile-解析)
10. [关键知识点总结](#10-关键知识点总结)
11. [驱动执行完整时序图](#11-驱动执行完整时序图)

---

### 1. 实验背景：蜂鸣器 vs LED

### 1.1 为什么 LED 之后做蜂鸣器

学了实验6 `gpioled`，你已经掌握了用 GPIO 子系统控制一个 GPIO 引脚。蜂鸣器实验的驱动架构**与 LED 几乎一模一样**，但有一个关键区别：

| | LED（实验6） | 蜂鸣器（实验7） |
|------|-----------|-----------|
| **硬件** | LED 灯 | 有源蜂鸣器（三极管驱动） |
| **控制方式** | GPIO 输出高低电平 | GPIO 输出高低电平 |
| **电平逻辑** | 低电平 = 亮，高电平 = 灭 | 低电平 = 响，高电平 = 不响 |
| **驱动代码差异** | 极微 | 极微 |

> **核心认识**：这个实验的目的不是学新技术，而是**巩固 GPIO 子系统**——换个硬件、换个设备名，驱动框架完全一样。这说明 GPIO 子系统的抽象是通用的。

### 1.2 你在这个实验要巩固什么

- 字符设备驱动框架（实验1/3）
- 设备树节点与属性（实验4/5）
- GPIO 子系统 API（实验6）
- 错误处理 goto 链模式
- 驱动与应用的分离思维

---

### 2. 硬件工作原理

### 2.1 蜂鸣器类型

```
蜂鸣器分类:
  ├── 有源蜂鸣器（本实验用）
  │     ├── 内部自带振荡电路
  │     ├── 通电即响，断电即停
  │     └── 控制方式：GPIO 输出高低电平 = 开关
  │
  └── 无源蜂鸣器
        ├── 内部无振荡电路
        ├── 需要 PWM 方波驱动
        └── 控制方式：PWM 不同频率 = 不同音调
```

本实验用的是**有源蜂鸣器**，所以驱动和 LED 一样简单——只控制 GPIO 高低电平。

### 2.2 硬件电路原理

```
IMX6ULL GPIO ──→ 三极管基极 ──→ 蜂鸣器 ──→ VCC
                      │
                     GND

当 GPIO 输出低电平(0) → 三极管导通 → 蜂鸣器通电 → 蜂鸣器响
当 GPIO 输出高电平(1) → 三极管截止 → 蜂鸣器断电 → 蜂鸣器不响
```

> **注意**：和 LED 一样是**低电平有效**！这与直觉相反——写 `0` 是"开"，写 `1` 是"关"。

---

### 3. 设备树配置

### 3.1 设备树中的 beep 节点

来自开发板设备树（.dts）：

```dts
/* Pinctrl 配置 —— 设置引脚的复用和电气属性 */
&iomuxc {
    pinctrl_beep: beepgrp {
        fsl,pins = <
            MX6UL_PAD_SNVS_TAMPER1__GPIO5_IO01  0x10B0
            /*  ↑ 宏：引脚 + 功能         ↑ 电气属性值 */
        >;
    };
};

/* beep 设备节点 */
/ {
    beep {
        compatible = "alientek,beep";
        status = "okay";
        pinctrl-0 = <&pinctrl_beep>;           /* 引用 pinctrl 配置 */
        beep-gpios = <&gpio5 1 GPIO_ACTIVE_LOW>;
        /*             ↑      ↑  ↑
              GPIO控制器  引脚号  有效电平(低电平有效) */
    };
};
```

### 3.2 和 LED 的设备树对比

```dts
/* ===== LED(实验6) ===== */
MX6UL_PAD_GPIO1_IO03__GPIO1_IO03  0x10B0    // GPIO1_IO03
led-gpios = <&gpio1 3 GPIO_ACTIVE_LOW>;

/* ===== 蜂鸣器(实验7) ===== */
MX6UL_PAD_SNVS_TAMPER1__GPIO5_IO01  0x10B0   // GPIO5_IO01
beep-gpios = <&gpio5 1 GPIO_ACTIVE_LOW>;
```

结构完全一样，只是：
- GPIO 控制器不同：`gpio1` → `gpio5`
- 引脚编号不同：`3` → `1`
- 属性名不同：`led-gpios` → `beep-gpios`（按命名规范）

---

### 4. beep.c 驱动源码完整流程分析

### 4.1 设备结构体

```c
struct beep_dev {
    dev_t devid;              // 设备号（主+次）
    int major;                // 主设备号
    int minor;                // 次设备号
    struct cdev cdev;         // 内核字符设备结构体
    struct class *class;      // 设备类（用于自动创建设备节点）
    struct device *device;    // 设备实例
    struct device_node *nd;   // 设备树节点指针
    int beep_gpio;            // GPIO 编号（从设备树解析得到）
};
```

> **要点**：`beep_gpio` 是一个整数编号，由 `of_get_named_gpio()` 返回——不是寄存器地址！这是 GPIO 子系统封装的核心。

### 4.2 驱动初始化流程

```
insmod beep.ko
      │
      ▼
beep_init()
  │
  ├── 步骤① 注册字符设备号
  │     ├── beep.major = 0 → 走 alloc_chrdev_region() 自动分配
  │     └── 打印主次设备号到内核日志
  │
  ├── 步骤② 初始化 cdev 字符设备
  │     ├── beep.cdev.owner = THIS_MODULE
  │     └── cdev_init(&beep.cdev, &beep_fops)  ← 绑定 file_operations
  │
  ├── 步骤③ 添加 cdev 到内核
  │     └── cdev_add(&beep.cdev, beep.devid, BEEP_CNT)
  │
  ├── 步骤④ 创建类和设备节点
  │     ├── class_create(THIS_MODULE, "beep")   → /sys/class/beep/
  │     └── device_create(class, NULL, devid, NULL, "beep")  → /dev/beep
  │
  ├── 步骤⑤ 从设备树获取 GPIO ★核心★
  │     ├── of_find_node_by_path("/beep")       // 找设备树节点
  │     ├── of_get_named_gpio(nd, "beep-gpios", 0)  // 读 GPIO 编号
  │     └── gpio_request(beep_gpio, "beep-gpio")     // 申请 GPIO
  │
  ├── 步骤⑥ 配置 GPIO 为输出
  │     ├── gpio_direction_output(beep_gpio, 0)  // 输出模式 + 初始低电平
  │     └── gpio_set_value(beep_gpio, 0)         // 低电平 = 蜂鸣器响
  │
  └── 步骤⑦ 返回 0，模块加载成功
        │
        如果任何步骤失败 → goto 回滚链（反向清理已分配资源）
```

### 4.3 file_operations 操作集

```c
static const struct file_operations beep_fops = {
    .owner    = THIS_MODULE,
    .write    = beep_write,      // ★ 核心：通过 write 控制蜂鸣器
    .open     = beep_open,       // 绑定私有数据
    .release  = beep_release,    // 关闭时无操作
};
```

**没有 `.read`** — 为什么？

因为蜂鸣器（和 LED 一样）是输出设备，应用只需要"写命令"，不需要"读状态"。这是一个**单向控制**设备。

### 4.4 各操作函数详解

#### beep_open — 打开设备

```c
static int beep_open(struct inode *inode, struct file *filp)
{
    filp->private_data = &beep;  // ★ 关键：将设备结构体指针存入文件的私有数据
    return 0;
}
```

**为什么这样做？**

打开文件时，内核为本次打开创建一个 `struct file`，其中 `private_data` 是留给驱动用的 `void *`。驱动在这里存入 `beep` 的地址，后续 `write`/`release` 时通过 `filp->private_data` 取回来用。

```
open:  filp->private_data = &beep   (存入)
write: dev = filp->private_data;     (取出)
       gpio_set_value(dev->beep_gpio, ...)  (使用)
```

> 这就是驱动中传递"设备上下文"的标准模式。

#### beep_write — 控制蜂鸣器

```c
static ssize_t beep_write(struct file *filp, const char __user *buf,
                          size_t count, loff_t *ppos)
{
    int ret;
    unsigned char databuf[1];                       // 1字节缓冲区
    struct beep_dev *dev = filp->private_data;      // 取出设备结构体

    ret = copy_from_user(databuf, buf, count);      // ★ 从用户空间拷贝数据
    if (ret < 0) {
        return -EFAULT;                              // 拷贝失败，返回错误
    }

    if (databuf[0] == BEEPON) {                     // 用户写 1 → 蜂鸣器响
        gpio_set_value(dev->beep_gpio, 0);          // 低电平有效：0 = 响
    } else if (databuf[0] == BEEPOFF) {             // 用户写 0 → 蜂鸣器灭
        gpio_set_value(dev->beep_gpio, 1);          // 高电平：1 = 不响
    }

    return 0;
}
```

**执行流程分析**：

```
用户空间:  ./ledAPP /dev/beep 1
                │
                ▼  write(fd, [0x01], 1)
                │
================ 用户态/内核态 边界 ================
                │
                ▼  beep_write()
内核空间:     copy_from_user(databuf, buf, 1)  → databuf[0] = 1
                │
              if (databuf[0] == BEEPON)         → 条件成立
                │
                ▼
              gpio_set_value(dev->beep_gpio, 0) → GPIO输出低电平
                │
                ▼
              三极管导通 → 蜂鸣器通电 → 蜂鸣器响！
```

#### beep_release — 关闭设备

```c
static int beep_release(struct inode *inode, struct file *filp)
{
    return 0;  // 无操作，直接返回
}
```

> **思考**：为什么 release 里不关蜂鸣器？因为用户可能在 close 之后还希望蜂鸣器保持当前状态。这种行为由驱动设计者决定。如果你希望 close 时自动关蜂鸣器，在这里加 `gpio_set_value(dev->beep_gpio, 1);` 即可。

### 4.5 驱动退出流程

```
rmmod beep.ko
      │
      ▼
beep_exit()
  ├── gpio_set_value(beep.beep_gpio, 1)     // ① 关蜂鸣器（安全考虑）
  ├── cdev_del(&beep.cdev)                   // ② 从内核删除 cdev
  ├── unregister_chrdev_region(beep.devid, 1) // ③ 注销设备号
  ├── device_destroy(beep.class, beep.devid)  // ④ 销毁设备节点 /dev/beep
  ├── class_destroy(beep.class)              // ⑤ 销毁类 /sys/class/beep/
  └── gpio_free(beep.beep_gpio)             // ⑥ 释放 GPIO
```

> **释放顺序口诀**：先关硬件 → 再销设备（与 init 反向） → 最后放 GPIO。init 是"申请资源"，exit 是"释放资源"，顺序正好相反。

---

### 5. ledAPP.c 应用程序分析

### 5.1 完整执行流程

```
./ledAPP /dev/beep 1
  │
  ├── ① argc 检查：必须要有 3 个参数，否则打印 "Error Usage!" 退出
  │
  ├── ② open("/dev/beep", O_RDWR)
  │      └── 触发内核 beep_open() → private_data = &beep
  │
  ├── ③ atoi(argv[2]) → databuf[0]
  │      └── "1" → 1,  "0" → 0
  │
  ├── ④ write(fd, databuf, sizeof(databuf))
  │      └── 触发内核 beep_write() → copy_from_user → gpio_set_value
  │
  └── ⑤ close(fd)
         └── 触发内核 beep_release()
```

### 5.2 关键知识点

| 知识点 | 说明 |
|--------|------|
| `argc` / `argv[]` | 命令行参数：`argc`=参数个数，`argv[]`=字符串数组 |
| `atoi()` | 字符串转整数：`"1"` → `1` |
| `open()` | 系统调用，触发驱动的 `.open` |
| `write()` | 系统调用，触发驱动的 `.write` |
| `close()` | 系统调用，触发驱动的 `.release` |

### 5.3 使用说明

```bash
# 加载驱动
insmod beep.ko

# 控制蜂鸣器
./ledAPP /dev/beep 1    # 蜂鸣器响（低电平有效）
./ledAPP /dev/beep 0    # 蜂鸣器不响

# 卸载驱动
rmmod beep.ko
```

---

### 6. 重点函数深度解析

### 6.1 of_find_node_by_path — 查找设备树节点

```c
struct device_node *of_find_node_by_path(const char *path);
```

| 项目 | 说明 |
|------|------|
| **参数** | `"/beep"` — 设备树中的节点路径 |
| **返回值** | 指向 `device_node` 的指针，失败返回 `NULL` |
| **作用** | 在设备树中按路径查找节点 |
| **类比** | 按路径打开文件：`fopen("/etc/passwd", "r")` |

**设备树中的对应关系**：

```dts
/ {                  // ← 根节点
    beep {           // ← of_find_node_by_path("/beep") 找到这个节点
        ...
    };
};
```

### 6.2 of_get_named_gpio — 从设备树读 GPIO 信息

```c
int of_get_named_gpio(struct device_node *np, const char *propname, int index);
```

| 参数 | 值 | 说明 |
|------|-----|------|
| `np` | `beep.nd` | 设备树节点 |
| `propname` | `"beep-gpios"` | 属性名 |
| `index` | `0` | 该属性中第几个 GPIO（从0开始） |
| **返回值** | `5*32 + 1 = 161` | GPIO 编号（GPIO5_IO01） |

**内部解析过程**：

```
设备树:  beep-gpios = <&gpio5 1 GPIO_ACTIVE_LOW>;
                         │    │
                         │    └──→ 引脚号 = 1
                         └──────→ GPIO控制器 = gpio5

of_get_named_gpio() 内部:
  ┌─→ 解析 gpio5   → bank = 5
  ├─→ 解析 1       → pin  = 1
  └─→ 计算公式: gpio编号 = (bank - 1) * 32 + pin
                       = (5 - 1) * 32 + 1
                       = 129

  返回 129 → 存入 beep.beep_gpio
```

### 6.3 gpio_request — 申请 GPIO 资源

```c
int gpio_request(unsigned gpio, const char *label);
```

| 参数 | 说明 |
|------|------|
| `gpio` | GPIO 编号（由 `of_get_named_gpio` 返回） |
| `label` | 标签，用于调试（出现在 `/sys/kernel/debug/gpio`） |

**为什么要申请？**

内核用引用计数管理 GPIO——一个 GPIO 同时只能被一个驱动使用。`gpio_request` 就是"声明占用"，防止多个驱动争抢同一个引脚。

**类比**：在图书馆借书——你先登记（request），然后才能阅读（使用），最后要还回去（free）。

### 6.4 gpio_direction_output — 设置 GPIO 为输出

```c
int gpio_direction_output(unsigned gpio, int value);
```

| 参数 | 说明 |
|------|------|
| `gpio` | GPIO 编号 |
| `value` | 初始输出值（`0`=低电平, `1`=高电平） |

**本实验中的调用**：`gpio_direction_output(beep.beep_gpio, 0)`

- 设置 GPIO5_IO01 为**输出模式**
- 初始输出**低电平** → 蜂鸣器一初始化就响

> **为什么初始化要设为低电平？** 这是为了验证硬件——驱动加载时蜂鸣器响一声，说明硬件没问题。实际上这行之后又 `gpio_set_value(beep_gpio, 0)` 了一次，有点冗余。

### 6.5 gpio_set_value — 设置 GPIO 电平

```c
void gpio_set_value(unsigned gpio, int value);
```

| `value` | 含义 | 蜂鸣器状态 |
|---------|------|-----------|
| `0` | 低电平 | **响**（三极管导通） |
| `1` | 高电平 | **不响**（三极管截止） |

> **关键理解**：`gpio_set_value(gpio, 0)` 等价于之前实验5中的 `readl/writel` 操作 GPIO 数据寄存器，但开发者不需要知道寄存器地址。

### 6.6 copy_from_user — 用户空间到内核空间的数据拷贝

```c
unsigned long copy_from_user(void *to, const void __user *from, unsigned long n);
```

| 参数 | 说明 |
|------|------|
| `to` | 内核空间目标地址（`databuf`） |
| `from` | 用户空间源地址（`buf`） |
| `n` | 拷贝的字节数（`count`） |
| **返回值** | `0`=成功，非0=未能拷贝的字节数 |

> **安全意义**：内核不能直接访问用户空间指针（用户可能传一个非法地址导致内核崩溃）。`copy_from_user` 会先**检查地址合法性**再拷贝，保证内核安全。

---

### 7. 6_gpioled vs 7_beep 对比

### 7.1 代码结构对比

| 对比维度 | 6_gpioled (LED) | 7_beep (蜂鸣器) | 差异 |
|----------|-----------------|-----------------|------|
| 头文件 | 14 个 | 14 个 | 完全相同 |
| 设备结构体字段 | 7 个 | 7 个 | 完全相同 |
| `file_operations` | open/write/release | open/write/release | 完全相同 |
| 设备号分配 | alloc_chrdev_region | alloc_chrdev_region | 完全相同 |
| cdev 操作 | cdev_init + cdev_add | cdev_init + cdev_add | 完全相同 |
| 类/设备创建 | class_create + device_create | class_create + device_create | 完全相同 |
| GPIO 获取 | of_get_named_gpio(nd, "led-gpios", 0) | of_get_named_gpio(nd, "beep-gpios", 0) | **仅属性名不同** |
| 方向设置 | gpio_direction_output(gpio, 1) | gpio_direction_output(gpio, 0) | **仅初始值不同** |
| 设备树节点路径 | "/gpioled" | "/beep" | **仅路径不同** |
| write 中的判断 | LEDON/LEDOFF | BEEPON/BEEPOFF | **仅宏名不同** |
| 设备名 | "gpioled" | "beep" | **仅名称不同** |

### 7.2 核心发现

```
6_gpioled 和 7_beep 的代码结构几乎完全一样！

差异只在这些地方:
  "led" ←→ "beep"           (命名)

这说明: GPIO 子系统提供了统一的抽象，
       同样的框架可以驱动 LED、蜂鸣器、继电器、电机...
       只要你通过 GPIO 高低电平控制的，全都一样！
```

---

### 8. 错误处理与 goto 回滚链

### 8.1 goto 链结构

```c
static int __init beep_init(void)
{
    int ret = 0;

    // 步骤1: 注册设备号
    ret = alloc_chrdev_region(...);
    if (ret < 0) goto fail_devid;           // → 直接返回，无需清理

    // 步骤2: 初始化 cdev
    cdev_init(...);
    ret = cdev_add(...);
    if (ret) goto fail_cdevadd;              // → 需清理设备号

    // 步骤3: 创建类
    beep.class = class_create(...);
    if (IS_ERR(beep.class)) {
        ret = PTR_ERR(beep.class);
        goto fail_class;                     // → 需清理cdev+设备号
    }

    // 步骤4: 创建设备
    beep.device = device_create(...);
    if (IS_ERR(beep.device)) {
        ret = PTR_ERR(beep.device);
        goto fail_device;                    // → 需清理类+cdev+设备号
    }

    // 步骤5: 获取GPIO
    // ... 可能失败的步骤
    //         goto fail_nd → fail_set → ...

    return 0;  // 全部成功！

fail_set:
    gpio_free(beep.beep_gpio);
fail_nd:
    device_destroy(beep.class, beep.devid);
fail_device:
    class_destroy(beep.class);
fail_class:
    cdev_del(&beep.cdev);
fail_cdevadd:
    unregister_chrdev_region(beep.devid, BEEP_CNT);
fail_devid:
    return ret;
}
```

### 8.2 goto 标签清理内容

| 标签 | 清理内容 | 为何需要清理 |
|------|---------|-------------|
| `fail_set` | `gpio_free()` | 释放已申请的 GPIO |
| `fail_nd` | `device_destroy()` | 销毁已创建的设备节点 |
| `fail_device` | `class_destroy()` | 销毁已创建的类 |
| `fail_class` | `cdev_del()` | 删除已添加的 cdev |
| `fail_cdevadd` | `unregister_chrdev_region()` | 注销已注册的设备号 |
| `fail_devid` | （无） | 还没注册成功，直接返回错误 |

> **设计原则**：init 中从前往后申请，goto 标签从后往前清理。每个标签只清理"到这个标签为止已经申请成功"的资源。这就是**栈式资源管理**——后申请的先释放。

---

### 9. Makefile 解析

```makefile
KERNELDIR := /home/zzk/linux/IMX6ULL/linux/linux-imx-rel_imx_4.1.15_2.1.0_ga_alientek
# ↑ 内核源码树路径（正点原子IMX6ULL开发板的内核）

CURRENT_PATH := $(shell pwd)        # 当前目录路径
obj-m := beep.o                     # 目标：编译 beep.o → beep.ko

build: kernel_modules               # 默认目标

kernel_modules:
    $(MAKE) -C $(KERNELDIR) M=$(CURRENT_PATH) modules
    #        ↑ 进入内核源码树        ↑ 模块源码在当前目录
    # 意思：在内核源码的上下文中编译当前目录的模块

clean:
    $(MAKE) -C $(KERNELDIR) M=$(CURRENT_PATH) clean
```

### 关键理解

| 语法 | 含义 |
|------|------|
| `obj-m := beep.o` | 声明 beep 为**模块**（m = module）。如果是 `obj-y` 则是编译进内核 |
| `-C $(KERNELDIR)` | 切换到内核源码目录执行 make |
| `M=$(CURRENT_PATH)` | 告诉内核构建系统：模块代码在 M 指定的目录 |
| `modules` | make 目标：编译内核模块 |

> **为什么编译内核模块需要内核源码树？** 内核模块依赖大量的内核头文件和 Makefile。`-C` 切换到内核源码树，内核的顶层 Makefile 会处理一切——编译器、头文件路径、内核配置等。

---

### 10. 关键知识点总结

### 10.1 必须掌握的 12 个知识点

| # | 知识点 | 属于 | 说明 |
|---|--------|------|------|
| 1 | `alloc_chrdev_region()` | 字符设备 | 自动分配设备号 |
| 2 | `cdev_init()` + `cdev_add()` | 字符设备 | 注册字符设备到内核 |
| 3 | `class_create()` + `device_create()` | 设备模型 | 自动创建 `/dev/beep` |
| 4 | `of_find_node_by_path()` | 设备树 | 按路径查找设备树节点 |
| 5 | `of_get_named_gpio()` | GPIO子系统 | 从设备树解析 GPIO 编号 |
| 6 | `gpio_request()` | GPIO子系统 | 申请 GPIO 使用权 |
| 7 | `gpio_direction_output()` | GPIO子系统 | 设置 GPIO 为输出模式 |
| 8 | `gpio_set_value()` | GPIO子系统 | 控制 GPIO 输出电平 |
| 9 | `copy_from_user()` | 内核API | 安全地从用户空间拷贝数据 |
| 10 | `filp->private_data` | VFS | 驱动传递设备上下文的机制 |
| 11 | goto 回滚链 | 错误处理 | 资源分配失败时的反向清理模式 |
| 12 | `module_init()` / `module_exit()` | 模块框架 | 指定模块的入口和出口函数 |

### 10.2 驱动开发"套路"总结

```
Linux 字符设备驱动开发的 6 步套路:

  ┌─ 步骤1: 定义设备结构体
  │   (装所有设备相关的数据：devid, cdev, gpio, class...)
  │
  ├─ 步骤2: 实现 file_operations
  │   (open → 绑定 private_data
  │    write/read → copy_from/to_user + 硬件操作
  │    release → 清理)
  │
  ├─ 步骤3: 实现 init 函数
  │   (alloc_chrdev_region → cdev_init → cdev_add
  │    → class_create → device_create → 硬件初始化)
  │
  ├─ 步骤4: 实现 exit 函数
  │   (与 init 反向：硬件关闭 → device_destroy → class_destroy
  │    → cdev_del → unregister_chrdev_region)
  │
  ├─ 步骤5: module_init/exit + MODULE_LICENSE
  │   (模块入口出口 + 许可证声明)
  │
  └─ 步骤6: 写 Makefile
       (obj-m := xxx.o + 指向内核源码树)
```

### 10.3 你已经走过的学习路线

```
实验1   chrdevbase     → 字符设备驱动基础 (手动 mknod)
实验2   led            → LED 驱动初体验
实验3   newchrled      → 新字符设备框架 (自动创建设备节点)
实验4   dtsof          → 设备树 OF 函数基础
实验5   dtsled         → 设备树 reg 属性 + of_iomap (手动寄存器)
实验6   gpioled        → ★ GPIO 子系统 (核心突破！不再操作寄存器)
实验7   beep           → 蜂鸣器驱动 ★ (GPIO子系统的巩固应用)
═══════════════════════════════════════════════════════════════
                         【第一个里程碑达成！
              你已掌握：字符设备框架 + 设备树 + GPIO子系统】
═══════════════════════════════════════════════════════════════
实验8   atomic         → 原子操作 (并发保护入门)
实验9   spinlock       → 自旋锁 (忙等待锁)
实验10  semaphore      → 信号量 (休眠锁)
实验11  mutex          → 互斥锁 (最常用的锁)
实验12  key            → 按键输入驱动 (中断入门)
...
```

---

### 11. 驱动执行完整时序图

```
时间轴 ─────────────────────────────────────────────────────────────→

【模块加载阶段】insmod beep.ko

  insmod ──→ beep_init()
               ├── alloc_chrdev_region()       分配设备号 (如 248,0)
               ├── cdev_init() + cdev_add()     注册字符设备
               ├── class_create("beep")         创建 /sys/class/beep/
               ├── device_create()              创建 /dev/beep
               ├── of_find_node_by_path()       查找设备树 /beep 节点
               ├── of_get_named_gpio()          解析 beep-gpios = <&gpio5 1>
               ├── gpio_request()               申请 GPIO5_IO01
               ├── gpio_direction_output(gpio,0) 配置为输出，初始低电平
               └── gpio_set_value(gpio, 0)      蜂鸣器响一声（验证硬件）
                    │
                    ▼
               返回 0 → 模块加载成功 → 蜂鸣器已响
               
【运行阶段】./ledAPP /dev/beep 1

  用户程序                          内核驱动
  ────────                        ──────────
  open("/dev/beep", O_RDWR)  ──→ beep_open()
                                   private_data = &beep
                                 ← return 0
                                 
  write(fd, [1], 1)          ──→ beep_write()
                                   copy_from_user([1], ...)    用户态→内核态
                                   if (databuf[0] == 1) → BEEPON
                                   gpio_set_value(gpio, 0)    GPIO输出低电平
                                   蜂鸣器响！
                                 ← return 0
                                 
  close(fd)                  ──→ beep_release()
                                 ← return 0

【模块卸载阶段】rmmod beep.ko

  rmmod ──→ beep_exit()
               ├── gpio_set_value(gpio, 1)     关蜂鸣器
               ├── cdev_del()                   删除字符设备
               ├── unregister_chrdev_region()   注销设备号
               ├── device_destroy()             删除 /dev/beep
               ├── class_destroy()              删除 /sys/class/beep/
               └── gpio_free()                  释放 GPIO5_IO01
                    │
                    ▼
               模块卸载完成
```

---

> **学习建议**：
> 1. 对比 `6_gpioled` 和 `7_beep` 的代码，感受 GPIO 子系统的通用性
> 2. 手写一遍 goto 回滚链，理解资源管理的思想
> 3. 思考：如果不用 GPIO 子系统，你要写多少行寄存器操作代码？
> 4. 准备进入实验8：原子操作——驱动不止你一个人在用！

---

*文档结合代码实际运行逻辑分析生成，知识点基于正点原子阿尔法Linux开发板驱动开发篇视频教程 7_beep 实验。*

---

## 第八章 原子操作（并发保护）

> 基于正点原子阿尔法Linux开发板（IMX6ULL），结合 `atomic.c` / `atomicAPP.c` / `Makefile` 代码实例分析。

---

## 目录

1. [实验背景：为什么需要原子操作](#1-实验背景为什么需要原子操作)
2. [原子操作的概念与原理](#2-原子操作的概念与原理)
3. [atomic.c 驱动源码完整流程分析](#3-atomicc-驱动源码完整流程分析)
4. [atomicAPP.c 应用程序分析](#4-atomicappc-应用程序分析)
5. [重点函数深度解析](#5-重点函数深度解析)
6. [原代码中存在的 Bug 分析](#6-原代码中存在的-bug-分析)
7. [7_beep vs 8_atomic 对比](#7-7_beep-vs-8_atomic-对比)
8. [Makefile 解析](#8-makefile-解析)
9. [关键知识点总结](#9-关键知识点总结)
10. [驱动执行完整时序图](#10-驱动执行完整时序图)

---

### 1. 实验背景：为什么需要原子操作

### 1.1 问题场景

实验1~7 的驱动有一个隐藏前提：**假设同一时刻只有一个程序在打开设备**。

```
正常情况（单用户）:
  App A: open(/dev/led) → write → close
  没问题 ✓

异常情况（多用户）:
  App A: open(/dev/led) → write...
                               App B: open(/dev/led) → write ← 冲突！
  两个程序同时操作同一个 GPIO → 不可预测 ✗
```

### 1.2 本实验要解决什么

| | 之前的驱动（1~7） | 本实验（8_atomic） |
|---|---|---|
| **并发保护** | 无 | 有（原子操作锁） |
| **同一时刻** | 多个程序都能 open | **只有第一个能 open，其他返回 -EBUSY** |
| **实现方式** | — | `atomic_t` + `atomic_dec_and_test()` |

> **核心认识**：原子操作是 Linux 内核中最轻量级的并发保护手段。这个实验的目的不是学新硬件，而是在熟悉的 LED 驱动上加入并发保护——让你专注于"锁"这个概念本身。

### 1.3 本实验与前面实验的关系

```
实验6 gpioled    → GPIO 子系统操作 LED
实验7 beep       → GPIO 子系统操作蜂鸣器（框架复用验证）
实验8 atomic     → 在 GPIO LED 基础上，加入原子操作实现"互斥访问"
                  （驱动本体仍然是 LED，新知识点仅在于并发保护）
```

---

### 2. 原子操作的概念与原理

### 2.1 什么是"原子"

> **原子 = 不可分割 = 要么做完，要么完全没做，不存在"做了一半"的状态。**

类比：银行转账

```
非原子操作（有漏洞）:
  ① 读余额: balance = 1000
  ② 扣款:   balance = balance - 500    ← 如果①和②之间被另一个转账插队…
  ③ 写回:   存 500

原子操作（安全）:
  ① atomic_sub(500, &balance)           ← 一条指令完成"读-改-写"，不可打断
```

### 2.2 为什么普通变量不行

```c
/* 错误示范 —— 非原子操作，有竞态条件 */
int lock = 1;

// App A:                    // App B:
if (lock > 0) {              if (lock > 0) {       ← A 和 B 同时读到 lock=1
    lock--;                  // 都以为自己拿到了锁！
    // ... 操作硬件 ...           lock--;
}                            }
// 结果：lock = -1，两个程序同时认为自己持有锁 → 完全失控
```

**问题本质**：`if (lock > 0) { lock--; }` 是两条 CPU 指令（读 + 写），中间可以被中断、抢占或多核并行打断。这是经典的 **read-modify-write 竞态条件**。

### 2.3 内核的 `atomic_t` 类型

```c
typedef struct {
    int counter;         // 计数器值
} atomic_t;
```

内核把这个普通的 `int` 包装成 `atomic_t`，所有修改操作都通过**专用函数**完成。这些函数在 ARM 平台上用 **LDREX/STREX 独占指令**实现，保证"读-改-写"不可打断。

### 2.4 本实验使用的原子操作函数一览

| 函数 | 作用 | 本实验中用法 |
|------|------|-------------|
| `atomic_set(&v, 1)` | 初始化原子变量为 1 | init 中设 lock=1（可用） |
| `atomic_read(&v)` | 读取原子变量当前值 | 调试/判断（原代码 #if 0 中有） |
| `atomic_dec_and_test(&v)` | **减 1 并测试**，减后为 0 返回 true | open 中"抢锁" ★核心★ |
| `atomic_inc(&v)` | 加 1 | release 中"释放锁"；open 抢锁失败恢复值 |

### 2.5 锁机制的核心逻辑（配图版）

```
atomic_t lock = 1;     // 1 = 可用,  0 = 已被占用

值的变化轨迹:

                    App A open           App A close
                       ↓                    ↓
  lock:  1  ─────────→  0  ──────────────→  1
           "可用"       "被A占用"          "可用"


                    App B open (此时 lock=0)
                       ↓
              atomic_dec_and_test → 0→-1, return false
                       ↓
              atomic_inc: -1→0    恢复原值（因为没抢到！）
                       ↓
              return -EBUSY       告诉 App B: "设备正忙！"
```

> **关键细节**：没抢到锁时为什么要 `atomic_inc` 恢复？因为 `atomic_dec_and_test` 已经执行了减 1 操作——虽然返回值告诉你"没抢到"，但值已经被改了。不恢复的话，lock 值就永久错误了。

---

### 3. atomic.c 驱动源码完整流程分析

### 3.1 新增头文件

```c
#include <linux/atomic.h>    /* ★ 新增 */
```

> 对比实验6/7：其余 14 个头文件完全相同，仅多一个 `<linux/atomic.h>`。这就是本实验唯一需要新学的头文件。

### 3.2 设备结构体 —— 新增 `atomic_t lock`

```c
struct gpioled_dev {
    dev_t devid;              // 设备号（主+次）
    int major;                // 主设备号
    int minor;                // 次设备号
    struct cdev cdev;         // 内核字符设备结构体
    struct class *class;      // 设备类
    struct device *device;    // 设备实例
    struct device_node *nd;   // 设备树节点指针
    int led_gpio;             // LED 的 GPIO 编号

    atomic_t lock;            // ★ 新增：原子锁，1=可用，0=被占用
};
```

> **设计思路**：`lock` 是设备级的锁（每个设备一把锁），放在设备结构体里是自然的做法。如果有多个 LED，每个 LED 各有一把自己的 `lock`，互不影响。

### 3.3 驱动初始化流程

```
insmod atomic.ko
      │
      ▼
led_init()
  │
  ├── 步骤① ★ atomic_set(&gpioled.lock, 1);
  │      初始化原子锁为 1（可用状态），必须在注册设备之前完成
  │      为什么？如果先注册设备再初始化锁 → 注册完的瞬间就可能被 open → 读到未初始化的锁
  │
  ├── 步骤② 注册字符设备号
  │      alloc_chrdev_region(&gpioled.devid, 0, GPIOLED_CNT, GPIOLED_NAME)
  │      （major=0 表示让内核自动分配）
  │
  ├── 步骤③ cdev_init + cdev_add
  │      cdev_init(&gpioled.cdev, &led_fops) → 绑定 file_operations
  │      cdev_add(&gpioled.cdev, gpioled.devid, GPIOLED_CNT) → 注册入内核
  │
  ├── 步骤④ class_create(THIS_MODULE, "gpioled")
  │      创建 /sys/class/gpioled/
  │
  ├── 步骤⑤ device_create(gpioled.class, NULL, gpioled.devid, NULL, "gpioled")
  │      创建 /dev/gpioled（内部发 uevent → mdev 建节点）
  │
  ├── 步骤⑥ 从设备树获取 GPIO 信息
  │      of_find_node_by_path("/gpioled") → 查找设备树节点
  │      of_get_named_gpio(nd, "led-gpios", 0) → 解析 GPIO 编号
  │
  ├── 步骤⑦ 申请并配置 GPIO
  │      gpio_request(led_gpio, "led-gpio") → 声明占用
  │      gpio_direction_output(led_gpio, 1) → 输出模式，初始高电平（LED 灭）
  │      gpio_set_value(led_gpio, 0) → 输出低电平，亮灯验证硬件
  │
  └── 返回 0 → 模块加载成功
```

### 3.4 file_operations 操作集 —— open 和 release 不再空转

```c
static const struct file_operations led_fops = {
    .owner    = THIS_MODULE,
    .write    = led_write,       // 控制 LED（同实验6）
    .open     = led_open,        // ★ 多了原子锁检查
    .release  = led_release,     // ★ 多了原子锁释放
};
```

**与实验6/7的关键差异**：`open` 和 `release` 不再是简单绑定/空函数，而是包含了抢锁/释放逻辑。

### 3.5 各操作函数逐行详解

#### 3.5.1 led_open —— 打开设备（抢锁） ★最重要★

```c
static int led_open(struct inode *inode, struct file *filp)
{
    /* ① 绑定设备结构体指针（同之前实验） */
    filp->private_data = &gpioled;

    /* ② 尝试抢锁：atomic_dec_and_test
     *    将 lock 减 1，然后判断减后的值是不是 0
     *    如果 lock 原来是 1 → 1-1=0 → 返回 true → 抢到了！         
     *    如果 lock 原来是 0 → 0-1=-1 → 返回 false → 没抢到！
     */
    if (!atomic_dec_and_test(&gpioled.lock)) {
        /* ③ 没抢到锁 → 先恢复 lock 值（因为已经减1了） */
        atomic_inc(&gpioled.lock);
        /* ④ 返回 -EBUSY → 上层 open() 返回 -1, errno=EBUSY */
        return -EBUSY;
    }
    /* ⑤ 抢到了锁 → 正常返回 */
    return 0;
}
```

**执行流程（分支版）**：

```
led_open() 被调用
      │
      ▼
filp->private_data = &gpioled       ① 绑定设备
      │
      ▼
atomic_dec_and_test(&gpioled.lock)  ② 尝试减1并测试
      │
      ├── lock=1 → 1→0, return true
      │     └── !true → 不进入 if → return 0 (成功!)
      │
      └── lock=0 → 0→-1, return false
            └── !false → 进入 if
                  ├── atomic_inc(-1→0)   ③ 恢复原值 ★重要!
                  └── return -EBUSY      ④ 告诉应用"设备忙"
```

**原代码中的 `#if 0` 注释块**展示的是**错误的旧写法**：

```c
/* 这段代码被 #if 0 禁用了，因为它有竞态条件 */
#if 0
    if (atomic_read(&gpioled.lock) <= 0) {
        return -EBUSY;              // ① 读 lock 值
    } else {
        atomic_dec(&gpioled.lock);  // ② 减 lock 值
    }
#endif
```

❌ ①和②之间可以被中断！如果 App A 和 App B 同时执行到①，都读到 lock=1，然后都执行②把 lock 减两次 → lock=-1。两个程序都以为自己抢到了锁 → **互斥失效**。

✅ `atomic_dec_and_test()` 把"读+判断+减"合并成一条原子操作 → 不可打断 → 安全。

#### 3.5.2 led_release —— 关闭设备（释放锁）

```c
static int led_release(struct inode *inode, struct file *filp)
{
    struct gpioled_dev *dev = filp->private_data;  // 取出设备结构体

    atomic_inc(&dev->lock);  // ★ 锁值+1，释放驱动使用权

    return 0;
}
```

```
释放锁的过程：

  lock: 0  ──atomic_inc()──→  1
         "被A占用"            "可用"

App B 再次 open → atomic_dec_and_test(1→0) → 成功！
```

#### 3.5.3 led_write —— 控制 LED（无需额外加锁）

```c
static ssize_t led_write(struct file *filp, const char __user *buf,
                         size_t count, loff_t *ppos)
{
    int ret;
    unsigned char databuf[1];
    struct gpioled_dev *dev = filp->private_data;

    ret = copy_from_user(databuf, buf, count);    // 从用户空间拷贝数据
    /* ★ BUG: copy_from_user 返回 unsigned long（未拷贝字节数）
     *        成功=0, 失败>0, 永远不会<0 */
    if (ret < 0) {
        return -EINVAL;
    }

    if (databuf[0] == LEDON) {                    // 用户写 1 → LED 亮
        gpio_set_value(dev->led_gpio, 0);         // 低电平有效：0=亮
    } else if (databuf[0] == LEDOFF) {            // 用户写 0 → LED 灭
        gpio_set_value(dev->led_gpio, 1);         // 高电平：1=灭
    }

    return 0;
}
```

> **注意**：`led_write` 里面没有再加锁！因为锁加在 `open` 上了——只有 `open` 成功的进程才能执行 `write`。这是一个**"文件打开级"的互斥锁**，不是"每次操作级"的锁。

### 3.6 驱动退出流程

```
rmmod atomic.ko
      │
      ▼
led_exit()
  ├── gpio_set_value(led_gpio, 1)           // ① 关 LED
  ├── cdev_del(&gpioled.cdev)               // ② 删除 cdev（★顺序有Bug，见第6节）
  ├── unregister_chrdev_region(...)         // ③ 注销设备号
  ├── device_destroy(gpioled.class, devid)  // ④ 销毁 /dev/gpioled
  ├── class_destroy(gpioled.class)          // ⑤ 销毁 /sys/class/gpioled/
  └── gpio_free(gpioled.led_gpio)          // ⑥ 释放 GPIO
```

---

### 4. atomicAPP.c 应用程序分析

### 4.1 与之前 APP 的关键差异

```c
/* ===== 前面实验的 APP（以 ledAPP.c 为例）===== */
int main(int argc, char *argv[])
{
    open("/dev/gpioled", O_RDWR);      // 打开
    write(fd, databuf, sizeof(...));   // 写命令
    close(fd);                          // 立即关闭
    return 0;
}

/* ===== 本实验的 APP（atomicAPP.c）===== */
int main(int argc, char *argv[])
{
    open("/dev/gpioled", O_RDWR);      // 打开（拿到锁）
    write(fd, databuf, sizeof(...));   // 写命令

    /* ★ 新增：模拟长时间占用设备 */
    while (1) {
        sleep(5);                       // 每 5 秒
        cnt++;
        printf("App Running times:%d\r\n", cnt);
        if (cnt >= 5) break;            // 共占用 5×5=25 秒
    }
    printf("App Running finished!\r\n");

    close(fd);                          // 关闭（释放锁）
    return 0;
}
```

### 4.2 设计目的 —— 验证并发互斥

```
这个 25 秒的循环是为了让你在开发板上做这个实验：

终端1: ./atomicAPP /dev/gpioled 1 &    ← 后台运行，占用设备 25 秒
终端2: ./atomicAPP /dev/gpioled 0      ← 立即尝试打开设备
        → "file /dev/gpioled open failed!"  ← 因为终端1还占着锁！

终端1 25秒结束 → close()释放锁
终端2 重新运行 → 这次就能 open 了！
```

### 4.3 完整执行时序

```
./atomicAPP /dev/gpioled 1
  │
  ├── open("/dev/gpioled", O_RDWR)
  │      → atomic_dec_and_test(lock): 1→0, 抢到锁!
  │
  ├── write(fd, [1], 1)
  │      → gpio_set_value(led_gpio, 0) → LED 亮
  │
  ├── while(1) { sleep(5); cnt++; ... }     ← 占用 25 秒
  │      │
  │      │  此时其他程序 open → -EBUSY
  │      │
  │      └── cnt>=5 → break → printf("finished!")
  │
  └── close(fd)
         → atomic_inc(lock): 0→1, 释放锁!
         → 现在其他程序可以 open 了
```

---

### 5. 重点函数深度解析

### 5.1 atomic_set —— 初始化原子变量

```c
void atomic_set(atomic_t *v, int i);
```

| 参数 | 说明 |
|------|------|
| `v` | 指向原子变量的指针 |
| `i` | 初始值 |

**本实验中**：`atomic_set(&gpioled.lock, 1)` = 初始化锁为"可用"状态。

### 5.2 atomic_dec_and_test —— 减1并测试 ★核心★

```c
int atomic_dec_and_test(atomic_t *v);
```

| 项目 | 说明 |
|------|------|
| **操作** | 将 `*v` 减 1，然后判断减后的值是否为 0 |
| **返回值** | 减后为 0 → `true`（非0）；减后不为 0 → `false`（0） |
| **原子性** | ARM 的 LDREX/STREX 独占指令保证，不可中断 |
| **内核实现** | `<linux/atomic.h>` → 架构相关汇编实现 |

**ARM 架构底层实现原理**：

```asm
; atomic_dec_and_test 在 ARM 上的伪代码
retry:
    LDREX  r0, [&lock]       ; ① 独占读取 lock 值到 r0
    SUB    r0, r0, #1        ; ② 减 1
    STREX  r1, r0, [&lock]   ; ③ 独占写回（如果地址被其他 CPU 碰过则失败）
    TEQ    r1, #0            ; ④ 检测 STREX 是否成功
    BNE    retry              ; ⑤ 失败就重试
    ; r0 现在是减1后的值 → C 层判断是否为 0 得到返回值
```

> **关键**：LDREX（Load Exclusive）和 STREX（Store Exclusive）是 ARM 的独占访问指令对。STREX 只有在"从 LDREX 到 STREX 之间地址未被其他 CPU/设备修改"时才成功写回——否则失败并重试。这就是硬件级的原子性保证。

### 5.3 atomic_inc —— 加1

```c
void atomic_inc(atomic_t *v);
```

| 项目 | 说明 |
|------|------|
| **操作** | 将 `*v` 加 1 |
| **本实验中两处使用** | ① open 抢锁失败时恢复值；② release 释放锁 |

### 5.4 atomic_read —— 读取当前值

```c
int atomic_read(const atomic_t *v);
```

纯读取操作，不修改。在 `#if 0` 禁用的旧代码中出现过一次，展示了它被用于"先读后判"的错误模式。

### 5.5 -EBUSY 错误码

```c
return -EBUSY;
```

| 项目 | 说明 |
|------|------|
| **含义** | "Device or resource busy" — 设备或资源正忙 |
| **宏值** | 16（定义在 `<linux/errno.h>`） |
| **上层表现** | `open()` 返回 -1，`errno = EBUSY` |

---

### 6. 原代码中存在的 Bug 分析

> 本实验的原代码（教程提供的版本）存在以下问题，学习时需要注意，实际生产代码应当修正。

### 6.1 Bug ①：`copy_from_user` 返回值检查错误（led_write）

```c
// atomic.c 第76行
ret = copy_from_user(databuf, buf, count);
if (ret < 0) {        // ❌ copy_from_user 返回 unsigned long，永不小于 0
    return -EINVAL;
}
```

**问题**：`copy_from_user` 返回的是"未成功拷贝的字节数"（`unsigned long`），成功返回 `0`，失败返回 `>0`。**永远不返回负数**。`if (ret < 0)` 条件永远为假。

**修复**：`if (ret < 0)` → `if (ret)`

### 6.2 Bug ②：`led_init()` 中 `class_create`/`device_create` 失败时直接 return 无清理

```c
// 第125-128行
gpioled.class = class_create(THIS_MODULE, GPIOLED_NAME);
if (IS_ERR(gpioled.class)) {
    return PTR_ERR(gpioled.class);  // ❌ 直接 return！之前申请的 cdev 和设备号没释放！
}

// 第131-134行
gpioled.device = device_create(gpioled.class, NULL, gpioled.devid, NULL, GPIOLED_NAME);
if (IS_ERR(gpioled.device)) {
    return PTR_ERR(gpioled.device);  // ❌ 直接 return！class、cdev、设备号都没释放！
}
```

**问题**：如果 `class_create` 失败，此前 `alloc_chrdev_region` 分配的设备号和 `cdev_add` 注册的 cdev 没有被清理，造成内核资源泄漏。

**修复**：参考 beep.c 的 goto 回滚链，应该写成：

```c
if (IS_ERR(gpioled.class)) {
    ret = PTR_ERR(gpioled.class);
    goto fail_class;          // → 清理 cdev + 设备号
}
if (IS_ERR(gpioled.device)) {
    ret = PTR_ERR(gpioled.device);
    goto fail_device;         // → 清理 class + cdev + 设备号
}
```

### 6.3 Bug ③：`led_init()` goto 链清理范围不足

```c
fail_setoutput:
    gpio_free(gpioled.led_gpio);           // 只释放 GPIO
fail_findnode:
    return ret;                             // 什么都没清理！
```

**问题**：`fail_findnode` 被 `of_find_node_by_path`、`of_get_named_gpio`、`gpio_request` 三处失败共用，但它不清理 device、class、cdev、设备号。这意味着从这些点失败返回时，之前注册的资源全部泄漏。

### 6.4 Bug ④：`led_exit()` 资源释放顺序错误

```c
static void __exit led_exit(void)
{
    gpio_set_value(gpioled.led_gpio, 1);           // ① 关 LED

    cdev_del(&gpioled.cdev);                       // ② 删 cdev  ← 太早！
    unregister_chrdev_region(gpioled.devid, ...);  // ③ 注销设备号 ← 太早！

    device_destroy(gpioled.class, gpioled.devid);  // ④ 删设备节点
    class_destroy(gpioled.class);                  // ⑤ 删类

    gpio_free(gpioled.led_gpio);                   // ⑥ 释放 GPIO
}
```

**问题**：init 中资源的申请顺序是：设备号 → cdev → class → device → GPIO。exit 中释放应该严格逆序。但原代码把 `cdev_del` 和 `unregister` 放到了 `device_destroy` 和 `class_destroy` 之前。

**正确的顺序**（与 beep.c 一致）：

```c
gpio_set_value(gpioled.led_gpio, 1);              // ① 关硬件
gpio_free(gpioled.led_gpio);                       // ② 释放 GPIO
device_destroy(gpioled.class, gpioled.devid);      // ③ 销毁设备节点
class_destroy(gpioled.class);                      // ④ 销毁类
cdev_del(&gpioled.cdev);                           // ⑤ 删除 cdev
unregister_chrdev_region(gpioled.devid, ...);      // ⑥ 注销设备号
```

### 6.5 Bug ⑤：`cdev.owner` 在 `cdev_init` 之前设置被覆盖

```c
// 第118-119行
gpioled.cdev.owner = THIS_MODULE;   // ← 这行赋值会被下面这行清零覆盖
cdev_init(&gpioled.cdev, &led_fops); // cdev_init 内部执行 memset(cdev, 0, ...)
```

**修复**：把 `.owner` 赋值移到 `cdev_init` 之后。

### 6.6 Bug 汇总表

| # | 位置 | 严重程度 | 问题 |
|---|------|---------|------|
| ① | led_write 第76行 | **严重** | `if(ret < 0)` 永远不会为真，错误检查完全失效 |
| ② | led_init 第127行 | **严重** | class_create/device_create 失败直接 return，资源泄漏 |
| ③ | led_init goto 标签 | 中等 | 标签只清理 GPIO，未覆盖 device/class/cdev/设备号 |
| ④ | led_exit 第184-191行 | 中等 | 资源释放顺序与申请顺序不一致 |
| ⑤ | led_init 第118行 | 低 | cdev.owner 在 cdev_init 前赋值，被 memset 覆盖 |

> **说明**：这些 Bug 不影响本实验的核心目的（验证原子操作），但体现了"功能正确"和"工程正确"之间的差距。

---

### 7. 7_beep vs 8_atomic 对比

### 7.1 代码结构对比

| 对比维度 | 7_beep（蜂鸣器） | 8_atomic（原子LED） | 差异 |
|----------|-----------------|---------------------|------|
| 头文件数量 | 14 个 | **15 个**（多了 atomic.h） | +1 |
| 设备结构体字段 | 8 个 | **9 个**（多了 atomic_t lock） | +1 |
| `open` 函数 | 只做 private_data 绑定 | **+ 原子锁检查（4行）** | 核心变化 |
| `release` 函数 | 空函数 | **+ atomic_inc 释放锁（1行）** | 核心变化 |
| `write` 函数 | copy_from_user + gpio_set_value | 完全相同 | 无差异 |
| 设备树节点 | `"/beep"` / `"beep-gpios"` | `"/gpioled"` / `"led-gpios"` | 仅命名不同 |
| 初始化额外步骤 | 无 | **+ atomic_set 在最前面** | 必须最先执行 |
| APP 端 | 立即 open→write→close | **+ 25秒占用循环** | 验证并发 |

### 7.2 核心发现

```
原子操作引入的改动非常小，集中在 3 个地方：

  1. 结构体：多加一个 atomic_t lock
  2. open：  开头加抢锁逻辑（4行代码）
  3. release：加释放锁（1行 atomic_inc）

就这么点改动，驱动就从"无保护"变成"互斥访问"！

这体现了 Linux 内核 API 设计的优雅——并发保护是"叠上去"的，不改变原有的 GPIO/字符设备代码。
```

---

### 8. Makefile 解析

```makefile
KERNELDIR := /home/zzk/linux/IMX6ULL/linux/linux-imx-rel_imx_4.1.15_2.1.0_ga_alientek
# ↑ 内核源码树路径（正点原子 IMX6ULL 开发板的内核）

CURRENT_PATH := $(shell pwd)        # 当前目录路径
obj-m := atomic.o                   # ★ 目标：编译 atomic.o → atomic.ko

build: kernel_modules               # 默认目标

kernel_modules:
    $(MAKE) -C $(KERNELDIR) M=$(CURRENT_PATH) modules
    #        ↑ 进入内核源码树        ↑ 模块源码在当前目录

clean:
    $(MAKE) -C $(KERNELDIR) M=$(CURRENT_PATH) clean
```

| 语法 | 含义 |
|------|------|
| `obj-m := atomic.o` | 声明 atomic 为**模块**（m=module）。`obj-y` 则是编译进内核 |
| `-C $(KERNELDIR)` | 切换到内核源码目录执行 make |
| `M=$(CURRENT_PATH)` | 告诉内核构建系统：模块代码在 M 指定的目录 |
| `modules` | make 目标：编译内核模块 |

> 与实验6/7的 Makefile 完全一样，仅 `obj-m` 的值从 `beep.o` 变成 `atomic.o`。

---

### 9. 关键知识点总结

### 9.1 本实验新增必须掌握的 8 个知识点

| # | 知识点 | 属于 | 说明 |
|---|--------|------|------|
| 1 | **竞态条件** | 并发基础 | 多个进程同时访问共享资源导致的不可预测结果 |
| 2 | **原子操作** | 并发基础 | 不可打断的"读-改-写"操作 |
| 3 | `atomic_t` | 内核API | 原子变量类型（底层是 int，但必须通过原子函数访问） |
| 4 | `atomic_set(&v, val)` | 内核API | 初始化原子变量为指定值 |
| 5 | `atomic_dec_and_test(&v)` | **★核心★** | 减1并测试是否为0——实现"抢锁"的关键函数 |
| 6 | `atomic_inc(&v)` | 内核API | 加1——释放锁 / 恢复锁值 |
| 7 | `-EBUSY` | 错误码 | 告诉用户"设备忙"，上层 errno=16 |
| 8 | ARM LDREX/STREX | 硬件原理 | 独占加载/存储指令，原子操作的硬件基础 |

### 9.2 本实验巩固的已有知识点

| # | 知识点 | 来自实验 |
|---|--------|---------|
| 1 | 字符设备驱动框架（alloc_chrdev/cdev_init_add/class_create/device_create） | 实验3 |
| 2 | 设备树节点查找 of_find_node_by_path + GPIO 解析 of_get_named_gpio | 实验5/6 |
| 3 | GPIO 子系统 API（gpio_request → gpio_direction_output → gpio_set_value） | 实验6 |
| 4 | copy_from_user 用户态→内核态安全拷贝 | 实验1~7 |
| 5 | filp->private_data 驱动上下文传递的机制 | 实验1~7 |

### 9.3 原子操作 vs 后续并发机制（前瞻）

```
实验8   atomic_t          原子操作       ← 你现在的位置 [最轻量级]
实验9   spinlock          自旋锁         ← 忙等待（while循环），适合极短临界区
实验10  semaphore         信号量         ← 可休眠，适合长临界区
实验11  mutex             互斥锁         ← 最常用，带 owner 检查，不允许嵌套

                         复杂度和开销递增 →
                        （但使用场景也越来越广泛）
```

### 9.4 驱动开发套路（更新版 7 步）

```
Linux 字符设备驱动开发的 7 步套路:

  ┌─ 步骤1: 定义设备结构体
  │   （加入并发保护字段：atomic_t lock / struct mutex lock 等）
  │
  ├─ 步骤2: 实现 file_operations
  │   （open → ★抢锁 + 绑定 private_data
  │    write/read → copy_from/to_user + 硬件操作
  │    release → ★释放锁）
  │
  ├─ 步骤3: 实现 init 函数
  │   （★★ 先初始化锁！再 alloc_chrdev_region → cdev → class → device → gpio）
  │
  ├─ 步骤4: 实现 exit 函数
  │   （★★ 严格逆序释放：gpio → device → class → cdev → devid）
  │
  ├─ 步骤5: module_init/exit + MODULE_LICENSE
  │
  ├─ 步骤6: 写 Makefile
  │
  └─ 步骤7: 写测试 APP（模拟并发/长时间占用，验证锁是否生效）
```

---

### 10. 驱动执行完整时序图

```
时间 ────────────────────────────────────────────────────────────→

【模块加载】

  insmod atomic.ko
         │
         ▼  led_init()
              ├── atomic_set(&lock, 1)              锁 = 可用
              ├── alloc_chrdev_region()              分配设备号
              ├── cdev_init() + cdev_add()           注册 cdev
              ├── class_create("gpioled")            创建 /sys/class/gpioled/
              ├── device_create()                    创建 /dev/gpioled
              ├── of_find_node_by_path("/gpioled")   查找设备树节点
              ├── of_get_named_gpio(nd, "led-gpios", 0) 解析 GPIO
              ├── gpio_request() + gpio_direction_output()  申请+配置
              ├── gpio_set_value(gpio, 0)            LED 亮（验证硬件）
              └── return 0                           加载成功！


【单用户场景】 ./atomicAPP /dev/gpioled 1

  用户程序                          内核驱动
  ────────                        ──────────
  open("/dev/gpioled")      ──→ led_open()
                                   atomic_dec_and_test(lock): 1→0 ✓
                                 ← return 0 (成功)
                                 
  write(fd, [1], 1)          ──→ led_write()
                                   copy_from_user([1], ...) → databuf[0]=1
                                   gpio_set_value(gpio, 0) → LED 亮
                                 ← return 0
                                 
  sleep(5)×5 = 25秒...           （硬件保持 LED 亮）
  
  close(fd)                  ──→ led_release()
                                   atomic_inc(lock): 0→1 释放
                                 ← return 0


【并发冲突场景】

  App A:                            App B:
    │                                 │
    ├─ open()                         │
    │   lock: 1→0, 成功!              │
    │                                 │
    ├─ write()  LED 亮               ├─ open()
    │                                 │   lock: 0→-1, 失败!
    │                                 │   atomic_inc: -1→0 恢复
    │                                 │   return -EBUSY
    │                                 │   → "open failed!"
    │                                 │
    ├─ sleep...（占用中）              │   (App B 等待或退出)
    │                                 │
    ├─ close()                        │
    │   lock: 0→1 释放!               │
    │                                 ├─ 再次 open()
    │                                 │   lock: 1→0, 成功! ✓
    │                                 ├─ write()
    │                                 └─ close()


【模块卸载】

  rmmod atomic.ko
         │
         ▼  led_exit()
              ├── gpio_set_value(gpio, 1)            关 LED
              ├── gpio_free(gpio)                     释放 GPIO
              ├── device_destroy(class, devid)        删除 /dev/gpioled
              ├── class_destroy(class)                删除 /sys/class/gpioled/
              ├── cdev_del(&gpioled.cdev)             删除 cdev
              └── unregister_chrdev_region(devid, 1)  注销设备号
```

---

> **学习建议**：
> 1. 在开发板上实际跑一下两个终端的并发实验，亲眼看到 `-EBUSY` 的效果
> 2. 对比 `atomic_dec_and_test` 和 `#if 0` 中被禁用的旧写法，理解"为什么必须是原子操作"
> 3. 手写一遍 `led_open` 中的抢锁逻辑，特别注意"没抢到要恢复值"这个细节
> 4. 思考：如果只调用 `atomic_dec`（不 test），驱动还能实现互斥吗？（答案：不能，因为永远无法知道锁是否被抢到）
> 5. 准备进入实验9：自旋锁 —— 原子操作的"忙等待"升级版

---

*文档结合代码实际运行逻辑分析生成，知识点基于正点原子阿尔法Linux开发板驱动开发篇视频教程 8_atomic 实验。*

---

## 第九章 自旋锁（Spinlock）

---

### 一、实验概述

本实验通过 GPIO LED 字符设备驱动，演示 **自旋锁（spinlock）** 在内核驱动中保护共享资源（`dev_status`，设备使用标记）的用法，防止多进程并发打开设备时的竞态条件（Race Condition）。

**配套对比实验：**

| 实验编号 | 实验名称 | 并发保护机制 | 核心 API |
|---------|---------|-------------|---------|
| 6 | gpioled | ❌ 无保护 | 无 |
| 8 | atomic | 原子操作 | `atomic_dec_and_test` / `atomic_inc` |
| **9** | **spinlock** | **自旋锁** | **`spin_lock_irqsave` / `spin_unlock_irqrestore`** |
| 10 | semaphore | 信号量 | `down` / `up` |
| 11 | mutex | 互斥体 | `mutex_lock` / `mutex_unlock` |

---

### 二、源代码逐函数分析

### 设备结构体（第 24-36 行）

```c
struct gpioled_dev{
    dev_t devid;            // 设备号（主+次设备号合并）
    int major;              // 主设备号
    int minor;              // 次设备号
    struct cdev cdev;       // 内核字符设备结构体
    struct class *class;    // 设备类指针 → /sys/class/gpioled
    struct device *device;  // 设备实例指针 → /dev/gpioled
    struct device_node *nd; // 设备树节点指针
    int led_gpio;           // LED 对应 GPIO 编号

    int dev_status;         // ★ 被保护资源：0=设备空闲可用，>0=已被占用
    spinlock_t lock;        // ★ 自旋锁：保护 dev_status 的并发访问
};
```

**关键变化（相比实验6 gpioled）：**
- 新增 `int dev_status`：设备是否被占用的标志
- 新增 `spinlock_t lock`：自旋锁变量

---

### 打开函数 `led_open()`（第 40-58 行）

```c
static int led_open(struct inode *inode, struct file *filp)
{
    unsigned long irqflag;               // ★ 用于保存中断状态

    filp->private_data = &gpioled;       // 将设备指针存入文件私有数据

    // ★ spin_lock_irqsave: 三步合一
    //   ① 保存当前 CPU 的中断状态到 irqflag
    //   ② 关闭当前 CPU 的中断（防止中断处理程序也尝试获取同一把锁 → 死锁）
    //   ③ 获取自旋锁（如果锁已被占用，则在此"自旋"忙等）
    spin_lock_irqsave(&gpioled.lock, irqflag);

    if(gpioled.dev_status) {             // 设备已被占用？
        spin_unlock(&gpioled.lock);      // ★ Bug: 应使用 spin_unlock_irqrestore
        return -EBUSY;                   // 返回"设备忙"
    }

    gpioled.dev_status++;                // 标记设备被使用
    // ★ 为什么用 spin_unlock_irqrestore 而不是 spin_unlock？
    //   因为它会恢复之前保存的中断状态，而不仅仅是开中断
    spin_unlock_irqrestore(&gpioled.lock, irqflag);
//自旋锁保护的只是在进行status状态判断的时候不被人打扰，但判断后这个unlock的地方就释放锁了在下边//程序运行的过程中锁都没作用，是status的状态作用的。
    return 0;
}
```

**执行流程：**
```
进程调用 open()
    │
    ▼
spin_lock_irqsave(&lock, irqflag)
    ├── 保存 CPU 中断状态 → irqflag
    ├── 关闭本地 CPU 中断
    ├── 尝试获取锁：
    │   ├── 锁空闲 → 获取成功，继续
    │   └── 锁被占 → 忙等（自旋），直到锁释放
    ▼
检查 dev_status：
    ├── dev_status != 0 → 设备已被占用
    │   ├── spin_unlock(&lock)  [Bug: 未恢复中断]
    │   └── return -EBUSY
    └── dev_status == 0 → 设备空闲
        ├── dev_status++（标记占用）
        ├── spin_unlock_irqrestore(&lock, irqflag)  恢复锁+中断
        └── return 0（成功）
```

**关键知识点：**

1. **为什么用 `spin_lock_irqsave` 而不是 `spin_lock`？**
   - `spin_lock`：只获取锁，不关中断。如果中断处理程序也尝试获取同一把锁 → **死锁**（当前 CPU 持有锁，中断来了，中断处理函数等待锁，但持有锁的上下文被中断打断了，永远无法释放锁）
   - `spin_lock_irqsave`：在获取锁的同时保存并关闭本地中断，防止中断处理程序打断持锁临界区
   - `spin_lock_irqrestore`：释放锁并恢复中断状态（不是无条件开中断！如果之前中断就是关的，恢复后仍保持关）

2. **Bug 分析（第 48 行）：** 错误路径中用了 `spin_unlock` 而不是 `spin_unlock_irqrestore`
   - 进入时通过 `spin_lock_irqsave` 关了中断
   - 出错返回时用 `spin_unlock` 只释放了锁，**没有恢复中断状态**
   - 导致中断被永久关闭 → 系统可能"假死"

---

### 释放函数 `led_release()`（第 60-74 行）

```c
static int led_release(struct inode *inode, struct file *filp)
{
    unsigned long irqflag;
    struct gpioled_dev *dev = filp->private_data;

    spin_lock_irqsave(&dev->lock, irqflag);   // 加锁 + 关中断
    if(dev->dev_status) {
        dev->dev_status--;                    // 标记设备可用
    }
    spin_unlock_irqrestore(&dev->lock, irqflag); // 解锁 + 恢复中断

    return 0;
}
```

**为什么这里也需要加锁？**
`dev_status--` 不是原子的（读-改-写三步），在多核系统中如果两个 CPU 同时执行 release，可能产生竞态。加自旋锁保证操作的原子性。

---

### 写函数 `led_write()`（第 76-95 行）

```c
static ssize_t led_write(struct file *filp, const char __user *buf,
                         size_t count, loff_t *ppos)
{
    int ret;
    unsigned char databuf[1];
    struct gpioled_dev *dev = filp->private_data;

    ret = copy_from_user(databuf, buf, count);   // 从用户空间拷贝数据
    if(ret < 0) {
        return -EINVAL;
    }

    if(databuf[0] == LEDON) {
        gpio_set_value(dev->led_gpio, 0);         // 低电平 → LED 亮
    } else if(databuf[0] == LEDOFF) {
        gpio_set_value(dev->led_gpio, 1);         // 高电平 → LED 灭
    }

    return 0;
}
```

**注意：** `led_write` 中没有加锁！因为 GPIOLED 是单实例设备，已经在 `open` 中通过 `dev_status` 实现了互斥——能成功 open 才能 write，不需要额外保护。

**Bug 注意：** `copy_from_user` 永远返回 ≥0 的值（未成功拷贝的字节数），不会返回负数。用 `if(ret < 0)` 是错误判断，应为 `if(ret != 0)`。

---

### 驱动入口 `led_init()`（第 106-184 行）

```c
static int __init led_init(void)
{
    /* ★ 初始化自旋锁（必须在使用前初始化！） */
    spin_lock_init(&gpioled.lock);
    gpioled.dev_status = 0;                // 设备初始空闲

    // ===== 字符设备框架 =====
    // 1. 注册设备号（动态分配）
    // 2. 初始化 cdev
    // 3. 添加 cdev 到内核
    // 4. 创建设备类 → /sys/class/gpioled
    // 5. 创建设备实例 → /dev/gpioled

    // ===== 硬件初始化 =====
    // 6. 获取设备树节点 /gpioled
    // 7. 获取 GPIO 编号
    // 8. 申请 GPIO
    // 9. 设置 GPIO 为输出
    // 10. 输出低电平点亮 LED
}
```

**关键：`spin_lock_init(&gpioled.lock)`**
- 必须在使用自旋锁之前调用
- 初始化自旋锁结构体内部状态为"未锁定"
- 这是宏/内联函数，不是运行时分配，只是置初值

---

### 驱动出口 `led_exit()`（第 187-201 行）

```c
static void __exit led_exit(void)
{
    gpio_set_value(gpioled.led_gpio, 1);    // 关灯
    // 释放字符设备框架资源
    cdev_del(&gpioled.cdev);
    unregister_chrdev_region(...);
    device_destroy(...);
    class_destroy(...);
    gpio_free(gpioled.led_gpio);            // 释放 GPIO
}
```

**注意：** 自旋锁不需要"销毁"操作，因为它在静态内存中，随模块卸载自动释放。

---

### 三、测试程序 `spinlockAPP.c` 分析

```c
int main(int argc, char *argv[])
{
    fd = open(filename, O_RDWR);    // 打开设备 → 触发 led_open → 获取自旋锁
    databuf[0] = atoi(argv[2]);     // 解析控制命令
    write(fd, databuf, sizeof(databuf)); // 控制LED

    // ★ 模拟占用25秒，测试互斥效果
    while(1) {
        sleep(5);
        cnt++;
        printf("App Runing times:%d\r\n", cnt);
        if(cnt >= 5) break;
    }

    close(fd);  // 关闭设备 → 触发 led_release → 释放自旋锁
    return 0;
}
```

**测试方法（验证自旋锁互斥）：**
```
终端1: ./spinlockAPP /dev/gpioled 1 &
       → 后台运行，占用驱动 25 秒

终端2: ./spinlockAPP /dev/gpioled 0
       → open() 返回 -1 (errno=EBUSY)，打印 "file open failed!"
       → 因为 dev_status=1，自旋锁保护的检查失败

25秒后终端1退出 → 终端2再次运行 → 成功
```

---

### 四、核心知识点 —— 自旋锁

### 什么是自旋锁？

自旋锁（spinlock）是 Linux 内核中最基础的锁机制：

- **"自旋"** = 当锁被占用时，请求者**不睡眠**，而是在 CPU 上循环忙等（busy-wait）
- **适用场景**：临界区极短（微秒级），不能在临界区中睡眠
- **不适用场景**：临界区时间长（毫秒级以上），会导致 CPU 空转浪费

### 自旋锁 API 族

| API | 说明 | 使用场景 |
|-----|------|---------|
| `spin_lock_init(&lock)` | 初始化自旋锁 | 驱动加载时 |
| `spin_lock(&lock)` | 获取锁（忙等） | 确定中断不会竞争此锁 |
| `spin_unlock(&lock)` | 释放锁 | 对应 spin_lock |
| `spin_lock_irq(&lock)` | 关本地中断 + 获取锁 | 中断可能竞争此锁（不知道中断原来状态） |
| `spin_unlock_irq(&lock)` | 释放锁 + 开本地中断 | 对应 spin_lock_irq |
| `spin_lock_irqsave(&lock, flags)` | 保存中断状态 + 关中断 + 获取锁 | ★ 推荐：最安全的方式 |
| `spin_unlock_irqrestore(&lock, flags)` | 释放锁 + 恢复中断状态 | 对应 spin_lock_irqsave |
| `spin_lock_bh(&lock)` | 关 Bottom Half + 获取锁 | 与 BH 竞争时使用 |
| `spin_unlock_bh(&lock)` | 释放锁 + 开 Bottom Half | 对应 spin_lock_bh |

### 为什么推荐 irqsave 版本？

```
场景：你不知道调用上下文的中断状态

spin_lock_irq:
    ├── 无条件关中断
    └── 无条件开中断  ← 问题！如果调用者本身就关了中断，你强行打开会破坏调用者的假设

spin_lock_irqsave:
    ├── 保存当前中断状态
    └── 恢复时照原样恢复  ← 正确！不破坏调用者的上下文
```

### 自旋锁 vs 信号量 vs 互斥体（核心对比）

| 特性 | 自旋锁 spinlock | 信号量 semaphore | 互斥体 mutex |
|------|:--------------:|:---------------:|:-----------:|
| 等待方式 | **忙等（自旋）** | **睡眠** | **睡眠** |
| 临界区能做睡眠操作？ | ❌ 禁止 | ✅ 允许 | ✅ 允许 |
| 适合临界区长度 | 极短（< 几μs） | 较长（ms 级） | 较长（ms 级） |
| 中断上下文能用？ | ✅ 可以 | ❌ 不可以 | ❌ 不可以 |
| 持有锁时内核可抢占？ | 禁止抢占 | 可以抢占 | 可以抢占 |
| 能否递归获取？ | ❌ 死锁 | ❌ 死锁 | ❌ 死锁（Linux mutex） |
| 开销 | 低（几个 CPU 指令） | 高（上下文切换） | 中（优化过的睡眠锁） |
| 锁持有时间 | ns~μs 级 | ms~s 级 | ms~s 级 |

### 自旋锁使用规则（面试必考）

1. **临界区必须短**：持有锁的时间越短越好，最好在几微秒内
2. **临界区内不能睡眠**：不能调用 `copy_from_user`、`kmalloc(GFP_KERNEL)`、`schedule()` 等可能睡眠的函数
3. **临界区内不能调用同类锁**：持有一个自旋锁时不能再获取同一个锁 → 死锁
4. **加锁顺序要一致**：如果代码中有多把锁，获取顺序必须全局一致 → 防止 ABBA 死锁
5. **推荐使用 `spin_lock_irqsave`** 而非 `spin_lock`（防止中断竞争该锁）
6. **锁持有期间禁止调用 `schedule()`**：持有自旋锁时内核抢占被禁止

### 死锁场景分析

```
【场景1：中断上下文死锁】
  CPU0:
    spin_lock(&lock)          ← 获取锁成功
    >>> 中断发生 <<<
    中断处理函数:
      spin_lock(&lock)        ← 同一个锁！CPU0 已经持有，等它释放
                               ← 但 CPU0 被中断打断，无法继续执行
                               ← ★ 死锁！

  解决方案：用 spin_lock_irqsave 在获取锁之前关中断

【场景2：ABBA 死锁】
  CPU0: spin_lock(A) → spin_lock(B)   ← 先A后B
  CPU1: spin_lock(B) → spin_lock(A)   ← 先B后A
  → 互相等待对方释放 → ★ 死锁！

  解决方案：所有代码按相同顺序获取锁
```

---

### 五、驱动执行流程全景图

```
模块加载 (insmod spinlock.ko)
│
├─ led_init()
│   ├─ spin_lock_init(&gpioled.lock)        # 初始化自旋锁
│   ├─ gpioled.dev_status = 0               # 设备初始可用
│   ├─ alloc_chrdev_region()                # 分配设备号
│   ├─ cdev_init() + cdev_add()            # 注册字符设备
│   ├─ class_create() + device_create()     # 创建设备文件
│   ├─ of_find_node_by_path("/gpioled")     # 查找设备树节点
│   ├─ of_get_named_gpio()                  # 获取GPIO编号
│   ├─ gpio_request()                       # 申请GPIO
│   ├─ gpio_direction_output(..., 1)        # 设为输出(默认高)
│   └─ gpio_set_value(..., 0)               # 点亮LED
│
用户空间: open("/dev/gpioled", O_RDWR)
│   └─ VFS ───→ led_open()
│       ├─ filp->private_data = &gpioled
│       ├─ spin_lock_irqsave(&lock, irqflag)    # 关中断+获取锁
│       ├─ if (dev_status) → 设备忙？→ unlock → -EBUSY
│       ├─ dev_status++                          # 标记占用
│       ├─ spin_unlock_irqrestore(&lock, irqflag)# 释放锁+恢复中断
│       └─ return 0                              # 成功
│
用户空间: write(fd, buf, 1)
│   └─ VFS ───→ led_write()
│       ├─ copy_from_user(databuf, buf, count)
│       └─ gpio_set_value(led_gpio, 0/1)        # 控制LED
│
用户空间: close(fd)
│   └─ VFS ───→ led_release()
│       ├─ spin_lock_irqsave(&lock, irqflag)
│       ├─ dev_status--                          # 释放设备
│       ├─ spin_unlock_irqrestore(&lock, irqflag)
│       └─ return 0
│
模块卸载 (rmmod spinlock)
└─ led_exit()
    ├─ gpio_set_value(..., 1)                # 关LED
    ├─ cdev_del()                            # 删除cdev
    ├─ unregister_chrdev_region()            # 注销设备号
    ├─ device_destroy()                      # 销毁设备
    ├─ class_destroy()                       # 销毁类
    └─ gpio_free()                           # 释放GPIO
```

---

### 六、并行实验对比总表

| 维度 | 实验6 gpioled | 实验8 atomic | **实验9 spinlock** | 实验10 semaphore | 实验11 mutex |
|------|:-----------:|:----------:|:---------------:|:--------------:|:----------:|
| **保护机制** | ❌ 无 | 原子变量 | **自旋锁** | 信号量 | 互斥体 |
| **保护对象** | — | lock (atomic_t) | **dev_status (int)** | sem (信号量自身) | lock (mutex) |
| **等待方式** | — | 不等待(直接返回) | **忙等(自旋)** | 睡眠等待 | 睡眠等待 |
| **可多个进程同时打开？** | ✅ 是 | ❌ 否 | **❌ 否** | ❌ 否 | ❌ 否 |
| **临界区能睡眠？** | — | — | **❌ 不可以** | ✅ 可以 | ✅ 可以 |
| **中断上下文可用？** | — | ✅ 可以 | **✅ 可以** | ❌ 不可以 | ❌ 不可以 |
| **open 失败返回** | 不失败 | -EBUSY | **-EBUSY** | 阻塞(睡眠) | 阻塞(睡眠) |
| **资源占用模式** | 无限制 | 1个进程 | **1个进程** | 1个进程(初始化1) | 1个进程 |
| **核心初始化** | 无 | atomic_set(&lock, 1) | **spin_lock_init** | sema_init(&sem, 1) | mutex_init(&lock) |
| **获取操作** | 无 | atomic_dec_and_test | **spin_lock_irqsave** | down | mutex_lock |
| **释放操作** | 无 | atomic_inc | **spin_unlock_irqrestore** | up | mutex_unlock |
| **实现复杂度** | 最简单 | 简单 | **中等** | 中等 | 中等 |
| **性能开销** | 无 | 极低 | **低(忙等耗CPU)** | 高(上下文切换) | 中 |
| **使用场景** | 无需保护的场景 | 简单二值互斥 | **极短临界区+中断安全** | 长临界区/计数同步 | 长临界区/互斥 |

---

### 七、本实验代码 Bug 和改进建议

### Bug #1：错误路径未恢复中断
```c
// spinlock.c 第48行
if(gpioled.dev_status) {
    spin_unlock(&gpioled.lock);   // ✗ 应该用 spin_unlock_irqrestore
    return -EBUSY;
}
// 正确写法：
if(gpioled.dev_status) {
    spin_unlock_irqrestore(&gpioled.lock, irqflag);  // ✓
    return -EBUSY;
}
```

### Bug #2：copy_from_user 返回值判断
```c
// spinlock.c 第84行
ret = copy_from_user(databuf, buf, count);
if(ret < 0) {    // ✗ copy_from_user 永远不返回负值！
// 应改为：
if(ret != 0) {   // ✓ 返回未拷贝成功的字节数
```

### 设计思考：本实验自旋锁使用是否合适？

本实验使用自旋锁保护 `dev_status`，实际上对于这种简单的"检查-设置"操作，**实验8的原子操作 `atomic_dec_and_test` 更加合适**：
- 临界区只有一条判断+一条赋值，用自旋锁"杀鸡用牛刀"
- 原子操作开销更低，代码更简洁
- 自旋锁的优势（关中断、忙等保护复杂临界区）在本场景中未体现

**但教学意义明确**：让学生理解自旋锁的完整 API 和使用模式。

---

### 八、必须掌握的知识点清单

1. ✅ 自旋锁的工作原理："忙等"而非睡眠
2. ✅ `spin_lock_init` / `spin_lock` / `spin_unlock` 基本 API
3. ✅ `spin_lock_irqsave` / `spin_unlock_irqrestore` 为什么比 `spin_lock` 更安全
4. ✅ 自旋锁临界区内不能睡眠的原因
5. ✅ 中断上下文死锁的场景和避免方法
6. ✅ 自旋锁 vs 信号量 vs 互斥体的区别（面试高频）
7. ✅ 什么时候用自旋锁？什么时候用信号量？
8. ✅ `copy_from_user` 的返回值含义（不是 errno 负数！）
9. ✅ Linux 字符设备驱动的标准框架
10. ✅ 设备树 GPIO 的获取和使用流程

---

## 第十章 信号量（Semaphore）

---

### 一、实验概述

本实验通过 GPIO LED 字符设备驱动，演示 **信号量（semaphore）** 在内核驱动中实现设备互斥访问的用法。信号量初始化为 1（二值信号量），`down()` 操作用于获取信号量（如果为 0 则进程**睡眠等待**），`up()` 操作用于释放信号量并唤醒等待者。

**配套对比实验：**
| 实验编号 | 实验名称 | 并发保护机制 | 核心 API |
|---------|---------|-------------|---------|
| 6 | gpioled | ❌ 无保护 | 无 |
| 8 | atomic | 原子操作 | `atomic_dec_and_test` / `atomic_inc` |
| 9 | spinlock | 自旋锁 | `spin_lock_irqsave` / `spin_unlock_irqrestore` |
| **10** | **semaphore** | **信号量** | **`down` / `up`** |
| 11 | mutex | 互斥体 | `mutex_lock` / `mutex_unlock` |

---

### 二、源代码逐函数分析

### 设备结构体（第 24-35 行）

```c
struct gpioled_dev{
    dev_t devid;            // 设备号（主+次设备号合并）
    int major;              // 主设备号
    int minor;              // 次设备号
    struct cdev cdev;       // 内核字符设备结构体
    struct class *class;    // 设备类指针 → /sys/class/gpioled
    struct device *device;  // 设备实例指针 → /dev/gpioled
    struct device_node *nd; // 设备树节点指针
    int led_gpio;           // LED 对应 GPIO 编号

    struct semaphore sem;   // ★ 信号量：代替实验9的 dev_status + spinlock
                            //   初始化为 1 → 相当于二值信号量（互斥锁）
};
```

**关键变化（相比实验9 spinlock）：**
- **删除**了 `int dev_status`（设备使用标记）
- **删除**了 `spinlock_t lock`（自旋锁）
- **新增** `struct semaphore sem`：一个信号量搞定所有同步！

**为什么更简洁？**
- 信号量内部已经包含了"计数器 + 等待队列 + 自旋锁保护"
- 不再需要手动保护 `dev_status`，信号量本身就提供了完整的并发控制

---

### 打开函数 `led_open()`（第 39-46 行）

```c
static int led_open(struct inode *inode, struct file *filp)
{
    filp->private_data = &gpioled;   // 将设备指针存入文件私有数据

    /*
     * ★ down()：获取信号量（P 操作 / 荷兰语 Proberen = 尝试）
     *
     * 内部执行流程（原子性由信号量内部自旋锁保证）：
     *   1. 信号量计数器 sem.count 减 1
     *   2. 判断 count 是否 >= 0：
     *      - 如果 >= 0（原值 > 0，即有空闲资源）：立即返回，进程继续执行
     *      - 如果 < 0（原值 = 0，即无空闲资源）：
     *        a. 将当前进程加入信号量的等待队列
     *        b. 设置进程状态为 TASK_UNINTERRUPTIBLE（不可中断睡眠）
     *        c. 调用 schedule() 让出 CPU，触发进程切换
     *        d. 被唤醒后，重新尝试获取信号量
     *
     * 关键区别（vs 自旋锁）：
     *   - 自旋锁：锁被占用时 CPU 空转忙等（不释放 CPU）
     *   - 信号量：信号量为 0 时进程睡眠让出 CPU（其他进程可以运行）
     */
    down(&gpioled.sem);

    return 0;  // 成功获取信号量 = 成功打开设备
}
```

**`down()` vs `down_interruptible()` vs `down_trylock()`：**

| API | 行为 | 能被信号唤醒？ | 使用场景 |
|-----|------|:----------:|---------|
| `down(&sem)` | 获取信号量，失败则**不可中断睡眠** | ❌ 否 | 用户不想被打断的等待 |
| `down_interruptible(&sem)` | 获取信号量，失败则**可中断睡眠** | ✅ 是 | ★ 推荐！允许 Ctrl+C 终止 |
| `down_trylock(&sem)` | 尝试获取，失败**立即返回** | — | 不想睡眠的场景 |
| `down_timeout(&sem, timeout)` | 获取信号量，**超时**返回 | ✅ 是 | 等待时间有限的场景 |
| `up(&sem)` | 释放信号量（V 操作） | — | 配对的释放操作 |

**为什么本实验用 `down()` 而不是 `down_interruptible()`？**
- 简单起见，但实际项目中 **强烈推荐 `down_interruptible()`**
- `down()` 导致的 `TASK_UNINTERRUPTIBLE` 状态进程无法被 `kill -9` 杀掉！
- 如果驱动有 bug 导致信号量永远不被释放，进程变成"D 状态僵尸"（无法杀死）

---

### 释放函数 `led_release()`（第 48-55 行）

```c
static int led_release(struct inode *inode, struct file *filp)
{
    struct gpioled_dev *dev = filp->private_data;

    /*
     * ★ up()：释放信号量（V 操作 / 荷兰语 Verhogen = 增加）
     *
     * 内部执行流程（原子性由信号量内部自旋锁保证）：
     *   1. 信号量计数器 sem.count 加 1
     *   2. 判断 count 是否 <= 0：
     *      - 如果 <= 0：说明有进程在等待队列中睡眠
     *        → 从等待队列中取出第一个等待进程
     *        → 调用 wake_up_process() 唤醒它
     *      - 如果 > 0：说明没有等待者，直接返回
     *
     * 注意：up() 可以在中断上下文中调用！
     *       这是信号量和互斥体的重要区别之一
     */
    up(&dev->sem);

    return 0;
}
```

**`up()` 可以在中断上下文调用吗？**  ✅ **可以！**
- 信号量的 `up()` 内部使用自旋锁保护，可以在中断上下文中调用
- 但互斥体 `mutex_unlock()` **不可以**在中断上下文中调用

---

### 写函数 `led_write()`（第 57-76 行）

```c
static ssize_t led_write(struct file *filp, const char __user *buf,
                         size_t count, loff_t *ppos)
{
    int ret;
    unsigned char databuf[1];
    struct gpioled_dev *dev = filp->private_data;  // 取回设备指针

    ret = copy_from_user(databuf, buf, count);     // 从用户空间拷贝数据
    if(ret < 0) {                                   // Bug: 应为 ret != 0
        return -EINVAL;
    }

    if(databuf[0] == LEDON) {
        gpio_set_value(dev->led_gpio, 0);            // 低电平 → LED 亮
    } else if(databuf[0] == LEDOFF) {
        gpio_set_value(dev->led_gpio, 1);            // 高电平 → LED 灭
    }

    return 0;
}
```

**安全性分析：** 不需要在 write 中加锁，因为能成功 open 的进程已经持有信号量，保证了互斥访问。

---

### 驱动入口 `led_init()`（第 87-164 行）

```c
static int __init led_init(void)
{
    int ret = 0;

    /*
     * ★ sema_init(&gpioled.sem, 1)：
     *   初始化信号量，计数器初始值 = 1
     *
     * 初始值为 1 的含义：
     *   - sem.count = 1 → 有 1 个"资源"可用
     *   - 第1个进程 down() → count 变为 0 → 成功获取
     *   - 第2个进程 down() → count 变为 -1 → 进入睡眠等待
     *   - 第1个进程 up()   → count 变为 0 → 唤醒等待者
     *
     * 如果初始化为 0：
     *   - sem.count = 0 → 所有 down() 都阻塞
     *   - 适用于"等待某个事件发生后再唤醒"的同步场景
     *
     * 如果初始化为 N（N > 1）：
     *   - 相当于有 N 个"资源"，前 N 个 down() 都成功
     *   - 适用于限制同时访问数量的场景
     */
    sema_init(&gpioled.sem, 1);

    // ===== 字符设备框架（与实验9完全相同）=====
    // 1. 注册设备号（动态分配）
    // 2. 初始化 cdev + 绑定 file_operations
    // 3. 添加 cdev 到内核
    // 4. 创建设备类 → /sys/class/gpioled
    // 5. 创建设备实例 → /dev/gpioled

    // ===== 硬件初始化（与实验9完全相同）=====
    // 6. 获取设备树节点 /gpioled
    // 7. 获取 GPIO 编号
    // 8. 申请 GPIO
    // 9. 设置 GPIO 为输出（默认高电平）
    // 10. 输出低电平点亮 LED
}
```

**信号量初始化 API 族：**
```c
// 方式1: 运行时初始化（本实验使用）
void sema_init(struct semaphore *sem, int val);

// 方式2: 静态定义 + 初始化（编译时）
static DECLARE_SEMAPHORE_GENERIC(name, val);

// 方式3: 互斥信号量（初始值=1 的快捷方式）
static DEFINE_SEMAPHORE(name);  // 等价于 sema_init(&name, 1)
```

---

### 三、信号量核心知识

### 什么是信号量？

信号量（Semaphore）是 Dijkstra 在 1965 年发明的同步原语：

```
概念模型：
  struct semaphore {
      int count;           // 计数器（表示可用资源数量）
      wait_queue_head_t wait;  // 等待队列（睡眠进程链表）
  };

规则：
  - count >= 0：有 count 个资源可用，没有进程在等待
  - count < 0： 没有资源可用，有 |count| 个进程在等待
```

**P 操作（Proberen = 尝试 / Linux 的 down）：**
```
count--;
if (count < 0) {
    加入等待队列;
    睡眠;
}
```

**V 操作（Verhogen = 增加 / Linux 的 up）：**
```
count++;
if (count <= 0) {  // 有等待者
    唤醒等待队列中的第一个进程;
}
```

### 二值信号量 vs 计数信号量

| 类型 | 初始值 | 行为 | 类比 |
|------|:-----:|------|------|
| **二值信号量** | 1 | 只有 0/1 两种状态，相当于互斥锁 | 卫生间门锁（有人/没人） |
| **计数信号量** | N (N>1) | 允许多个持有者同时访问 | 停车场有 N 个车位 |

本实验是**二值信号量**（初始值=1），效果等价于互斥锁。

### 信号量持有者可以睡眠！

**这是信号量和自旋锁最本质的区别：**

```c
// ✅ 在持有信号量时可以睡眠！
down(&sem);
copy_from_user(buf, user_buf, size);  // 可能睡眠（缺页异常）
kmalloc(1024, GFP_KERNEL);            // 可能睡眠（内存不足时）
schedule();                           // 主动让出 CPU
up(&sem);

// ❌ 持有自旋锁时绝对不能睡眠！
spin_lock(&lock);
copy_from_user(...);   // 危险！可能睡眠导致内核崩溃
kmalloc(..., GFP_KERNEL); // 危险！
spin_unlock(&lock);
```

### 信号量内部分析

```c
struct semaphore {
    raw_spinlock_t lock;       // ★ 内部使用自旋锁保护 count 和 wait_list 的并发访问
    unsigned int count;        // 可用资源计数
    struct list_head wait_list; // 等待队列（在此睡眠的进程链表）
};
```

- **保护临界数据用自旋锁**（count 和 wait_list 的修改只需几个指令，极短）
- **等待资源用睡眠**（可能等很长时间，不能让 CPU 空转）

这就是"自旋锁保护机制，信号量实现策略"的组合思想。

---

### 四、测试程序 `semaApp.c` 分析

```c
int main(int argc, char *argv[])
{
    fd = open(filename, O_RDWR);    // → led_open → down(&sem)
                                    // 如果信号量已被占用，open() 会阻塞！
                                    // 不像实验9 spinlock 那样立即返回 -EBUSY

    databuf[0] = atoi(argv[2]);     // 解析控制命令
    write(fd, databuf, sizeof(databuf)); // 控制LED

    // ★ 模拟占用25秒
    while(1) {
        sleep(5);
        cnt++;
        printf("App Runing times:%d\r\n", cnt);
        if(cnt >= 5) break;
    }

    close(fd);  // → led_release → up(&sem)
                // 释放信号量，如果有等待者则唤醒
    return 0;
}
```

**测试方法（验证信号量阻塞行为）：**
```
终端1: ./semaApp /dev/gpioled 1 &
       → LED 亮，程序进入 25 秒睡眠循环

终端2: ./semaApp /dev/gpioled 0
       → 卡住！open() 中 down() 阻塞，进程进入睡眠
       → ps aux 看到进程状态为 D (不可中断睡眠)
       → 25秒后终端1退出 → up() 唤醒终端2 → 终端2继续执行，LED灭

终端3: ./semaApp /dev/gpioled 1
       → 同样阻塞，在等待队列中排队
       → 30秒后终端1退出 → 终端2执行完 → 终端3才被唤醒
```

**信号量 vs 自旋锁的测试行为差异：**
| 测试行为 | 实验8 atomic | 实验9 spinlock | **实验10 semaphore** |
|---------|:-----------:|:-------------:|:-----------------:|
| 第二个进程 open | 立即返回 -EBUSY | 立即返回 -EBUSY | **阻塞等待（睡眠）** |
| 进程状态 | 不阻塞，直接失败 | 不阻塞，直接失败 | **D 状态（不可中断睡眠）** |
| Ctrl+C 能否终止？ | — | — | **不能（用了 down，非 interruptible）** |

---

### 五、信号量 vs 其他同步机制（总对比）

### 核心维度对比

| 维度 | 原子操作 atomic | 自旋锁 spinlock | **信号量 semaphore** | 互斥体 mutex |
|------|:-----------:|:-----------:|:----------------:|:--------:|
| **等待方式** | 不等待 | CPU 忙等 | **睡眠** | 睡眠 |
| **临界区能睡眠？** | — | ❌ | **✅** | ✅ |
| **中断上下文可用？** | ✅ | ✅ | **❌ down不行，up可以** | ❌ |
| **持有时可抢占？** | — | ❌ 禁止 | **✅** | ✅ |
| **可同时持有数** | N/A | 1 | **1~N（取决于初值）** | 1 |
| **递归获取** | — | ❌ 死锁 | **❌ 死锁** | ❌ 死锁 |
| **CPU 开销** | 极低 | 低（忙等耗CPU） | **高（上下文切换）** | 中 |
| **锁持有时间** | ns 级 | ns~μs 级 | **ms~s 级** | ms~s 级 |

### 选择决策树

```
需要保护共享资源并发访问？
│
├─ 临界区 < 几微秒？
│   ├─ 可能在中断上下文访问？ → 自旋锁 spinlock
│   └─ 仅在进程上下文？ → 原子操作 atomic（更轻量）
│
├─ 临界区 > 几微秒？可能睡眠？
│   ├─ 只需要互斥（1个持有者）？ → 互斥体 mutex（推荐，有调试支持）
│   ├─ 需要多个持有者（如限制5个进程同时访问）？ → 信号量 semaphore(N)
│   └─ 需要简单的互斥 + 代码简单？ → 信号量 semaphore(1)
│
└─ 不确定？
    → 优先用 mutex（最安全，有 lockdep 死锁检测）
```

---

### 六、驱动执行流程全景图

```
模块加载 (insmod semaphore.ko)
│
├─ led_init()
│   ├─ sema_init(&gpioled.sem, 1)          # ★ 初始化信号量=1（二值信号量）
│   ├─ alloc_chrdev_region()                # 分配设备号
│   ├─ cdev_init() + cdev_add()            # 注册字符设备
│   ├─ class_create() + device_create()     # 创建设备文件
│   ├─ of_find_node_by_path("/gpioled")     # 查找设备树节点
│   ├─ of_get_named_gpio()                  # 获取GPIO编号
│   ├─ gpio_request()                       # 申请GPIO
│   ├─ gpio_direction_output(..., 1)        # 设为输出(默认高)
│   └─ gpio_set_value(..., 0)               # 点亮LED
│
用户空间: open("/dev/gpioled", O_RDWR)
│   └─ VFS ───→ led_open()
│       ├─ filp->private_data = &gpioled
│       └─ ★ down(&gpioled.sem)
│           ├── count: 1→0 → 成功，立即返回
│           └── count: 0→-1 → 进程加入等待队列 → 睡眠等待
│                                    ↑
│                           （等待 up() 唤醒）
│
用户空间: write(fd, buf, 1)
│   └─ VFS ───→ led_write()
│       ├─ copy_from_user(databuf, buf, count)
│       └─ gpio_set_value(led_gpio, 0/1)
│
用户空间: close(fd)
│   └─ VFS ───→ led_release()
│       └─ ★ up(&gpioled.sem)
│           ├── count: 0→1 → 无等待者，直接返回
│           └── count: -1→0 → 有等待者！
│               └── 从等待队列取出第一个进程 → wake_up_process()
│                   └── 被唤醒的进程从 down() 返回，继续执行
│
模块卸载 (rmmod semaphore)
└─ led_exit()
    ├─ gpio_set_value(..., 1) → 关LED
    ├─ cdev_del() + unregister_chrdev_region()
    ├─ device_destroy() + class_destroy()
    └─ gpio_free()
```

---

### 七、本实验的关键改进点

### 设计优势（vs 实验9 spinlock）
1. **代码更简洁**：不需要 `dev_status` + `spinlock` 两个变量，一个 `semaphore` 搞定
2. **不会忙等**：等待者睡眠让出 CPU，不浪费 CPU 资源
3. **临界区更灵活**：持有信号量时可以调用可能睡眠的函数

### 本实验的改进建议
1. **用 `down_interruptible()` 代替 `down()`**：
   ```c
   // 改进版
   if (down_interruptible(&gpioled.sem)) {
       return -ERESTARTSYS;  // 被信号唤醒，返回给用户空间
   }
   // 这样 Ctrl+C 可以终止等待中的进程
   ```

2. **处理 `copy_from_user` 返回值**：
   ```c
   ret = copy_from_user(databuf, buf, count);
   if (ret != 0) {  // 不是 ret < 0！
       return -EFAULT;
   }
   ```

3. **考虑使用 mutex 代替二值信号量**：
   对于初始值=1 的信号量（纯互斥场景），mutex 更合适（更轻量，有调试支持）

---

### 八、必须掌握的知识点清单

1. ✅ 信号量的概念：P(down) / V(up) 操作
2. ✅ 二值信号量 vs 计数信号量
3. ✅ `down` / `down_interruptible` / `down_trylock` 的区别
4. ✅ 信号量持有期间可以睡眠（vs 自旋锁不能睡眠）
5. ✅ `up()` 可以在中断上下文中调用
6. ✅ 信号量内部用自旋锁保护（组合思想）
7. ✅ `TASK_UNINTERRUPTIBLE` vs `TASK_INTERRUPTIBLE` 的进程状态
8. ✅ `sema_init` / `DEFINE_SEMAPHORE` 初始化方式
9. ✅ 信号量等待队列的工作机制
10. ✅ 信号量 vs 自旋锁 vs 互斥体的选择标准

---

## 第十一章 互斥体（Mutex）

---

### 一、实验概述

本实验通过 GPIO LED 字符设备驱动，演示 **互斥体（mutex）** 在内核驱动中实现设备互斥访问的用法。互斥体是 Linux 内核专门为"互斥"场景优化的睡眠锁——初始值为 1 的计数信号量也能实现互斥，但 mutex 更轻量、语义更严格、支持 lockdep 死锁检测。

**配套对比实验：**
| 实验编号 | 实验名称 | 并发保护机制 | 核心 API |
|---------|---------|-------------|---------|
| 6 | gpioled | ❌ 无保护 | 无 |
| 8 | atomic | 原子操作 | `atomic_dec_and_test` / `atomic_inc` |
| 9 | spinlock | 自旋锁 | `spin_lock_irqsave` / `spin_unlock_irqrestore` |
| 10 | semaphore | 信号量 | `down` / `up` |
| **11** | **mutex** | **互斥体** | **`mutex_lock` / `mutex_unlock`** |

---

### 二、源代码逐函数分析

### 设备结构体（第 24-35 行）

```c
struct gpioled_dev{
    dev_t devid;            // 设备号（主+次设备号合并）
    int major;              // 主设备号
    int minor;              // 次设备号
    struct cdev cdev;       // 内核字符设备结构体
    struct class *class;    // 设备类指针 → /sys/class/gpioled
    struct device *device;  // 设备实例指针 → /dev/gpioled
    struct device_node *nd; // 设备树节点指针
    int led_gpio;           // LED 对应 GPIO 编号

    struct mutex lock;      // ★ 互斥体：专门为"互斥"场景优化的睡眠锁
                            //   相当于"加强版的二值信号量"
};
```

**关键变化（相比实验10 semaphore）：**
- **删除**了 `struct semaphore sem`
- **新增** `struct mutex lock`
- 其他一切保持不变！

---

### 打开函数 `led_open()`（第 39-46 行）

```c
static int led_open(struct inode *inode, struct file *filp)
{
    filp->private_data = &gpioled;   // 将设备指针存入文件私有数据

    /*
     * ★ mutex_lock()：获取互斥体
     *
     * 内部执行流程：
     *   1. 如果互斥体未被持有 → 设置 owner 为当前进程 → 立即返回（fastpath）
     *   2. 如果互斥体已被持有 → 进程进入睡眠等待（slowpath）
     *
     * 与 down(&sem) 的区别：
     *   - mutex_lock 有明确的"所有者"概念（struct task_struct *owner）
     *   - semaphore 没有所有者概念——任何进程都可以 up，哪怕不是 down 的那个进程
     *   - mutex 有严格的"谁 lock 谁 unlock"语义——强制配对
     *
     * Mutex 的设计原则：
     *   - 只有获取 mutex 的进程才能释放它
     *   - 内核会做调试检查（如果违反 → 内核 warning）
     */
    mutex_lock(&gpioled.lock);

    return 0;  // 成功获取互斥体 = 成功打开设备
}
```

**`mutex_lock()` 的两个执行路径：**

```
mutex_lock(&lock)
│
├─ 【fastpath】互斥体未被持有
│   └─ 原子性地设置 owner = current，直接返回
│       （这条路径不需要上下文切换，开销极低）
│
└─ 【slowpath】互斥体已被持有
    ├─ 将当前进程加入 mutex 的等待队列
    ├─ 设置进程状态为 TASK_UNINTERRUPTIBLE
    ├─ 调用 schedule() 让出 CPU
    └─ 被唤醒后，获取互斥体，设置 owner，返回
```

**Mutex API 族：**

| API | 行为 | 能被信号唤醒？ | 返回值 |
|-----|------|:----------:|------|
| `mutex_lock(&lock)` | 获取锁，失败**不可中断睡眠** | ❌ | void |
| `mutex_lock_interruptible(&lock)` | 获取锁，失败**可中断睡眠** | ✅ | 0 或 -EINTR |
| `mutex_trylock(&lock)` | 尝试获取，失败立即返回 | — | true/false |
| `mutex_lock_killable(&lock)` | 获取锁，失败可被**致命信号**杀死 | ✅ | 0 或 -EINTR |
| `mutex_unlock(&lock)` | 释放锁，唤醒等待者 | — | void |
| `mutex_is_locked(&lock)` | 检查锁是否被持有 | — | true/false |

**建议：** 用 `mutex_lock_interruptible()` 代替 `mutex_lock()`，让用户可以用 Ctrl+C 终止等待中的进程。

---

### 释放函数 `led_release()`（第 48-55 行）

```c
static int led_release(struct inode *inode, struct file *filp)
{
    struct gpioled_dev *dev = filp->private_data;

    /*
     * ★ mutex_unlock()：释放互斥体
     *
     * 内部执行流程：
     *   1. 验证当前进程确实是 mutex 的 owner（调试检查）
     *   2. 清除 owner 标记
     *   3. 如果有等待者，唤醒等待队列中的第一个进程
     *
     * ★ 重要限制：mutex_unlock 不能在中断上下文中调用！
     *   因为需要操作进程调度（唤醒睡眠进程），而中断上下文没有当前进程的概念。
     *   这一点和 up(&sem) 不同（up 可以在中断上下文中调用）。
     */
    mutex_unlock(&dev->lock);

    return 0;
}
```

**互斥体 vs 信号量的关键区别：**

| 特性 | 信号量 semaphore | 互斥体 mutex |
|------|:--------------:|:----------:|
| **有所有者概念？** | ❌ 没有 | ✅ 有（owner 指针） |
| **谁释放谁获取要一致？** | ❌ 不要求 | **✅ 严格要求** |
| **unlock 可在中断上下文？** | **✅ 可以（up）** | ❌ 不可以 |
| **lockdep 死锁检测？** | ❌ 不支持 | **✅ 支持** |
| **可同时持有多个？** | ✅ 可以（N>1） | ❌ 永远只允许 1 个 |
| **优先级继承？** | ❌ 不支持 | **✅ 支持（PI mutex）** |

---

### 写函数 `led_write()`（第 57-76 行）

```c
static ssize_t led_write(struct file *filp, const char __user *buf,
                         size_t count, loff_t *ppos)
{
    int ret;
    unsigned char databuf[1];
    struct gpioled_dev *dev = filp->private_data;  // 取回设备指针

    ret = copy_from_user(databuf, buf, count);     // 从用户空间拷贝数据
    if(ret < 0) {                                   // Bug: 应为 ret != 0
        return -EINVAL;
    }

    if(databuf[0] == LEDON) {
        gpio_set_value(dev->led_gpio, 0);            // 低电平 → LED 亮
    } else if(databuf[0] == LEDOFF) {
        gpio_set_value(dev->led_gpio, 1);            // 高电平 → LED 灭
    }

    return 0;
}
```

---

### 驱动入口 `led_init()`（第 87-164 行）

```c
static int __init led_init(void)
{
    int ret = 0;

    /*
     * ★ mutex_init(&gpioled.lock)：
     *   初始化互斥体为"未锁定"状态
     *
     * 互斥体初始化没有"初始值"参数！
     * 因为互斥体永远是二值的（锁定/未锁定），不存在计数概念。
     *
     * 对比：
     *   sema_init(&sem, 1)  ← 可以指定初始值为任意值
     *   mutex_init(&lock)    ← 始终是未锁定状态
     */
    mutex_init(&gpioled.lock);

    // ===== 字符设备框架（与实验9、10完全相同）=====
    // 1. 注册设备号（动态分配）
    // 2. 初始化 cdev + 绑定 file_operations
    // 3. 添加 cdev 到内核
    // 4. 创建设备类 → /sys/class/gpioled
    // 5. 创建设备实例 → /dev/gpioled

    // ===== 硬件初始化（与实验9、10完全相同）=====
    // 6. 获取设备树节点 /gpioled
    // 7. 获取 GPIO 编号
    // 8. 申请 GPIO
    // 9. 设置 GPIO 为输出（默认高电平）
    // 10. 输出低电平点亮 LED
}
```

**互斥体初始化方式：**
```c
// 方式1: 运行时初始化（本实验使用）
struct mutex lock;
mutex_init(&lock);

// 方式2: 静态定义 + 初始化（编译时）
static DEFINE_MUTEX(lock);
// 等价于 static struct mutex lock = __MUTEX_INITIALIZER(lock);
```

---

### 三、互斥体核心知识

### 什么是互斥体？

互斥体（mutex = **mut**ual **ex**clusion）是 Linux 内核中专门为"二进制互斥"设计的睡眠锁。它从信号量衍生而来，但语义更严格：

```c
struct mutex {
    atomic_long_t       owner;      // ★ 所有者（指向当前持有锁的 task_struct）
    raw_spinlock_t      wait_lock;  // 保护等待队列的自旋锁
    struct list_head    wait_list;  // 等待队列
    // ... 调试字段 ...
};
```

**Mutex 的"三不允许"：**
1. ❌ 不能在中断上下文中使用（lock 和 unlock 都不行）
2. ❌ 不能递归获取（同一个进程 lock 两次 = 死锁）
3. ❌ 持有 mutex 时不能退出（进程退出前必须 unlock）

### Mutex 的 fastpath / slowpath 设计

Linux mutex 使用**乐观自旋（Optimistic Spinning）**来优化性能：

```
mutex_lock(&lock)
│
├─ 【fastpath - 无竞争】
│   mutex 未被持有
│   → 通过原子指令直接设置 owner = current
│   → 立即返回（没有上下文切换）
│   → 开销：几个 CPU 指令（接近自旋锁的效率！）
│
├─ 【midpath - 乐观自旋】（内核配置 MUTEX_SPIN_ON_OWNER）
│   mutex 被持有，但持有者正在另一个 CPU 上运行
│   → 自旋等待一小段时间（不是立即睡眠）
│   → 如果持有者很快释放 → 直接获取，避免上下文切换
│   → 如果自旋超时 → 进入 slowpath 睡眠
│
└─ 【slowpath - 真实竞争】
    mutex 被持有且自旋无望
    → 加入等待队列
    → 睡眠让出 CPU
    → 被唤醒后获取 mutex
```

这就是为什么 mutex 在"临界区短"时性能接近自旋锁，在"临界区长"时又不会浪费 CPU。

### 优先级继承（PI Mutex）

互斥体支持**优先级反转**的解决方案：

```
【优先级反转经典场景】
  低优先级进程 L: 持有 mutex
  高优先级进程 H: mutex_lock() → 阻塞等待
  中优先级进程 M: 不需要 mutex，持续运行
  
  → 问题：L 被 M 抢占了 CPU，无法释放 mutex
  → H 虽然优先级最高，但被 M 间接阻塞！
  → 这就是"优先级反转"

【PI Mutex 的解决方案】
  mutex_lock(PI) → L 的优先级被临时提升到与 H 相同
  → M 无法抢占 L（因为 L 的优先级临时变高了）
  → L 尽快完成工作释放 mutex
  → H 获取 mutex 继续执行
```

内核配置：`CONFIG_PREEMPT_RT` 将内核 mutex 自动变为 PI mutex。

### Lockdep 死锁检测

Mutex 的一大优势是**内核 lockdep 支持**，能自动检测潜在死锁：

```c
// 场景：两个 mutex 以不同顺序获取
// CPU0: mutex_lock(A) → mutex_lock(B)
// CPU1: mutex_lock(B) → mutex_lock(A)
// → ABBA 死锁！

// Lockdep 会在运行时输出：
// ======================================================
// WARNING: possible circular locking dependency detected
// ======================================================
// CPU0: lock(A) → lock(B)
// CPU1: lock(B) → lock(A)   ← 潜在死锁！
```

**信号量没有这个能力**——如果你用信号量，ABBA 死锁不会产生任何 warning，只会静静地把系统卡死。

---

### 四、测试程序 `mutexAPP.c` 分析

```c
int main(int argc, char *argv[])
{
    fd = open(filename, O_RDWR);    // → led_open → mutex_lock(&lock)
                                    // 如果互斥体已被占用，open() 会阻塞！
                                    // 行为和信号量一样（睡眠等待）

    databuf[0] = atoi(argv[2]);     // 解析控制命令
    write(fd, databuf, sizeof(databuf)); // 控制LED

    // ★ 模拟占用25秒
    while(1) {
        sleep(5);
        cnt++;
        printf("App Runing times:%d\r\n", cnt);
        if(cnt >= 5) break;
    }

    close(fd);  // → led_release → mutex_unlock(&lock)
                // 释放互斥体，唤醒等待者
    return 0;
}
```

**测试行为与实验10（信号量）完全相同：**
- 第二个进程 open 时阻塞睡眠
- 第一个进程 close 后第二个进程被唤醒

**mutex vs semaphore 无法从用户空间测试区分**，区别体现在内核层面的安全性、性能和调试支持。

---

### 五、全部实验对比总结（实验6→8→9→10→11 演化路径）

### 代码演进对比

```
【实验6 - gpioled】无保护
  struct gpioled_dev {
      ...
      // 无任何并发保护字段
  };
  led_open(): 无任何锁操作
  led_release(): 无任何锁操作

     ↓  加入互斥需求：多个进程不能同时打开设备

【实验8 - atomic】原子操作
  struct gpioled_dev {
      ...
      atomic_t lock;  // ★ 新增
  };
  led_open(): atomic_dec_and_test(&lock)  ← 读-减-判断 一条原子指令
  led_release(): atomic_inc(&lock)

     ↓  原子操作只适合简单场景，复杂临界区需要锁

【实验9 - spinlock】自旋锁
  struct gpioled_dev {
      ...
      int dev_status;      // ★ 新增：被保护数据
      spinlock_t lock;     // ★ 新增：保护 dev_status 的锁
  };
  led_open(): spin_lock_irqsave → 检查 dev_status → spin_unlock_irqrestore
  led_release(): spin_lock_irqsave → dev_status-- → spin_unlock_irqrestore

     ↓  自旋锁不能睡眠，临界区长时浪费 CPU

【实验10 - semaphore】信号量
  struct gpioled_dev {
      ...
      struct semaphore sem;  // ★ 替代 dev_status + spinlock
  };
  led_open(): down(&sem)    ← 失败则睡眠，不忙等
  led_release(): up(&sem)   ← 释放并唤醒等待者

     ↓  信号量适合计数同步，纯互斥场景有更优选择

【实验11 - mutex】互斥体 ★ 推荐
  struct gpioled_dev {
      ...
      struct mutex lock;     // ★ 替代 semaphore
  };
  led_open(): mutex_lock(&lock)      ← 有所有者、fastpath、debug 支持
  led_release(): mutex_unlock(&lock) ← 严格的所有者检查
```

### 综合对比大表

| 维度 | gpioled (6) | atomic (8) | spinlock (9) | semaphore (10) | **mutex (11) ★** |
|------|:------:|:------:|:--------:|:---------:|:--------:|
| **保护机制** | 无 | 原子指令 | 自旋忙等 | 睡眠+队列 | 睡眠+队列 |
| **锁类型** | — | 无锁 | 忙等锁 | 睡眠锁 | 睡眠锁(优化) |
| **所有者概念** | — | — | — | ❌ 无 | **✅ 有** |
| **临界区长度** | 任意 | < μs | < μs | ms~s | ms~s |
| **临界区内可睡眠？** | ✅ | — | ❌ 死机 | ✅ | ✅ |
| **中断上下文可用？** | — | ✅ 可 | ✅ 可 | 仅 up() | ❌ 不可 |
| **可同时持有数** | ∞ | 1 | 1 | 1~N | 1 |
| **未获取时的行为** | — | 返回错误 | 忙等(自旋) | 睡眠 | **睡眠/乐观自旋** |
| **CPU 开销** | 无 | 极低 | 中(忙等) | 高(调度) | **中(fastpath优化)** |
| **死锁检测** | — | — | — | ❌ | **✅ lockdep** |
| **优先级继承** | — | — | — | ❌ | **✅ 可选** |
| **代码复杂度** | 最简单 | 简单 | 中 | 中 | 中 |
| **调试支持** | — | 差 | 差 | 差 | **最好** |
| **使用场景** | 无需保护 | 简单标志 | 极短临界区+中断 | 计数同步 | **通用互斥(首选)** |

### 终极选择指南

```
你需要内核并发保护？

├─ 临界区在中断上下文中？
│   └─ → spinlock（唯一选择，中断上下文不能睡眠）
│
├─ 临界区极短（< 几微秒）、不能睡眠？
│   └─ → spinlock
│
├─ 临界区较长、可能睡眠？
│   ├─ 只需要简单互斥（0/1）？
│   │   └─ → mutex ★（首选！有所有者、debug、lockdep）
│   │
│   ├─ 需要允许多个进程同时访问（如限制5个）？
│   │   └─ → semaphore(N)
│   │
│   └─ 需要事件通知模式（A等B做某事）？
│       └─ → semaphore(0)  // 初始为0，B完成后up唤醒A
│
└─ 只需要保护一个整数的加减/判断？
    └─ → atomic_t（最轻量，无锁）
```

---

### 六、驱动执行流程全景图

```
模块加载 (insmod mutex.ko)
│
├─ led_init()
│   ├─ ★ mutex_init(&gpioled.lock)          # 初始化互斥体
│   ├─ alloc_chrdev_region()                # 分配设备号
│   ├─ cdev_init() + cdev_add()            # 注册字符设备
│   ├─ class_create() + device_create()     # 创建设备文件
│   ├─ of_find_node_by_path("/gpioled")     # 查找设备树节点
│   ├─ of_get_named_gpio()                  # 获取GPIO编号
│   ├─ gpio_request()                       # 申请GPIO
│   ├─ gpio_direction_output(..., 1)        # 设为输出(默认高)
│   └─ gpio_set_value(..., 0)               # 点亮LED
│
用户空间: open("/dev/gpioled", O_RDWR)
│   └─ VFS ───→ led_open()
│       ├─ filp->private_data = &gpioled
│       └─ ★ mutex_lock(&gpioled.lock)
│           ├── fastpath: 未持有 → 设置 owner=current → 返回
│           ├── midpath: 被持有+持有者在运行 → 乐观自旋 → 获取/放弃
│           └── slowpath: 自旋失败 → 加入等待队列 → 睡眠
│                                    ↑
│                          （等待 mutex_unlock() 唤醒）
│
用户空间: write(fd, buf, 1)
│   └─ VFS ───→ led_write()
│       ├─ copy_from_user(databuf, buf, count)
│       └─ gpio_set_value(led_gpio, 0/1)
│
用户空间: close(fd)
│   └─ VFS ───→ led_release()
│       └─ ★ mutex_unlock(&gpioled.lock)
│           ├── 检查: current == owner？（调试断言）
│           ├── 清除 owner
│           └── 有等待者？ → 唤醒等待队列中的第一个进程
│
模块卸载 (rmmod mutex)
└─ led_exit()
    ├─ gpio_set_value(..., 1) → 关LED
    ├─ cdev_del() + unregister_chrdev_region()
    ├─ device_destroy() + class_destroy()
    └─ gpio_free()
```

---

### 七、代码 Bug 及改进建议

### Bug #1：copy_from_user 返回值判断错误
```c
// mutex.c 第65行（同 spinlock/semaphore）
ret = copy_from_user(databuf, buf, count);
if(ret < 0) {    // ✗ 错误！该函数永远不返回负数
// 应改为：
if(ret != 0) {   // ✓ 检查是否有未成功拷贝的字节
    return -EFAULT;
}
```

### 改进建议 #1：使用可中断的锁
```c
// 当前代码
mutex_lock(&gpioled.lock);

// 推荐写法
if (mutex_lock_interruptible(&gpioled.lock)) {
    return -ERESTARTSYS;  // 被信号打断，返回让用户空间重试
}
```

### 改进建议 #2：添加超时机制
```c
// 如果需要等待超时
if (mutex_lock_interruptible(&gpioled.lock)) {
    return -ERESTARTSYS;
}
// 这个场景 mutex 没有直接提供超时版本，
// 可以用 mutex_trylock + schedule_timeout 组合实现
```

### 改进建议 #3：使用 DEFINE_MUTEX 简化初始化
```c
// 当前方式：运行时初始化
struct gpioled_dev gpioled;
// 在 led_init 中:
mutex_init(&gpioled.lock);

// 更简洁的方式：静态初始化
struct gpioled_dev gpioled = {
    .lock = __MUTEX_INITIALIZER(gpioled.lock),
};
// 或者 C99 指定初始化（需要 .lock 支持）
```

---

### 八、必须掌握的知识点清单

1. ✅ 互斥体的"所有者"概念——只有 lock 者才能 unlock
2. ✅ mutex 的 fastpath / midpath（乐观自旋） / slowpath 三级优化
3. ✅ `mutex_lock` / `mutex_lock_interruptible` / `mutex_trylock` 的区别
4. ✅ 为什么 mutex_unlock 不能在中断上下文调用
5. ✅ mutex vs semaphore 的本质区别（所有者、debug、PI）
6. ✅ 优先级反转问题和 PI mutex 的解决原理
7. ✅ lockdep 死锁检测对 mutex 的支持
8. ✅ `DEFINE_MUTEX` vs `mutex_init` 的初始化方式
9. ✅ mutex 的严格使用规则（不能递归、不能中断上下文、不能进程退出）
10. ✅ 五个实验的演化路径：gpioled(无保护) → atomic → spinlock → semaphore → mutex（终极推荐）

---

## 第十二章 四种并发保护机制对比

> 这四个实验实现了**同一个目标**：同一时刻只允许一个进程使用 LED 设备（互斥访问）。
> 90% 的代码完全相同（字符设备框架、GPIO 初始化、led_write 等），**唯一的变化在 4 个地方**：
> 设备结构体成员、led_init 初始化、led_open、led_release。

---

### 一、快速总览

| | 实验8 | 实验9 | 实验10 | 实验11 |
|---|---|---|---|---|
| **机制** | 原子操作 (`atomic_t`) | 自旋锁 (`spinlock_t`) | 信号量 (`struct semaphore`) | 互斥体 (`struct mutex`) |
| **头文件** | `<linux/atomic.h>` | `<linux/spinlock.h>` | `<linux/semaphore.h>` | `<linux/mutex.h>` |
| **设备忙时** | open() 立即返回 -EBUSY | open() 立即返回 -EBUSY | open() **阻塞睡眠等待** | open() **阻塞睡眠等待** |
| **是否睡眠** | 不睡眠 | 不睡眠 | **睡眠，让出 CPU** | **睡眠，让出 CPU** |
| **结构体成员** | `atomic_t lock`（1个） | `int dev_status` + `spinlock_t lock`（2个） | `struct semaphore sem`（1个） | `struct mutex lock`（1个） |
| **初始化** | `atomic_set(&lock, 1)` | `spin_lock_init()` + `dev_status = 0` | `sema_init(&sem, 1)` | `mutex_init(&lock)` |
| **申请** | `atomic_dec_and_test()` | `spin_lock`→判断→改值→`spin_unlock` | `down(&sem)` | `mutex_lock(&lock)` |
| **释放** | `atomic_inc(&lock)` | `spin_lock`→改值→`spin_unlock` | `up(&sem)` | `mutex_unlock(&lock)` |
| **中断可用** | ✅ 可以 | ✅ 可以 | ✅ up() 可以 (down 不行) | ❌ 不可以 |
| **持有锁时能睡眠** | — | ❌ 绝对不能 | ✅ 可以 | ✅ 可以 |
| **代码复杂度** | ⭐⭐ | ⭐⭐⭐（最啰嗦） | ⭐（最简洁） | ⭐ |
| **持有者追踪** | ❌ 无 | ❌ 无 | ❌ 无 | ✅ 有 owner |
| **死锁检测** | ❌ | ❌ | ❌ | ✅ lockdep |

---

### 二、各实验知识点详解

### 实验8 —— 原子操作 (atomic_t)

**核心概念**：利用 CPU 提供的原子指令（如 ARM 的 `LDREX/STREX`），在**不借助锁**的情况下完成"读-改-写"操作。原子变量内部是一个 `int` 类型的值，对它做加减等操作是**不可分割**的，硬件保证不会被其他 CPU 打断。

**原理**：`atomic_dec_and_test()` 先原子减 1，然后测试结果。整个过程在一个 CPU 指令序列中完成：
- 从 `lock=1` 减到 `0` → 返回真（减后等于 0）→ 成功获取
- 从 `lock=0` 减到 `-1` → 返回假（减后不等于 0）→ 已被占用

**适用场景**：保护单个整型变量的简单"是/否"状态切换，不需要复杂的等待队列。

**局限**：只能做简单的加减、置位等操作，不能保护复杂的临界区（多行代码）。

```c
// ============ 设备结构体 ============
struct gpioled_dev {
    // ... 通用成员 ...
    atomic_t lock;  // 原子变量：1=可用, 0=被占用
};

// ============ led_init 初始化 ============
atomic_set(&gpioled.lock, 1);  // 初始值设为 1

// ============ led_open 获取 ============
static int led_open(struct inode *inode, struct file *filp)
{
    filp->private_data = &gpioled;

    // 原子减 1 并测试是否等于 0
    if (!atomic_dec_and_test(&gpioled.lock)) {
        // lock 原来是 0 → 减完是 -1 → 设备已被占用
        atomic_inc(&gpioled.lock);   // 恢复原值！这一步很重要
        return -EBUSY;               // 立即返回错误，不等待
    }
    // lock 原来是 1 → 减完是 0 → 成功获取设备

    return 0;
}

// ============ led_release 释放 ============
static int led_release(struct inode *inode, struct file *filp)
{
    struct gpioled_dev *dev = filp->private_data;

    atomic_inc(&dev->lock);  // 加 1：0→1，恢复为可用状态

    return 0;
}
```

**执行流程图解**：

```
进程A打开设备：
  atomic_dec_and_test(&lock) → lock:1→0 → 返回true → 成功！

进程B打开设备（A还没关闭）：
  atomic_dec_and_test(&lock) → lock:0→-1 → 返回false
  → atomic_inc(&lock) → lock:-1→0 → 恢复
  → return -EBUSY → 用户程序收到 "open failed"
```

**关键细节**：失败时一定要 `atomic_inc` 恢复原值！因为 `dec_and_test` 已经减了 1。

---

### 实验9 —— 自旋锁 (spinlock_t)

**核心概念**：自旋锁通过**忙等（busy-wait）**来保护临界区。当一个 CPU 持有自旋锁时，另一个 CPU（或同一 CPU 上的其他上下文）尝试获取锁会在原地**不停地循环检查**（"自旋"），直到锁被释放。

**关键特性**：
- 自旋锁持仓期间**绝对不能睡眠**！否则可能死锁或内核崩溃
- `spin_lock_irqsave` 在加锁同时**关闭本地中断**，防止中断处理程序试图获取同一把锁造成死锁
- 适合保护**极短的临界区**（几行代码、几个变量修改）

**实验9为什么要两个变量？**
- `spinlock_t lock`：保护"检查和修改 dev_status"这个过程不被打断（只持有一瞬间）
- `int dev_status`：真正标记"设备是否被占用"（从 open 持续到 release）
- 自旋锁不能长时间持有（可能睡眠），所以不能用它直接锁住整个设备使用期

```c
// ============ 设备结构体 ============
struct gpioled_dev {
    // ... 通用成员 ...
    int dev_status;      // 设备状态：0=可用, >0=被占用
    spinlock_t lock;     // 保护 dev_status 读写的自旋锁
};

// ============ led_init 初始化 ============
spin_lock_init(&gpioled.lock);  // 初始化自旋锁
gpioled.dev_status = 0;         // 状态初始化为"可用"

// ============ led_open 获取 ============
static int led_open(struct inode *inode, struct file *filp)
{
    unsigned long irqflag;
    filp->private_data = &gpioled;

    // ① 加锁 + 关闭中断（保护接下来的读-改操作）
    spin_lock_irqsave(&gpioled.lock, irqflag);

    if (gpioled.dev_status) {             // ② 检查：设备被占用？
        // 被占用 → 直接返回错误
        spin_unlock_irqrestore(&gpioled.lock, irqflag);  // ③ 解锁
        return -EBUSY;
    }

    gpioled.dev_status++;                 // ④ 标记：设备已被占用
    spin_unlock_irqrestore(&gpioled.lock, irqflag);  // ⑤ 解锁（锁只持有一瞬间！）
    // ★ 注意：锁已释放，但 dev_status=1 持续到 release

    return 0;
}

// ============ led_release 释放 ============
static int led_release(struct inode *inode, struct file *filp)
{
    unsigned long irqflag;
    struct gpioled_dev *dev = filp->private_data;

    spin_lock_irqsave(&dev->lock, irqflag);  // ① 加锁
    if (dev->dev_status) {
        dev->dev_status--;                    // ② 改状态：标记为可用
    }
    spin_unlock_irqrestore(&dev->lock, irqflag);  // ③ 解锁

    return 0;
}
```

**执行流程图解**：

```
进程A打开设备：
  spin_lock → dev_status==0? 是 → dev_status=1 → spin_unlock → 成功！

进程B打开设备（A还没关闭）：
  spin_lock → dev_status==1? 是 → spin_unlock → return -EBUSY
  → 用户程序收到 "open failed"

  注意：B 的 spin_lock 可能短暂自旋等待（微秒级），
  因为 A 的锁只持有一瞬间就释放了。B 拿锁成功后，
  发现 dev_status=1（被占用），解锁后立即返回错误。
```

**自旋锁和 dev_status 的分工**：

```
时间轴：
────────────────────────────────────────────────────
          open                 整个使用期            release
┌─[自旋锁持有]────┐                                ┌─[自旋锁持有]┐
│ check & set     │                                │ clear       │
└─────────────────┘                                └─────────────┘
         ↑ 微秒级                                     ↑ 微秒级

┌────────────────────── dev_status = 1 ──────────────────────────┐
                         ↑ 持续到 release
```

**关键细节**：自旋锁只在"读写 dev_status"的瞬间持有（微秒级），**不是**整个设备使用期间持有。真正阻止其他人用的是 `dev_status` 这个标记位。

---

### 实验10 —— 信号量 (struct semaphore)

**核心概念**：信号量是一个**带计数器的等待队列**。当进程 `down()` 获取信号量时：
- 如果 `count > 0`（有资源）→ 原子减 1 → 立即返回（不睡眠）
- 如果 `count <= 0`（无资源）→ 进程加入等待队列 → **睡眠** → 让出 CPU → 等别人 `up()` 唤醒

**信号量内部结构**（简化版）：
```c
struct semaphore {
    int count;              // 计数器：1=可用, 0=被占, -N=N个等待者
    struct list_head wait_list;  // 等待队列
    spinlock_t lock;        // ★ 内部自旋锁（保护 count 和 wait_list）
};
```

信号量内部就封装了自旋锁 + 计数器 + 等待队列，所以你不需要手动管理这些！

```c
// ============ 设备结构体 ============
struct gpioled_dev {
    // ... 通用成员 ...
    struct semaphore sem;  // ★ 一个变量替代了实验9的 dev_status + lock
};

// ============ led_init 初始化 ============
sema_init(&gpioled.sem, 1);  // 初始值 1 = 二进制信号量（互斥信号量）

// ============ led_open 获取 ============
static int led_open(struct inode *inode, struct file *filp)
{
    filp->private_data = &gpioled;

    down(&gpioled.sem);  // ★ 一行搞定！
    // 内部流程（信号量自动完成）：
    //   1. 内部 spin_lock
    //   2. count--：1→0 → >=0 → 成功！spin_unlock → 返回
    //   3. 或 count--：0→-1 → <0 → 加入等待队列 → spin_unlock → 睡眠

    return 0;
}

// ============ led_release 释放 ============
static int led_release(struct inode *inode, struct file *filp)
{
    struct gpioled_dev *dev = filp->private_data;

    up(&dev->sem);  // ★ 一行搞定！
    // 内部流程（信号量自动完成）：
    //   1. 内部 spin_lock
    //   2. count++：0→1 → >0 → 无人等待 → spin_unlock → 返回
    //   3. 或 count++：-1→0 → <=0 → 从等待队列取出进程 → 唤醒
}

// ★ led_write 不需要操作信号量！因为能执行到这里的进程已经持有信号量。
```

**`down()` 内部实现要点**：

```c
void down(struct semaphore *sem)
{
    spin_lock(&sem->lock);          // ① 内部自旋锁保护
    sem->count--;                   // ② 原子：计数减1

    if (sem->count >= 0) {          // ③ 原来 >0，说明有资源
        spin_unlock(&sem->lock);    //    解锁 → 直接返回，不睡眠
        return;
    }

    // ④ 原来 =0，说明无资源 → 要睡眠了
    //    把当前进程加入 sem->wait_list
    spin_unlock(&sem->lock);        //    先解锁（不能抱着锁睡觉！）
    schedule();                     //    让出 CPU，进程在此睡眠
    // ⑤ 被 up() 唤醒后从 schedule() 返回
}
```

**执行流程图解**：

```
进程A打开设备：
  down(&sem) → count:1→0 → ≥0 → 成功！

进程B打开设备（A还没关闭）：
  down(&sem) → count:0→-1 → <0 → 加入等待队列 → 睡眠
  ★ 进程B 的 open() 调用不返回！B 卡住了，CPU 去跑别的进程

进程A关闭设备：
  up(&sem) → count:-1→0 → ≤0 → 从等待队列唤醒进程B
  ★ 进程B 从 schedule() 返回 → open() 返回 0 → B 现在持有设备
```

**与实验9的根本区别**：

| | 实验9 spinlock | 实验10 semaphore |
|---|---|---|
| 设备被占用时 | `open()` 立即返回 `-EBUSY` | `open()` **阻塞睡眠**，不返回 |
| 用户程序感知 | 立即知道失败，可以重试或放弃 | 卡在 `open()` 调用上，等别人释放 |
| 等待机制 | 无等待，直接返回错误 | 有等待队列，FIFO 公平唤醒 |
| 临界区内能睡眠 | ❌ 不行 | ✅ 可以（如 `copy_from_user`） |

---

### 实验11 —— 互斥体 (struct mutex)

**核心概念**：互斥体是 Linux 内核专门为**互斥场景**优化的睡眠锁，可以理解为"信号量的升级版"。它基于信号量的思想，但做了大量优化和增强了调试能力：

- **owner（所有者）**：记录当前是谁持有了锁（`task_struct` 指针），这是 mutex 最本质的设计
- **fastpath**：无竞争时，原子设置 owner = current，只需几个 CPU 指令
- **midpath**：有竞争但持有者在运行 → 乐观自旋一小段时间（类似自旋锁），避免昂贵的睡眠+唤醒
- **slowpath**：自旋失败 → 加入等待队列 → 睡眠
- **lockdep 死锁检测**：能检测到：自己锁自己（递归获取）、两个进程互相等对方的锁（AA 死锁）
- **PI（优先级继承）**：解决优先级反转问题（高优先级进程在等低优先级进程释放锁时造成中间优先级进程运行的问题）

```c
// ============ 设备结构体 ============
struct gpioled_dev {
    // ... 通用成员 ...
    struct mutex lock;  // ★ 互斥体：纯二值（锁住/未锁住），有 owner
};

// ============ led_init 初始化 ============
mutex_init(&gpioled.lock);  // 初始化为"未锁定"状态（不需要指定值）

// ============ led_open 获取 ============
static int led_open(struct inode *inode, struct file *filp)
{
    filp->private_data = &gpioled;

    mutex_lock(&gpioled.lock);  // ★ 一行搞定！
    // 三级执行路径：
    //   Fastpath:   无竞争 → 原子设置 owner → 立即返回
    //   Midpath:    有竞争+持有者在运行 → 乐观自旋
    //   Slowpath:   自旋失败 → 加入等待队列 → 睡眠

    return 0;
}

// ============ led_release 释放 ============
static int led_release(struct inode *inode, struct file *filp)
{
    struct gpioled_dev *dev = filp->private_data;

    mutex_unlock(&dev->lock);  // ★ 一行搞定！
    // 内核验证：current == owner？（不匹配 → kernel warning）
    // 检查等待队列 → 有人等就唤醒第一个

    return 0;
}
```

**Mutex 为什么比信号量更好（纯互斥场景）**：

```
场景：设备未被占用，进程A 来 open()

信号量的 down():
  内部 spin_lock → count-- → 判断 count>=0 → spin_unlock → 返回
  即使没竞争，也有"锁-解锁"的开销

互斥体的 mutex_lock():
  Fastpath: 原子设置 owner = current → 完成！
  没竞争时，比信号量更快！
```

---

### 三、四个实验的核心区别

### 3.1 第一层区别：是否睡眠

这是**最直观的区别**，直接影响用户程序的行为：

```
                       设备已被占用时的行为
                       ┌─────────────────┐
                       │                 │
            不睡眠      │        睡眠等待  │
          （立即返回）   │      （让出CPU）  │
              │        │         │       │
       ┌──────┴──────┐ │  ┌──────┴──────┐│
       │   实验8     │ │  │   实验10    ││
       │  atomic_t   │ │  │ semaphore   ││
       │   实验9     │ │  │   实验11    ││
       │  spinlock   │ │  │   mutex     ││
       └─────────────┘ │  └─────────────┘│
                       └─────────────────┘
```

**测试对比**（运行两次相同的应用程序，先启动的占用设备 25 秒）：

```
实验8 (atomic):                实验10 (semaphore):
$ ./atomicAPP /dev/gpioled 1   $ ./semaApp /dev/gpioled 1
App Runing times:1             App Runing times:1
                               
$ ./atomicAPP /dev/gpioled 1   $ ./semaApp /dev/gpioled 1  ← 另开终端
file open failed!  ← 立即报错   (卡住不动，什么都不输出...)  ← 在等
                               (25秒后自动继续...)
                               App Runing times:1      ← 第一个释放后被唤醒
```

### 3.2 第二层区别：代码简洁度（有无封装）

```
实验8 (atomic):     手动减1+判断+失败恢复   ← 需要 if/else/恢复原值
实验9 (spinlock):   加锁→判断→改值→解锁     ← 最啰嗦，需要两个变量
实验10 (semaphore): down() / up()          ← 一行，内核帮你封装
实验11 (mutex):     mutex_lock() / unlock()  ← 一行，内核帮你封装
```

实验8/9 是"手动挡"——你自己管理锁和状态。
实验10/11 是"自动挡"——内核帮你做好了互斥逻辑，你只调 API。

### 3.3 第三层区别：内部实现精细度

```
实验10 (semaphore) 内部：
  ┌──────────────┐
  │ 自旋锁        │ ← 保护 count 和 wait_list
  │ count 计数器   │ ← 1=可用, 0=被占, -N=N在等
  │ wait_list    │ ← 睡眠等待队列
  └──────────────┘
  简单、通用、但没做太多优化

实验11 (mutex) 内部：
  ┌──────────────┐
  │ owner 指针    │ ← ★ 记录谁持有锁（核心设计）
  │ 自旋锁        │
  │ wait_list    │
  │ debug 信息    │ ← lockdep 死锁检测
  │ fastpath标志  │ ← 无竞争时跳过锁操作
  │ midpath自旋   │ ← 乐观自旋（持有者在运行→不自即睡眠）
  └──────────────┘
  专门为互斥优化：更快、更安全、能发现 bug
```

### 3.4 第三层区别：允许的使用场景

| | 中断上下文 | 持有锁能睡眠 | 递归获取 | 谁获取谁释放 |
|---|---|---|---|---|
| **实验8 (atomic)** | ✅ | — | ❌ | 不要求 |
| **实验9 (spinlock)** | ✅ | ❌ | ❌ | 不要求 |
| **实验10 (semaphore)** | down❌ up✅ | ✅ | ❌ | 不要求 |
| **实验11 (mutex)** | ❌ | ✅ | ❌（会死锁） | ✅ 强制要求 |

---

### 四、演进关系图

这 4 个实验的演进逻辑是：**从手动到自动，从基础到优化，从不睡眠到睡眠**。

```
实验8 (atomic_t)
  │  最简单的原子操作
  │  局限：只能保护单变量
  │
  └──▶ 实验9 (spinlock)
         │  加入锁的概念，保护"读-改"临界区
         │  局限：需要 2 个变量，代码啰嗦；设备忙时只能返回错误
         │
         └──▶ 实验10 (semaphore)
                │  内核封装了锁+状态+等待队列
                │  优势：1 个变量，down/up 两行代码
                │  改善：设备忙时睡眠等待（而非返回错误）
                │  局限：无 owner、无死锁检测
                │
                └──▶ 实验11 (mutex)
                      信号量的"互斥专用升级版"
                      新增：owner 追踪、fastpath 优化
                            死锁检测、乐观自旋
```

---

### 五、一句话记忆口诀

| 实验 | 口诀 |
|---|---|
| **8 atomic** | **原子变量自己管，设备忙了立刻返** |
| **9 spinlock** | **两员大将来护驾，锁秒开、状态长占，忙时打回 EBUSY** |
| **10 semaphore** | **一个信号全搞定，别人用着我睡觉，等他放了我再起** |
| **11 mutex** | **信号量的升级版，认主人（owner）、防死锁、没竞争时贼快** |

---

### 六、实际项目选择建议

```
你要保护的东西是什么？
│
├─ 只是一个整型变量的状态切换
│   └─ 用原子操作 (atomic_t)              ← 实验8
│
├─ 多行代码的临界区，极短（几微秒），可能在中断中访问
│   └─ 用自旋锁 (spinlock_t)              ← 实验9
│
├─ 临界区可能睡眠（调用 copy_from_user 等），需要计数
│   └─ 用信号量 (semaphore)               ← 实验10
│
└─ 临界区可能睡眠，纯互斥（二值），在进程上下文
    └─ 用互斥体 (mutex)  ← 实验11（这是绝大多数情况的首选！）
```

> **总结**：对于纯互斥场景（同一时间只允许一个进程访问），**mutex 是首选**。信号量适用于计数同步或需要在中断上下文中 `up()` 的场景。自旋锁只适合极短的不睡眠临界区。原子操作用于简单的单变量标志位。

---

*文档创建时间：2026年6月8日*
*基于正点原子阿尔法IMX6ULL Linux驱动开发教程 实验8/9/10/11*

---

## 第十三章 按键输入驱动

> 本实验实现了一个基于 GPIO 子系统的按键输入字符设备驱动。
> 与实验6~11（LED输出）最大的区别：GPIO 方向从"输出"变为"输入"，
> 数据流向从"用户→驱动→硬件"变为"硬件→驱动→用户"。

---

### 一、你需要掌握的知识点清单

| 序号 | 知识点 | 说明 |
|------|--------|------|
| 1 | **GPIO 输入模式** | `gpio_direction_input()` — 与输出的本质区别 |
| 2 | **gpio_get_value()** | 读取引脚电平，替代输出的 `gpio_set_value()` |
| 3 | **copy_to_user()** | 数据从内核传到用户空间（输入驱动的核心操作） |
| 4 | **原子变量存状态** | `atomic_t keyvalue` — 在内核和用户间传递按键值 |
| 5 | **按键消抖原理** | 为什么需要消抖 + 本实验的简单处理方式 |
| 6 | **输入驱动的完整数据流** | 硬件信号 → GPIO读取 → 内核处理 → 用户空间 |
| 7 | **file_operations 的 .read 回调** | 与 .write 回调的对称关系 |

---

### 二、整体架构和数据流向

### 2.1 完整数据通路

```
┌─────────────────────────────────────────────────────────────────┐
│                        用户空间                                   │
│  keyAPP.c                                                        │
│  while(1) {                                                      │
│      read(fd, &value, sizeof(value));  ───── 系统调用 ─────┐     │
│      if(value == 0xF0)                                       │     │
│          printf("KEY0 Press");                                │     │
│  }                                                            │     │
└───────────────────────────────────────────────────────────────┼───┘
                                                                │
    ┌───────────────────────────────────────────────────────────┘
    │  VFS 层：根据文件描述符 fd → 找到 file → 找到 file_operations → 调用 .read
    ▼
┌─────────────────────────────────────────────────────────────────┐
│                        内核空间                                   │
│  key.c: key_read()                                               │
│                                                                  │
│  ① gpio_get_value(key_gpio)  ← 读引脚电平                        │
│       │                                                          │
│       ├── == 0 (低电平) → 按键按下                                │
│       │     while(!gpio_get_value());  ← 等松开（消抖）           │
│       │     keyvalue = 0xF0                                      │
│       │                                                          │
│       └── != 0 (高电平) → 没按或已松开                            │
│             keyvalue = 0x00                                      │
│                                                                  │
│  ② copy_to_user(buf, &value, sizeof(value))  ← 传回用户空间       │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│                        硬件层                                     │
│                                                                  │
│  按键电路：                                                       │
│  VCC_3.3V ──[上拉电阻]──┬── KEY0 引脚 (GPIO1_IO18)               │
│                         │                                        │
│                         [按键]                                    │
│                         │                                        │
│                        GND                                       │
│                                                                  │
│  未按下：引脚被上拉到 3.3V → gpio_get_value() = 1 (高电平)        │
│  按  下：引脚被拉到 GND     → gpio_get_value() = 0 (低电平)       │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 2.2 与 LED 驱动（实验6）的镜像对称

```
                     LED输出                      KEY输入
                     ═══════                      ═══════
                  
用户操作             write()                      read()
                     │                             │
驱动函数           led_write()     ←──镜像──→    key_read()
                     │                             │
数据方向         copy_from_user()              copy_to_user()
                (用户→内核)                   (内核→用户)
                     │                             │
GPIO操作         gpio_set_value()              gpio_get_value()
                (写电平)                      (读电平)
                     │                             │
GPIO方向         gpio_direction_output()       gpio_direction_input()
                (输出模式)                     (输入模式)
                     │                             │
硬件行为          控制 LED 亮灭                 检测按键按下/松开
```

---

### 三、代码逐块详解

### 3.1 头文件

```c
#include <linux/module.h>       /* 模块必备：module_init/module_exit/MODULE_LICENSE */
#include <linux/kernel.h>       /* printk 打印内核日志 */
#include <linux/init.h>         /* __init / __exit 宏 */
#include <linux/fs.h>           /* struct file_operations — 把VFS系统调用绑到驱动函数 */
#include <linux/slab.h>         /* kmalloc/kfree（本实验实际未使用） */
#include <linux/uaccess.h>      /* ★ copy_to_user / copy_from_user — 内核与用户空间安全传数据 */
#include <linux/io.h>           /* IO映射（本实验未直接使用） */
#include <linux/cdev.h>         /* cdev_init/cdev_add/cdev_del — 字符设备核心 */
#include <linux/device.h>       /* class_create/device_create — 自动创建设备节点 */
#include <linux/of.h>           /* of_find_node_by_path — 从设备树获取硬件信息 */
#include <linux/of_address.h>   /* 设备树地址映射（本实验未直接使用） */
#include <linux/of_irq.h>       /* 设备树中断（本实验未直接使用） */
#include <linux/gpio.h>         /* ★ GPIO 子系统核心：gpio_request/gpio_direction_input/gpio_get_value */
#include <linux/of_gpio.h>      /* ★ of_get_named_gpio — 从设备树属性解析GPIO编号 */
```

---

### 3.2 宏定义

```c
#define KEY_CNT     1           /* 设备号数量：本驱动只注册 1 个设备 */
#define KEY_NAME    "key"       /* 设备名称 → /dev/key */

#define KEY0VALUE   0xF0        /* ★ 有效按键值：按下并松开后返回给用户的值 */
#define INVAKEY     0x00        /* ★ 无效按键值：没按键时返回的值 */
```

**为什么用 0xF0 和 0x00？**

这是一种**按键编码协议**：
- `0xF0` = 1111 0000 = "按了一次 KEY0"
- `0x00` = "没有有效按键"
- 预留高4位区分不同按键（KEY0=0xF0, KEY1=0xF1, KEY2=0xF2...），后面实验中 `0x80` 位用于区分按下/释放

---

### 3.3 设备结构体

```c
struct key_dev {
    /* ===== 字符设备框架相关（8个标准成员，每个驱动都一样）===== */
    dev_t devid;                /* 设备号 = 主设备号 << 20 | 次设备号 */
    int major;                  /* 主设备号：标识驱动类型 */
    int minor;                  /* 次设备号：区分同一驱动下的不同设备 */
    struct cdev cdev;           /* 内核字符设备结构体（关联 file_operations） */
    struct class *class;        /* 设备类 → /sys/class/key/ */
    struct device *device;      /* 设备实例 → /dev/key */
    struct device_node *nd;     /* 设备树节点指针 → DTS 中 /key 节点 */

    /* ===== 硬件相关成员 ===== */
    int key_gpio;               /* ★ 按键的GPIO编号（从设备树"key-gpios"属性解析） */

    /* ===== 数据存储成员 ===== */
    atomic_t keyvalue;          /* ★ 原子变量：存储当前按键值
                                 *   = 0xF0：有有效按键（按下+松开）
                                 *   = 0x00：无按键
                                 *   用 atomic_t 而非普通 int 的原因：
                                 *   防止读取过程中被中断打断导致数据错误 */
};

struct key_dev key;  /* ★ 全局设备实例（单例）— 整个系统只有一个按键设备 */
```

**对比实验6 LED设备结构体**：

```c
// 实验6（LED输出）                  // 实验12（KEY输入）
struct gpioled_dev {                struct key_dev {
    ...                                ...
    int led_gpio;       // GPIO编号      int key_gpio;        // GPIO编号
    // 没有数据存储成员                  atomic_t keyvalue;   // ★ 需要存储读取到的键值
};                                  };
```

---

### 3.4 key_open — 打开设备

```c
static int key_open(struct inode *inode, struct file *filp)
{
    filp->private_data = &key;  /* ★ 把全局设备指针存到文件的私有数据区
                                  *
                                  * 上下文关系：
                                  * - inode：VFS 索引节点，代表设备文件在磁盘上的元数据
                                  * - filp：  本次打开的文件实例（进程级别的"文件描述符"的内核表示）
                                  * - filp->private_data：void * 指针，给驱动存任何东西
                                  *
                                  * 为什么这样做？
                                  * 后续 key_read/key_release 只能拿到 filp，
                                  * 需要从这里取出设备指针才能访问 key_gpio 和 keyvalue。
                                  * 这是 Linux 驱动最常用的"传递上下文"方式。
                                  */
    return 0;
}
```

**调用链**：
```
用户程序: fd = open("/dev/key", O_RDWR);
  → VFS:   查找 /dev/key 对应的 inode
  → VFS:   创建 struct file (filp)
  → VFS:   调用 key_fops.open = key_open(inode, filp)
  → 驱动:   filp->private_data = &key;   ← 绑定设备到文件
  → 返回:   fd → 用户程序
```

---

### 3.5 key_release — 关闭设备

```c
static int key_release(struct inode *inode, struct file *filp)
{
    /* 本驱动不需要额外清理——按键设备关闭时没状态要恢复
     *
     * 对比 LED 驱动：release 中要释放信号量/互斥体 (实验8~11)
     * 对比后续实验：中断和定时器需要在适当地方释放
     *
     * 这里什么都不做是合理的：
     * - GPIO 方向不变（一直是输入）
     * - 没有被占用状态需要清除
     * - 没有锁需要释放
     */
    return 0;
}
```

---

### 3.6 key_write — 写入设备（空操作）

```c
static ssize_t key_write(struct file *filp, const char __user *buf,
                         size_t count, loff_t *ppos)
{
    int ret = 0;
    /* 按键是纯输入设备，不支持写入——什么也不做
     *
     * 为什么不直接删掉 .write 回调？
     * - 保留空函数体让 file_operations 结构体完整
     * - 如果 .write = NULL，用户调用 write() 会返回 -EINVAL，
     *   但保留空函数可以让 write() 成功返回（不报错），
     *   取决于驱动作者的意图
     */
    return ret;
}
```

---

### 3.7 ★ key_read — 核心：读取按键

这是本实验最重要的函数，逐行详解：

```c
static ssize_t key_read(struct file *filp, char __user *buf,
                        size_t count, loff_t *ppos)
{
    int value;                          /* 临时存储将要传给用户的键值 */
    struct key_dev *dev = filp->private_data;  /* ★ 取回 open 时存入的设备指针
                                                 * 这是整个驱动上下文的"中枢" */
    int ret = 0;

    /* ================================================================
     * 步骤①：读取 GPIO 引脚电平，判断按键是否按下
     * ================================================================
     *
     * gpio_get_value(gpio编号)：
     *   返回 GPIO 引脚当前的逻辑电平：0 = 低电平，1 = 高电平
     *
     * 硬件电路（默认上拉）：
     *   未按下：引脚被上拉到 3.3V → gpio_get_value() = 1
     *   按  下：引脚被拉到 GND     → gpio_get_value() = 0
     *
     * ★ 所以 0 表示"按下"，1 表示"松开/没按"
     */
    if (gpio_get_value(dev->key_gpio) == 0) {   /* 低电平 = 按键按下 */

        /* ================================================================
         * 步骤②：消抖处理（极其简陋的方式）
         * ================================================================
         *
         * while(!gpio_get_value(dev->key_gpio));
         *   含义：只要引脚还是低电平，就不停循环读取
         *   效果：等待按键松开——用户手指抬起来
         *
         * ★ 这段代码的问题（后续实验会解决）：
         *   1. 如果用户一直按着不松手 → 死循环 → 进程卡死在这里
         *   2. 没有真正的消抖：按键刚按下时有机械抖动，
         *      电平会快速跳变(微秒级)，这里等了整整"按下持续期"
         *   3. 占用 CPU 100%（忙等）
         *
         * ★ 正确的消抖方式：
         *   中断 + 定时器（实验14）：
         *     中断检测到边沿 → 启动 20ms 定时器 →
         *     20ms 后抖动早已结束 → 读稳定电平
         */
        while (!gpio_get_value(dev->key_gpio));

        /* ================================================================
         * 步骤③：设置按键值为"有效"
         * ================================================================
         *
         * atomic_set(&dev->keyvalue, KEY0VALUE)：
         *   将 keyvalue 原子地设为 0xF0
         *
         * 为什么用 atomic_set 而不是直接赋值？
         *   在这个实验中，此处不在中断上下文，直接赋值 dev->keyvalue = KEY0VALUE
         *   也可以。但使用 atomic 类型是为后面的中断实验(实验14)做准备——
         *   当中断处理函数和 read() 可能并发访问 keyvalue 时，atomic_t 保证安全。
         */
        atomic_set(&dev->keyvalue, KEY0VALUE);   /* 0xF0 = 有效按键 */
    } else {
        atomic_set(&dev->keyvalue, INVAKEY);     /* 0x00 = 无效按键 */
    }

    /* ================================================================
     * 步骤④：将键值传给用户空间
     * ================================================================
     *
     * value = atomic_read(&dev->keyvalue)：
     *   原子读取 keyvalue 到局部变量 value
     *
     * copy_to_user(buf, &value, sizeof(value))：
     *   把内核空间的数据安全拷贝到用户空间
     *
     *   参数：
     *     buf  — 用户空间目标地址（__user 标记，不能在内核中直接解引用）
     *     &value — 内核空间源地址
     *     sizeof(value) — 拷贝字节数（4 字节，因为 int）
     *
     *   返回值：未能成功拷贝的字节数（0=全部成功，>0=部分失败）
     *   ★ 注意：copy_to_user 返回值是 unsigned long，永不返回负数！
     *     这跟实验中 if(ret < 0) 的写法是有 BUG 的。
     */
    value = atomic_read(&dev->keyvalue);
    ret = copy_to_user(buf, &value, sizeof(value));

    return ret;
}
```

**key_read 的完整状态机**：

```
用户调用 read()
  │
  ▼
gpio_get_value() == 0 ?
  │
  ├── YES（按键按下）
  │     │
  │     │  进入 while 循环—等按键松开
  │     │    ↓
  │     │  按键松开了
  │     │    ↓
  │     └── keyvalue = 0xF0 ──→ copy_to_user() ──→ 用户拿到 0xF0
  │
  └── NO（没按或已松开）
        │
        └── keyvalue = 0x00 ──→ copy_to_user() ──→ 用户拿到 0x00
```

---

### 3.8 file_operations 操作集

```c
static const struct file_operations key_fops = {
    .owner   = THIS_MODULE,    /* ★ 模块引用计数：防止驱动在使用中被 rmmod
                                * 每个 file_operations 都必须设置这个 */
    .write   = key_write,      /* 用户 write() → key_write()（空操作） */
    .open    = key_open,       /* 用户 open()  → key_open()（绑定 private_data） */
    .release = key_release,    /* 用户 close() → key_release()（空操作） */
    /* ★ 注意：没有 .read 回调！那用户怎么读数据？
     *
     * 检查原始 key.c：key_fops 里确实没有 .read = key_read
     * 这意味着 open/write/close 可以用，但 read() 会失败！
     *
     * ★ 这是一个教学代码——key.c 中的 key_fops 是框架模板，
     *   key_read 函数已单独写好，只需手动加到 fops 即可：
     *   .read = key_read,
     *
     *   在完整版本中应该是：
     *   static const struct file_operations key_fops = {
     *       .owner   = THIS_MODULE,
     *       .write   = key_write,
     *       .read    = key_read,       // ★ 加上这行
     *       .open    = key_open,
     *       .release = key_release,
     *   };
     */
};
```

---

### 3.9 keyio_init — GPIO 硬件初始化

```c
/* 函数上下文关系：
 * keyio_init() ← 被 key_init() 调用
 *               ↓
 *          初始化硬件(GPIO)，为 key_read() 读取电平做准备
 */
static int keyio_init(struct key_dev *dev)
{
    int ret = 0;

    /* ① 从设备树查找 /key 节点
     * 对应 DTS 中：key { compatible = "alientek,key"; ... };
     * 这一步建立驱动到设备树节点的连接 */
    dev->nd = of_find_node_by_path("/key");
    if (dev->nd == NULL) {
        ret = -EINVAL;
        goto fail_nd;
    }

    /* ② 从设备树解析 GPIO 编号
     * 对应 DTS 中：key-gpios = <&gpio1 18 GPIO_ACTIVE_LOW>;
     * 得到 GPIO1_IO18 的全局编号（如 50） */
    dev->key_gpio = of_get_named_gpio(dev->nd, "key-gpios", 0);
    if (dev->key_gpio < 0) {
        ret = -EINVAL;
        goto fail_gpio;
    }

    /* ③ 向内核申请 GPIO 使用权
     * 标签 "key0" 会显示在 /sys/kernel/debug/gpio 中 */
    ret = gpio_request(dev->key_gpio, "key0");
    if (ret) {
        ret = -EBUSY;
        printk("IO %d can't request!\r\n", dev->key_gpio);
        goto fail_request;
    }

    /* ④ ★ 设置为输入模式 — 与 LED 驱动的核心区别
     *
     * gpio_direction_input(gpio编号)：
     *   配置 GPIO 方向寄存器为"输入"
     *   之后 gpio_get_value() 才能读取引脚电平
     *
     * 对比 LED：gpio_direction_output(gpio编号, 初始值)
     *   配置 GPIO 方向寄存器为"输出" + 写入初始电平
     */
    ret = gpio_direction_input(dev->key_gpio);
    if (ret < 0) {
        ret = -EINVAL;
        goto fail_input;
    }
    return 0;

/* ===== 错误回滚路径（goto 链，LIFO 逆序释放）===== */
fail_input:
    gpio_free(dev->key_gpio);      /* 释放已申请的 GPIO */
fail_request:
fail_gpio:
fail_nd:
    return ret;
}
```

**GPIO 输入 vs 输出初始化对比**：

```
输出模式（LED）:                       输入模式（KEY）:
gpio_direction_output(gpio, 1)        gpio_direction_input(gpio)
  │                                     │
  ├─ 配方向寄存器 = 输出                 ├─ 配方向寄存器 = 输入
  └─ 写数据寄存器 = 1（初始值）           └─ 之后用 gpio_get_value() 读取
```

---

### 3.10 key_init — 驱动入口函数

这是模块加载时内核调用的函数。流程分**字符设备注册**和**硬件初始化**两个阶段：

```c
static int __init key_init(void)
{
    int ret = 0;

    /* ★ 步骤1：初始化原子变量 keyvalue 为"无效值" */
    atomic_set(&key.keyvalue, INVAKEY);  /* 驱动加载时，还没有按键按下 */

    /* ===== 阶段A：字符设备框架注册 ===== */

    /* 步骤2：注册字符设备号（动态分配） */
    key.major = 0;   /* 0 = 让内核自动分配主设备号 */
    if (key.major) {
        key.devid = MKDEV(key.major, 0);
        ret = register_chrdev_region(key.devid, KEY_CNT, KEY_NAME);
    } else {
        ret = alloc_chrdev_region(&key.devid, 0, KEY_CNT, KEY_NAME);
        key.major = MAJOR(key.devid);    /* 取出内核分配的主设备号 */
        key.minor = MINOR(key.devid);    /* 取出次设备号 */
    }
    if (ret < 0) goto fail_devid;
    printk("key major = %d, minor = %d\r\n", key.major, key.minor);

    /* 步骤3：初始化 cdev 并绑定 file_operations */
    key.cdev.owner = THIS_MODULE;
    cdev_init(&key.cdev, &key_fops);
    /* 内部：cdev->ops = &key_fops → 用户 open/read/write 会调用这些回调 */

    /* 步骤4：添加 cdev 到内核 → 设备正式"上线" */
    ret = cdev_add(&key.cdev, key.devid, KEY_CNT);
    if (ret) goto fail_cdevadd;

    /* 步骤5：创建设备类 → /sys/class/key/ */
    key.class = class_create(THIS_MODULE, KEY_NAME);
    if (IS_ERR(key.class)) {
        ret = PTR_ERR(key.class);
        goto fail_class;
    }

    /* 步骤6：创建设备实例 → 触发 udev/mdev 自动生成 /dev/key */
    key.device = device_create(key.class, NULL, key.devid, NULL, KEY_NAME);
    if (IS_ERR(key.device)) {
        ret = PTR_ERR(key.device);
        goto fail_device;
    }

    /* ===== 阶段B：硬件初始化 ===== */

    /* 步骤7：初始化按键 GPIO（设置输入模式） */
    ret = keyio_init(&key);
    if (ret < 0) {
        goto fail_device;    /* 失败时跳转，前面注册的字符设备框架也要回滚 */
    }

    return 0;   /* 一切就绪！/dev/key 已可用 */

/* ===== 错误回滚路径 ===== */
fail_device:
    class_destroy(key.class);          /* 逆序：先销毁类 */
fail_class:
    cdev_del(&key.cdev);              /* 再删除 cdev */
fail_cdevadd:
    unregister_chrdev_region(key.devid, KEY_CNT);  /* 最后释放设备号 */
fail_devid:
    return ret;
}
```

**初始化步骤的顺序不能乱**：

```
字符设备框架先搭好     → 然后才能初始化硬件
                      
顺序：                因为：
① 初始化 atomic       keyio_init 需要 dev->nd 等字段可用
② 注册设备号           如果硬件失败，goto 回滚需要框架已就绪
③ cdev_init
④ cdev_add             框架→硬件的顺序保证了错误回滚的一致性
⑤ class_create
⑥ device_create        如果硬件失败(goto fail_device)，
⑦ keyio_init           会从类/设备开始逆序清理
```

---

### 3.11 key_exit — 驱动出口函数

```c
static void __exit key_exit(void)
{
    /* 释放顺序 = 初始化的严格逆序（LIFO） */

    /* ① 删除 cdev → 停止接收新的 open() */      cdev_del(&key.cdev);
    /* ② 释放设备号 */                         unregister_chrdev_region(key.devid, KEY_CNT);
    /* ③ 销毁 /dev/key */                      device_destroy(key.class, key.devid);
    /* ④ 销毁 /sys/class/key/ */                class_destroy(key.class);
    /* ⑤ 释放 GPIO（告诉内核此引脚不再被使用） */  gpio_free(key.key_gpio);
    /* ★ 注意：atomic_t keyvalue 在模块内存中，卸载时自动释放，不需要手动清理 */
}
```

---

### 3.12 模块注册

```c
module_init(key_init);      /* insmod → 内核调用 key_init() */
module_exit(key_exit);      /* rmmod  → 内核调用 key_exit() */
MODULE_LICENSE("GPL");      /* 许可证：GPL，必须！否则内核被"污染" */
MODULE_AUTHOR("zuozhongkai"); /* 作者信息 → modinfo 可查看 */
```

---

### 四、用户程序 keyAPP.c 详解

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>          /* open() */
#include <stdio.h>          /* printf() */
#include <unistd.h>         /* read() / close() */
#include <stdlib.h>
#include <string.h>

#define KEY0VALUE  0xF0    /* 必须与驱动中的定义一致！这是驱动和应用的"协议" */
#define INVAKEY    0x00

int main(int argc, char *argv[])
{
    int value = 0;         /* 存储从驱动读到的按键值 */
    int fd, retvalue;
    char *filename;

    if (argc != 2) {
        printf("Error Usage!\r\n");
        return -1;
    }

    filename = argv[1];    /* 设备文件名：/dev/key */

    /* ① 打开设备 */
    fd = open(filename, O_RDWR);
    if (fd < 0) {
        printf("file %s open failed!\r\n", filename);
        return -1;
    }

    /* ② 循环读取按键值 */
    while (1) {
        read(fd, &value, sizeof(value));    /* 调用驱动的 key_read() */
        /*                                          ↓
         *                  驱动返回 value = 0xF0（有按键）或 0x00（无按键）
         */
        if (value == KEY0VALUE) {
            printf("KEY0 Press, value = %d\r\n", value);
        }
    }

    /* ③ 关闭设备（实际上永远不会执行到这里，因为 while(1) 是死循环） */
    close(fd);
    return 0;
}
```

**用户程序与驱动的调用关系**：

```
keyAPP.c                              key.c (驱动)
────────                              ────────────
open("/dev/key")      ─────────────→  key_open()
                        filp->private_data = &key

read(fd, &value, 4)   ─────────────→  key_read()
                        gpio_get_value() → 读硬件
                        atomic_set()     → 存键值
                        copy_to_user()   → 传回用户空间
                    ←─────────────────
                    value = 0xF0 或 0x00

close(fd)             ─────────────→  key_release()
```

---

### 五、关键知识点总结

### 5.1 GPIO 输入 vs 输出总结

| | 输出（LED） | 输入（KEY） |
|---|---|---|
| **方向设置** | `gpio_direction_output(gpio, init_val)` | `gpio_direction_input(gpio)` |
| **运行时操作** | `gpio_set_value(gpio, 0/1)` — 写电平 | `gpio_get_value(gpio)` — 读电平 |
| **数据拷贝** | `copy_from_user()` — 用户→内核 | `copy_to_user()` — 内核→用户 |
| **VFS 回调** | `.write = led_write` | `.read = key_read` |
| **用户系统调用** | `write(fd, buf, len)` | `read(fd, buf, len)` |

### 5.2 copy_from_user vs copy_to_user

```c
// 输出设备：用户→内核
copy_from_user(kernel_buf, user_buf, count);
//   从用户空间拷到内核空间

// 输入设备：内核→用户
copy_to_user(user_buf, kernel_buf, count);
//   从内核空间拷到用户空间
```

两个函数都会检查用户空间地址的合法性（防止恶意传非法指针导致内核崩溃），如果地址非法，返回未成功拷贝的字节数而不是崩溃。

### 5.3 本实验的不足（为后续实验铺垫）

| 问题 | 后果 | 解决（后续实验） |
|---|---|---|
| `while(!gpio_get_value())` 忙等 | CPU 100% 空转 | 实验14：中断方式 |
| 无消抖 | 可能读到抖动信号 | 实验14：定时器 20ms 消抖 |
| 用户程序 `while(1) read()` | 用户态 CPU 也空转 | 实验15：阻塞 IO |
| 无并发保护 | 多进程打开可同时读 | 实验8~11：互斥机制 |
| key_fops 缺少 `.read` | 用户 read() 实际不可用 | 需手动加 `.read = key_read` |

---

### 六、函数调用关系图

```
insmod                                     rmmod
  │                                          │
  ▼                                          ▼
key_init()                               key_exit()
  │                                          │
  ├─ atomic_set(&keyvalue, INVAKEY)          ├─ cdev_del()
  ├─ alloc_chrdev_region()                   ├─ unregister_chrdev_region()
  ├─ cdev_init(&cdev, &key_fops)             ├─ device_destroy()
  ├─ cdev_add()                              ├─ class_destroy()
  ├─ class_create()                          └─ gpio_free()
  ├─ device_create()
  └─ keyio_init()
       ├─ of_find_node_by_path("/key")
       ├─ of_get_named_gpio()
       ├─ gpio_request()
       └─ gpio_direction_input()

用户程序运行期间：
  open()  → key_open()    → filp->private_data = &key
  read()  → key_read()    → gpio_get_value() → copy_to_user()
  close() → key_release() → (空)
```

---

*文档创建时间：2026年6月9日*
*基于正点原子阿尔法IMX6ULL Linux驱动开发教程 实验12*

---

## 第十四章 内核定时器

---

### 一、实验定位

本实验是正点原子 Linux 驱动教程的一个**重要转折点**：

```
实验6~11（LED 输出）
  → 实验12（按键输入 — GPIO 方向第一次反转）
    → ★ 实验13（内核定时器 — 让内核替你干活，而不是你 while 忙等）
      → 实验14（中断 — 从轮询变为硬件通知）
        → 实验15（阻塞 IO — 从死循环变为睡眠唤醒）
```

**一句话总结：学会让 Linux 内核定时器自动做周期性工作——把"忙等"和"死循环"的责任从你的代码转移到内核。**

---

### 二、本实验解决了什么问题

实验12（按键）的核心问题是 **while 忙等**：

```c
// 实验12 key_read() 中的问题代码
if (gpio_get_value(dev->key_gpio) == 0) {     // 按下了
    while (!gpio_get_value(dev->key_gpio));    // ← CPU 100% 空转等松开！
    keyvalue = 0xF0;
}
```

实验13 展示了一个更好的方案：

```c
// 实验13：内核定时器自动触发 LED 翻转
init_timer(&timer);                    // 初始化
timer.function = timer_func;          // 设置回调
add_timer(&timer);                    // 启动→到期→回调→mod_timer→再次到期...
```

**核心思想变化：**

| 模式 | 描述 | 实验 |
|------|------|------|
| 忙等轮询 | 反复检查"I/O 好了没?" — 耗 CPU | 实验12 按键 |
| 定时回调 | 内核到时间了自动叫你 — CPU 高效 | 实验13 ★ |

---

### 三、本实验必须掌握的核心知识点

### 3.1 内核定时器 (struct timer_list)

```
定时器的 5 个操作 → 形成完整生命周期：

  init_timer()         初始化（出厂设置）
       ↓
  add_timer()          启动（放入系统定时器队列）
       ↓
  ┌─[到期] → 内核调用 timer.function(timer.data)  ← 回调
  │    ↓
  │ mod_timer()         重新设置超时时间（续命）
  │    ↓                （不调用的话定时器只触发一次）
  └── 循环
       ↓
  del_timer()          停止（从队列中移除）
  del_timer_sync()     安全停止（等回调执行完）
```

**关键理解：内核的定时器是"单次定时器"。要变成周期性定时器，必须在回调函数中自己调 `mod_timer()` 重新注册自己！**

### 3.2 jiffies — 内核的"心跳计数器"

```
jiffies 是一个全局变量，记录自系统启动以来的"节拍"总数。

每个时钟中断 → jiffies++
CONFIG_HZ = 100（默认） → 1秒 100 拍 → 每拍 10ms

                   HZ=100     HZ=250     HZ=1000
1秒 =              100 jf     250 jf     1000 jf
1拍 =              10ms       4ms        1ms
500ms =            50 jf      125 jf     500 jf
```

**必须使用的转换函数（别自己算）：**

```c
msecs_to_jiffies(500)    // 毫秒 → jiffies
usecs_to_jiffies(5000)   // 微秒 → jiffies
jiffies_to_msecs(50)     // jiffies → 毫秒
```

### 3.3 ioctl — 第三大系统调用

前面实验只用了 `read/write`，本实验引入 `ioctl`：

```
        方向        特点              典型场景
read    驱动→用户   被动收数据          按键值、传感器值
write   用户→驱动   主动写数据          控制 LED 亮灭
ioctl   双向/无    发命令（可带数据）   打开/关闭功能、设参数
```

**ioctl 命令码的构造规则：**

```
每个命令码是一个 32 位整数，由四个字段拼成：

  ┌──── type(8bit) ────┬── nr(8bit) ──┬─ dir(2bit) ─┬── size(14bit) ──┐
     魔数：0xEF            编号：1/2/3    方向           参数大小
```

**三个构造宏：**

| 宏 | 含义 | 使用场景 | 示例 |
|----|------|---------|------|
| `_IO(type, nr)` | 纯命令，不传数据 | 开关定时器 | `_IO(0xEF, 1)` |
| `_IOW(type, nr, type)` | 写命令，用户→驱动 | 设周期 | `_IOW(0xEF, 3, int)` |
| `_IOR(type, nr, type)` | 读命令，驱动→用户 | 读状态 | `_IOR(0xEF, 6, int)` |

### 3.4 定时器回调函数的上下文限制 ★★★

这是最容易被忽略但其实最关键的知识点：

```
定时器回调(timer_func) 运行在 → 软中断（softirq）上下文

绝对不能做的事：                 可以做的事：
  ✗ 睡眠/延时                     ✓ gpio_set_value()
  ✗ 调用 copy_to_user()          ✓ mod_timer()
  ✗ kmalloc(GFP_KERNEL)          ✓ printk()（慎用）
  ✗ mutex_lock()                 ✓ spin_lock()
  ✗ 访问 current（无意义）        ✓ atomic_xxx()
```

**为什么这是面试重点？** 因为很多驱动 bug 就是在定时器回调中调了 `copy_to_user()` 导致内核 oops。

---

### 四、驱动代码核心流程

### 4.1 初始化流程

```
insmod timer.ko
  │
  └→ timer_init()
       ├─ 阶段A：注册字符设备框架（和实验6~12 完全一样）
       │    ├─ alloc_chrdev_region()        → 申请设备号
       │    ├─ cdev_init() + cdev_add()     → 注册字符设备
       │    ├─ class_create()               → /sys/class/timer/
       │    └─ device_create()              → /dev/timer
       │
       ├─ 阶段B：初始化 LED 硬件
       │    └─ led_init()
       │         ├─ of_find_node_by_path("/gpioled")
       │         ├─ of_get_named_gpio()
       │         ├─ gpio_request()
       │         └─ gpio_direction_output(led_gpio, 1)  ← 默认关灯
       │
       └─ 阶段C：★★ 初始化定时器
            ├─ init_timer(&timerdev.timer)
            ├─ timeperiod = 500                ← 默认 500ms
            ├─ timer.function = timer_func     ← 绑定回调
            ├─ timer.expires = jiffies + msecs_to_jiffies(500)
            ├─ timer.data = (unsigned long)&timerdev
            └─ add_timer(&timerdev.timer)      ← 启动！
```

### 4.2 运行期间的事件循环

```
add_timer() 启动
       │
       ▼
   ┌──── 等 500ms ────┐
   │                  │
   │ 时钟中断 jiffies++ → 检查到期
   │                  │
   ▼                  │
定时器到期！           │
   │                  │
   ▼                  │
timer_func(arg)        │
  ├─ 取设备指针         │
  ├─ sta = !sta        │
  ├─ gpio_set_value()  │  LED 翻转（亮→灭 或 灭→亮）
  └─ mod_timer(...) ──┘  重新注册自己（循环！）
```

### 4.3 用户通过 ioctl 控制

```
用户输入命令:

  cmd=1（关闭）
    → ioctl(fd, CLOSE_CMD, &arg)
      → 驱动 timer_ioctl() → del_timer_sync()
      → LED 停闪

  cmd=2（打开）
    → ioctl(fd, OPEN_CMD, &arg)
      → 驱动 timer_ioctl() → mod_timer()
      → LED 恢复闪烁

  cmd=3（设周期）
    → 输入新周期值（如 200ms）
    → ioctl(fd, SETPERIOD_CMD, &arg)
      → 驱动 timer_ioctl() → copy_from_user(&value, arg, 4)
      → timeperiod = value
      → mod_timer(...) 用新周期重启
      → LED 按新频率闪烁
```

### 4.4 卸载流程

```
rmmod timer
  │
  └→ timer_exit()
       ├─ gpio_set_value(led_gpio, 1)       ← 先关灯
       ├─ del_timer(&timerdev.timer)         ← 停定时器
       ├─ cdev_del() + unregister...()       ← 注销字符设备
       ├─ device_destroy() + class_destroy() ← 删除设备节点
       └─ gpio_free(led_gpio)                ← 释放 GPIO
```

---

### 五、与之前实验的逐项对比

### 5.1 与实验12（按键）的对比

| 维度 | 实验12（按键）| 实验13（定时器）|
|------|-------------|----------------|
| GPIO 方向 | **输入** `gpio_direction_input()` | **输出** `gpio_direction_output()` |
| 数据操作 | `gpio_get_value()` 读 | `gpio_set_value()` 写 |
| 数据传输 | `copy_to_user()` 内核→用户 | `copy_from_user()` 用户→内核（经 ioctl）|
| 系统调用 | `read()` | `ioctl()` |
| file_ops | .open/.read/.write/.release | .open/.unlocked_ioctl/.release |
| 管腿 | 按键（/key 节点）| LED（/gpioled 节点）|
| 触发机制 | 用户调用 read 时读电平 | 定时器自动回调 |
| CPU 效率 | 忙等耗 CPU | 内核调度，高效 |

### 5.2 与实验6~11（LED 字符设备）的对比

| 维度 | 实验6~11（LED）| 实验13（定时器LED）|
|------|-------------|----------------|
| 用户操作 | write() 主动写值 | ioctl() 发命令配置 |
| 控制方式 | 用户手动控制 | 定时器自动控制 |
| LED 闪烁 | 用户程序 while+sleep | 内核定时器自动 |
| 新东西 | （逐步加并发控制）| 定时器 + ioctl |

### 5.3 file_operations 对比一览

```
实验6~11（LED）:       实验12（按键）:        实验13（定时器）:
.open   = led_open     .open   = key_open    .open    = timer_open
.release= led_release  .release= key_release .release = timer_release
.write  = led_write    .read   = key_read    .unlocked_ioctl = timer_ioctl
                       .write  = key_write
```

---

### 六、各函数职责速查表

### timer.c 函数

| 函数 | 所属阶段 | 一句话职责 |
|------|---------|-----------|
| `timer_open()` | 运行期 | 把 `&timerdev` 塞进 `filp->private_data` |
| `timer_release()` | 运行期 | 空函数（无资源释放） |
| `timer_ioctl()` | ★运行期 | 接收 ioctl 命令，控制定时器启停和周期 |
| `timer_func()` | ★中断上下文 | 定时器回调：翻转 LED → mod_timer 循环 |
| `led_init()` | 初始化 | 找设备树 /gpioled 节点 → 设为 GPIO 输出 |
| `timer_init()` | 初始化 | 字符设备 + LED 硬件 + 定时器，三步初始化 |
| `timer_exit()` | 卸载 | 关灯 → 删定时器 → 注销字符设备 → 释放 GPIO |

### timerAPP.c 函数

| 函数 | 职责 |
|------|------|
| `main()` | 打开 `/dev/timer` → 循环读用户命令 → `ioctl()` 发命令 |

### ioctl 命令

| 命令 | 宏 | 作用 | 驱动调用 |
|------|-----|------|---------|
| CLOSE_CMD(1) | `_IO(0xEF, 1)` | 关闭定时器 | `del_timer_sync()` |
| OPEN_CMD(2) | `_IO(0xEF, 2)` | 打开定时器 | `mod_timer()` |
| SETPERIOD_CMD(3) | `_IOW(0xEF, 3, int)` | 设置周期 | `copy_from_user()` + `mod_timer()` |

### 定时器 API 速查

| API | 一句话 |
|-----|--------|
| `init_timer(&t)` | 初始化定时器结构体 |
| `add_timer(&t)` | 放入系统队列，启动 |
| `mod_timer(&t, expires)` | 修改到期时间（或重新激活） |
| `del_timer(&t)` | 从队列移除（不等待回调） |
| `del_timer_sync(&t)` | 安全删除（等回调执行完） |
| `timer_pending(&t)` | 定时器是否在队列中？ |

---

### 七、关键概念一页纸

```
┌─────────────────────────────────────────────────────────────────┐
│                    jiffies 与定时器的关系                         │
│                                                                 │
│  时钟中断 (每 10ms 一次)                                         │
│      │                                                          │
│      ├→ jiffies++       ← 内核节拍计数器，永远只增不减            │
│      │                                                          │
│      └→ 检查定时器链表                                            │
│           │                                                     │
│           ├→ t->expires <= jiffies ?                            │
│           │     NO  → 跳过，此定时器还没到时间                     │
│           │     YES → 从链表中取出定时器                           │
│           │            → 发出 TIMER_SOFTIRQ                      │
│           │            → 软中断处理函数执行 t->function(t->data)   │
│           │            → 定时器从队列中移除（不再自动重复）          │
│                                                                 │
│  所以：要持续闪烁 → 必须在回调末尾调 mod_timer 重新排队！           │
└─────────────────────────────────────────────────────────────────┘
```

---

### 八、后续实验的铺垫

本实验用定时器展示了"周期性自动触发"的模式，但还有两个问题没解决：

| 本实验的不足 | 表现 | 后续解决 |
|------------|------|---------|
| 定时器回调在软中断上下文 | 不能 sleep、不能 copy_to_user | 实验14：中断 + tasklet/workqueue |
| 用户程序仍需 while(1) 等命令 | 进程一直跑着 | 实验15：阻塞IO（等待队列） |
| 只有一个 LED 自动闪烁 | 按键检测仍需轮询 | 实验14：中断检测按键 |

**实验13→14→15 这条线就是："从轮询到中断，从忙等到阻塞"——这是嵌入式 Linux 驱动最核心的一条进化路线。**

---

### 九、文件说明

| 文件 | 位置 | 说明 |
|------|------|------|
| `timer.c` | WSL `/home/lenovo/13_timer/` | 驱动源码（完整注释版） |
| `timerAPP.c` | WSL `/home/lenovo/13_timer/` | 测试程序源码（完整注释版） |
| `timer_temp.c` | WSL `/home/lenovo/13_timer/` | 字符设备框架模板（无定时器功能） |
| `Makefile` | WSL `/home/lenovo/13_timer/` | 编译脚本 |

---
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




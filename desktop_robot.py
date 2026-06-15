#!/usr/bin/env python3
"""
桌面学习机器人 — 弹窗显示今日任务 + 语音播报
用法：python desktop_robot.py
"""

import datetime
import sys
import io
import threading
import tkinter as tk
from tkinter import ttk

# 解决 Windows 终端 GBK 编码问题
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ============================================================
# 各阶段配置
# ============================================================

PHASES = [
    {
        "name": "暑假冲刺 — 阶段一",
        "start": "2026-06-15",
        "end": "2026-08-31",
        "weekday_tasks": [
            "上午（3h）：写项目代码 — IMU I2C驱动 → 超声波中断驱动 → PWM舵机 → ROS2集成",
            "下午（2h）：补实验（中断/I2C/阻塞IO）+ 调试 + 掌握ftrace和GDB",
            "晚上（1.5h）：C++ STL+面向对象 → ARM基础 → OS八股（30min）",
            "碎片时间：小林coding OS八股，每天2到3个知识点，要能口述出来",
        ],
        "weekend_tasks": [
            "整理代码 push GitHub，写踩坑博文",
            "OS八股继续查漏补缺",
        ],
        "daily": ["LeetCode 每天1道（代码随想录 / CodeTop / 力扣hot100）"],
    },
    {
        "name": "开题准备期",
        "start": "2026-09-01",
        "end": "2026-10-31",
        "weekday_tasks": [
            "写文献综述（3000字，中15到20篇+英20篇，近3年文献占一半以上）",
            "阶段一收尾：GitHub README写漂亮，截性能图",
            "计网八股：小林coding网络篇，跳过HTTP章",
            "LeetCode每天1道",
            "写好简历（中英文两版）",
        ],
        "weekend_tasks": [
            "继续文献综述 + LeetCode + 阶段一收尾",
        ],
        "daily": ["开题答辩是11月，提前准备好PPT和讲稿"],
    },
    {
        "name": "日常实习 + 阶段二并行",
        "start": "2026-11-01",
        "end": "2027-02-28",
        "weekday_tasks": [
            "周中白天：上班，BSP/驱动相关岗位",
            "周中晚上：八股30min + LeetCode 1道",
        ],
        "weekend_tasks": [
            "周末：阶段二 DMA / mmap 零拷贝，降速但不要停",
            "碎片：设计模式 + 序列化 + Bootloader概念",
        ],
        "daily": ["你正在实习，保持节奏，周末不要荒废阶段二"],
    },
    {
        "name": "暑期实习招聘 + 阶段二收尾",
        "start": "2027-03-01",
        "end": "2027-05-31",
        "weekday_tasks": [
            "投简历+面试：地平线/大疆/影石/拓竹/小马智行/字节机器人",
            "阶段二收尾：性能对比数据 + 延迟测试报告",
            "LeetCode强化 + 八股冲刺",
        ],
        "weekend_tasks": [
            "阶段二收尾 + 面试准备 + 八股冲刺",
        ],
        "daily": ["暑期实习3到5月集中投递，拿到offer秋招就有了保底"],
    },
    {
        "name": "暑期实习 + 阶段三起步",
        "start": "2027-07-01",
        "end": "2027-08-31",
        "weekday_tasks": [
            "周中白天：暑期实习，努力争取转正",
            "周中晚上：阶段三 NPU驱动框架",
        ],
        "weekend_tasks": [
            "周末：阶段三 NPU字符设备 + ioctl + poll + 异步推理流水线",
        ],
        "daily": ["转正offer是秋招最好的保底，认真对待实习"],
    },
    {
        "name": "秋招正式批",
        "start": "2027-09-01",
        "end": "2027-11-30",
        "weekday_tasks": [
            "投递+面试：大疆/影石/拓竹/地平线/字节机器人/小马智行",
            "晚上：阶段三继续 + 论文素材整理",
        ],
        "weekend_tasks": [
            "面试复盘 + 阶段三收尾 + 论文写作",
        ],
        "daily": ["秋招最后冲刺，目标SSP 45万到60万以上"],
    },
]

MILESTONES = [
    ("M0", "2026-06-30", "硬件到货 + GitHub建立 + ROS2环境搭好"),
    ("M1", "2026-08-31", "阶段一完成：传感器+ROS2全面跑通"),
    ("M1.5", "2026-10-31", "开题答辩通过 + 简历完成 + 投出第一份实习"),
    ("M2", "2027-02-28", "阶段二DMA+mmap跑通 + 日常实习满3个月"),
    ("M2.5", "2027-05-31", "阶段二完整产出 + 拿到暑期实习offer"),
    ("M3", "2027-08-31", "暑期转正offer + 阶段三NPU框架搭好"),
    ("M4", "2027-11-30", "秋招SSP offer 目标45到60万以上"),
    ("M5", "2028-03-31", "硕士论文终稿 + 答辩通过"),
]

TIPS = [
    "驱动作完就投实习，别等完美。第一段日常实习是整个飞轮的启动器。",
    "你的核心竞争力是掌握了数据在硅片与物理世界之间穿梭的规则。",
    "211本+985硕控制 + DMA/mmap深度 + ROS2中间件 = 2027秋招SSP有力竞争者。",
]

# ============================================================
# 核心逻辑
# ============================================================

def find_phase(today):
    for p in PHASES:
        start = datetime.date.fromisoformat(p["start"])
        end = datetime.date.fromisoformat(p["end"])
        if start <= today <= end:
            return p
    return None

def find_upcoming_milestones(today, n=3):
    upcoming = []
    for name, date_str, desc in MILESTONES:
        d = datetime.date.fromisoformat(date_str)
        if d >= today:
            upcoming.append((name, date_str, desc, (d - today).days))
    return sorted(upcoming, key=lambda x: x[3])[:n]

def is_weekend(today):
    return today.weekday() >= 5

def speak(text):
    """使用 Windows SAPI 语音合成"""
    try:
        import win32com.client
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Rate = -1  # 语速稍慢，更清晰
        speaker.Volume = 100
        speaker.Speak(text)
    except ImportError:
        print("  [语音模块未安装 pip install pywin32]")
    except Exception as e:
        print(f"  [语音播报失败: {e}]")

def build_message(today, phase):
    """构建今日任务文本"""
    lines = []
    weekday = "周末" if is_weekend(today) else "工作日"
    lines.append(f"今天是{today.year}年{today.month}月{today.day}日，{today.strftime('%A')}。")
    lines.append(f"当前阶段：{phase['name']}。")

    tasks = phase["weekend_tasks"] if is_weekend(today) else phase["weekday_tasks"]
    lines.append("今日任务：")
    for t in tasks:
        lines.append(t)

    if phase.get("daily"):
        for d in phase["daily"]:
            lines.append(d)

    # 里程碑
    milestones = find_upcoming_milestones(today)
    if milestones:
        name, date_str, desc, days_left = milestones[0]
        lines.append(f"距离最近的里程碑 {name} 还有 {days_left} 天：{desc}")

    return lines


# ============================================================
# GUI 弹窗
# ============================================================

class RobotWindow:
    def __init__(self, today, phase, message_lines):
        self.root = tk.Tk()
        self.root.title("🤖 学习机器人 — 今日提醒")
        self.root.geometry("620x520")
        self.root.resizable(False, False)

        # 居中
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - 620) // 2
        y = (sh - 520) // 2
        self.root.geometry(f"+{x}+{y}")

        # 始终置顶
        self.root.attributes("-topmost", True)

        # 样式
        style = ttk.Style()
        style.theme_use("clam")

        # 主框架
        main = ttk.Frame(self.root, padding=20)
        main.pack(fill="both", expand=True)

        # 标题
        title = ttk.Label(
            main,
            text=f"🤖 学习机器人",
            font=("Microsoft YaHei", 18, "bold"),
        )
        title.pack(pady=(0, 5))

        # 日期和阶段
        info = ttk.Label(
            main,
            text=f"{today.year}年{today.month}月{today.day}日  {today.strftime('%A')}  |  {phase['name']}",
            font=("Microsoft YaHei", 11),
            foreground="#555",
        )
        info.pack(pady=(0, 15))

        # 分隔线
        sep = ttk.Separator(main, orient="horizontal")
        sep.pack(fill="x", pady=5)

        # 任务列表
        task_label = ttk.Label(
            main,
            text="📋 今日任务",
            font=("Microsoft YaHei", 13, "bold"),
        )
        task_label.pack(anchor="w", pady=(10, 5))

        task_frame = ttk.Frame(main)
        task_frame.pack(fill="both", expand=True, pady=(0, 10))

        task_text = tk.Text(
            task_frame,
            font=("Microsoft YaHei", 10),
            wrap="word",
            height=10,
            borderwidth=0,
            padx=10,
            pady=10,
            bg="#f8f8f8",
        )
        task_text.pack(fill="both", expand=True)

        for line in message_lines:
            task_text.insert("end", f"  • {line}\n")
        task_text.config(state="disabled")

        # 里程碑
        milestones = find_upcoming_milestones(today, n=2)
        if milestones:
            ms_label = ttk.Label(
                main,
                text="⏰ 即将到来的里程碑",
                font=("Microsoft YaHei", 13, "bold"),
            )
            ms_label.pack(anchor="w", pady=(5, 5))

            ms_frame = ttk.Frame(main)
            ms_frame.pack(fill="x")

            for name, date_str, desc, days_left in milestones:
                urgency = "🔴" if days_left <= 14 else ("🟡" if days_left <= 30 else "🟢")
                ms_item = ttk.Label(
                    ms_frame,
                    text=f"{urgency} {name} | {date_str} | 还剩{days_left}天 | {desc}",
                    font=("Microsoft YaHei", 9),
                    foreground="#333",
                )
                ms_item.pack(anchor="w")

        # 底部按钮
        btn_frame = ttk.Frame(main)
        btn_frame.pack(fill="x", pady=(15, 0))

        speak_btn = ttk.Button(
            btn_frame,
            text="🔊 再播报一次",
            command=lambda: self.speak_thread(message_lines),
        )
        speak_btn.pack(side="left", padx=(0, 10))

        close_btn = ttk.Button(
            btn_frame,
            text="✓ 知道了",
            command=self.root.destroy,
        )
        close_btn.pack(side="right")

        # 首次自动播报
        self.root.after(500, lambda: self.speak_thread(message_lines))

    def speak_thread(self, lines):
        """在后台线程中播报"""
        text = "。".join(lines)
        t = threading.Thread(target=speak, args=(text,), daemon=True)
        t.start()

    def run(self):
        self.root.mainloop()


# ============================================================
# 入口
# ============================================================

def main():
    today = datetime.date.today()
    phase = find_phase(today)

    if phase is None:
        print("当前日期不在学习阶段范围内")
        return

    lines = build_message(today, phase)
    RobotWindow(today, phase, lines).run()


if __name__ == "__main__":
    main()

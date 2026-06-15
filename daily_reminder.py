#!/usr/bin/env python3
"""
每日学习提醒 — 根据 学习路线.md 中的阶段和节奏，提醒今天该干什么。
用法：python daily_reminder.py
开机自启：把本脚本的快捷方式放到 shell:startup 目录
"""

import datetime
import sys
import os
import io

# 解决 Windows 终端 GBK 编码问题
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ============================================================
# 配置：各阶段的时间窗口和每日节奏
# ============================================================

PHASES = [
    {
        "name": "暑假冲刺 — 阶段一",
        "start": "2026-06-15",
        "end": "2026-08-31",
        "weekday_plan": {
            "上午（3h）": "写项目代码：IMU I2C驱动 → 超声波中断驱动 → PWM舵机 → ROS2集成",
            "下午（2h）": "补实验（中断/I2C/阻塞IO）+ 调试 + ftrace/GDB调试工具",
            "晚上（1.5h）": "C++ STL+面向对象（前2周）→ ARM基础（1周）→ OS八股（每晚30min）",
            "碎片（30min）": "小林coding OS八股，每天2~3个知识点，口述能讲清楚",
        },
        "weekend_plan": {
            "全天": "整理代码 push GitHub，写踩坑博文",
            "碎片（30min）": "OS八股继续，查漏补缺",
        },
    },
    {
        "name": "开题准备期",
        "start": "2026-09-01",
        "end": "2026-10-31",
        "weekday_plan": {
            "白天（40%）": "写文献综述（3000字，中15~20篇+英20篇，近3年文献占50%~80%）",
            "白天（20%）": "阶段一收尾 + GitHub README写漂亮 + 截性能图",
            "白天（20%）": "计网八股（小林coding 网络篇，跳HTTP章）",
            "白天（10%）": "LeetCode 每天1道",
            "白天（10%）": "写好简历（中英文两版）",
        },
        "weekend_plan": {
            "全天": "继续文献综述 + LeetCode + 阶段一收尾",
        },
    },
    {
        "name": "日常实习 + 阶段二并行",
        "start": "2026-11-01",
        "end": "2027-02-28",
        "weekday_plan": {
            "周中白天": "上班（打杂也去，优先BSP/驱动相关）",
            "周中晚上": "八股30min + LeetCode 1道",
        },
        "weekend_plan": {
            "周末": "阶段二 DMA/mmap 零拷贝（降速但不停）",
            "碎片": "设计模式 + 序列化 + Bootloader概念 按需补",
        },
    },
    {
        "name": "暑期实习招聘 + 阶段二收尾",
        "start": "2027-03-01",
        "end": "2027-05-31",
        "weekday_plan": {
            "优先级1": "投简历+面试（暑期实习：地平线/大疆/影石/拓竹/小马/字节）",
            "优先级2": "阶段二收尾（性能对比数据 + 延迟测试报告）",
            "优先级3": "LeetCode + 八股继续",
        },
        "weekend_plan": {
            "全天": "阶段二收尾 + 面试准备 + 八股冲刺",
        },
    },
    {
        "name": "暑期实习 + 阶段三起步",
        "start": "2027-07-01",
        "end": "2027-08-31",
        "weekday_plan": {
            "周中白天": "暑期实习（争取转正 → 秋招保底offer）",
            "周中晚上": "阶段三 NPU驱动框架",
        },
        "weekend_plan": {
            "周末": "阶段三：NPU字符设备 + ioctl + poll + 异步推理流水线",
        },
    },
    {
        "name": "秋招正式批",
        "start": "2027-09-01",
        "end": "2027-11-30",
        "weekday_plan": {
            "全天": "秋招冲刺：大疆/影石/拓竹/地平线/字节机器人/小马智行",
            "晚上": "阶段三继续 + 论文素材整理",
        },
        "weekend_plan": {
            "全天": "面试复盘 + 阶段三收尾 + 论文写作",
        },
    },
]

MILESTONES = [
    ("🏁 M0", "2026-06-30", "硬件到货 + GitHub repo建立 + ROS2环境搭好"),
    ("🏁 M1", "2026-08-31", "阶段一完成：传感器+PWM+ROS2 全面跑通，GitHub有commit+截图"),
    ("🏁 M1.5", "2026-10-31", "开题答辩通过 + 简历完成 + 投出第一份实习"),
    ("🏁 M2", "2027-02-28", "阶段二核心通路跑通（DMA+mmap）+ 日常实习满3个月"),
    ("🏁 M2.5", "2027-05-31", "阶段二完整产出（延迟测试报告）+ 拿到暑期实习offer"),
    ("🏁 M3", "2027-08-31", "暑期实习转正offer（秋招保底）+ 阶段三NPU框架搭好"),
    ("🏁 M4", "2027-11-30", "秋招SSP offer（目标45w~60w+）"),
    ("🏁 M5", "2028-03-31", "硕士论文终稿 + 答辩"),
]

WEEKLY_LEETCODE = "LeetCode 每天1道（代码随想录 / CodeTop / 力扣hot100）"
WEEKLY_BAGU = "八股每日30min（C++/OS/计网/ARM，能口述）"

# ============================================================
# 逻辑
# ============================================================

def find_phase(today):
    """找到今天属于哪个阶段"""
    for p in PHASES:
        start = datetime.date.fromisoformat(p["start"])
        end = datetime.date.fromisoformat(p["end"])
        if start <= today <= end:
            return p
    return None

def find_upcoming_milestones(today, n=3):
    """找到接下来 n 个未完成的里程碑"""
    upcoming = []
    for name, date_str, desc in MILESTONES:
        d = datetime.date.fromisoformat(date_str)
        if d >= today:
            upcoming.append((name, date_str, desc, (d - today).days))
    return sorted(upcoming, key=lambda x: x[3])[:n]

def is_weekend(today):
    return today.weekday() >= 5  # 周六=5, 周日=6

def main():
    today = datetime.date.today()
    phase = find_phase(today)

    print("=" * 60)
    print(f"  📅 {today}  {today.strftime('%A')}")
    print("=" * 60)

    if phase is None:
        print("\n⚠️  当前日期不在任何学习阶段的范围内。")
        print("   请检查 daily_reminder.py 中的 PHASES 时间配置。")
        return

    # 当前阶段
    print(f"\n📍 当前阶段：{phase['name']}")
    print(f"   {phase['start']} → {phase['end']}")

    # 今日安排
    print("\n📋 今日任务：")
    print("-" * 40)
    plan = phase["weekend_plan"] if is_weekend(today) else phase["weekday_plan"]
    for when, what in plan.items():
        print(f"  🔸 {when}：{what}")

    # 始终提醒 LeetCode + 八股
    if "LeetCode" not in str(plan):
        print(f"  🔸 日常：{WEEKLY_LEETCODE}")
    if "八股" not in str(plan):
        print(f"  🔸 日常：{WEEKLY_BAGU}")

    # 即将到来的里程碑
    print(f"\n⏰ 即将到来的里程碑：")
    print("-" * 40)
    milestones = find_upcoming_milestones(today)
    for name, date_str, desc, days_left in milestones:
        urgency = "🔴" if days_left <= 14 else ("🟡" if days_left <= 30 else "🟢")
        print(f"  {urgency} {name} | {date_str} | 还剩 {days_left} 天")
        print(f"      {desc}")

    # 最近一个里程碑倒计时
    if milestones:
        name, date_str, desc, days_left = milestones[0]
        print(f"\n⚡ 距离最近的里程碑 [{name}] 还有 {days_left} 天：{desc}")

    print("\n" + "=" * 60)
    print("  📌 驱动作完就投实习，别等完美。")
    print("  📌 数据在硅片与物理世界之间穿梭的规则 > 点灯。")
    print("=" * 60)


if __name__ == "__main__":
    main()

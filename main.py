import tkinter as tk
import random
import threading
import time

# 🌸 美好祝福语
messages = [
    "愿你被世界温柔以待 💕",
    "生活明朗，万物可爱 🌈",
    "心有暖阳，自在生光 ☀️",
    "愿你此生尽兴，赤诚善良 🌷",
    "你值得一切美好 🍀",
    "保持热爱，奔赴山海 🌊",
    "心中有光，步履不停 ✨",
    "愿你快乐，不止此刻 💫",
    "温柔与星光同在 🌟",
    "平安喜乐，岁月静好 🌸"
]

# 🌈 柔和配色
colors = [
    "#FFB6C1", "#FFC0CB", "#FFD700", "#98FB98",
    "#87CEFA", "#BA55D3", "#FFA07A", "#F0E68C",
    "#AFEEEE", "#DDA0DD"
]


def dow():
    window = tk.Tk()
    window.overrideredirect(True)  # 去掉标题栏（让窗口更干净）
    window.attributes("-topmost", True)  # 置顶
    window.attributes("-alpha", 0.0)  # 初始透明

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    # 随机位置和样式
    x = random.randint(0, width - 300)
    y = random.randint(0, height - 150)
    color = random.choice(colors)
    msg = random.choice(messages)

    # 设置窗口大小和位置
    window.geometry(f"300x100+{x}+{y}")
    window.config(bg=color)

    # 圆角模拟（用 Canvas 绘制）
    canvas = tk.Canvas(window, width=300, height=100, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_rectangle(10, 10, 290, 90, fill=color, outline=color, width=0)

    # 文本标签
    label = tk.Label(
        window,
        text=msg,
        bg=color,
        fg="white",
        font=("微软雅黑", 14, "bold"),
        wraplength=260,
        justify="center"
    )
    label.place(relx=0.5, rely=0.5, anchor="center")

    # 🌟 淡入动画
    for i in range(0, 11):
        window.attributes("-alpha", i / 10)
        time.sleep(0.03)
        window.update()

    # 显示一段时间后自动关闭
    time.sleep(random.uniform(3, 5))
    for i in range(10, -1, -1):
        window.attributes("-alpha", i / 10)
        time.sleep(0.03)
        window.update()
    window.destroy()


# ✨ 启动多线程弹窗
threads = []
for i in range(20):  # 弹出数量（可调）
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.3)
    threads[i].start()

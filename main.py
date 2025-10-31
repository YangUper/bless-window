import tkinter as tk
import random
import threading
import time

# 💬 美好祝愿语录（无节日限定）
messages = [
    "愿你每天都笑口常开 😊",
    "生活温柔，岁月静好 🌷",
    "愿所有美好如期而至 ✨",
    "被爱包围，也懂得爱 ❤️",
    "星光不问赶路人 🌠",
    "你比想象中更坚强 💪",
    "心中有光，人生就有方向 🌞",
    "保持热爱，奔赴山海 🌊",
    "希望如约而至 🌈",
    "平安喜乐，顺遂无忧 🍀",
    "遇见温柔，也成为温柔 🌸",
    "微风不燥，岁月不扰 🌿",
    "好运永远与你同在 🍀",
    "眼中有光，心中有爱 💖",
    "前路漫漫，皆有星光 ✨"
]

# 🎨 随机颜色列表
colors = [
    "red", "orange", "gold", "yellow", "green",
    "lightgreen", "cyan", "lightblue", "blue", "purple",
    "pink", "plum", "tomato", "khaki", "lavender"
]


def dow():
    # 创建窗口
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    # 随机位置
    a = random.randrange(0, width - 200)
    b = random.randrange(0, height - 100)

    # 随机背景色和祝福语
    bg_color = random.choice(colors)
    msg = random.choice(messages)

    # 设置窗口
    window.title("祝福弹窗")
    window.geometry(f"250x80+{a}+{b}")

    # 标签
    tk.Label(
        window,
        text=msg,
        bg=bg_color,
        fg="black",
        font=("楷体", 15, "bold"),
        width=20, height=2
    ).pack()

    window.mainloop()


# 创建多个线程弹窗
threads = []
for i in range(50):  # 可调整弹出数量
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.15)
    threads[i].start()

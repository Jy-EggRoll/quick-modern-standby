import subprocess
import time
import os
from tkinter import messagebox


psshutdown_path = "psshutdown64.exe"
if not os.path.exists(psshutdown_path):
    messagebox.showinfo("提示", "请把两个 exe 文件均解压出来并放在同一目录下，您现在很可能是直接在压缩包中双击或只解压了主文件。")
    exit(0)
else:
    time.sleep(2)  # 等待两秒再操作，防止因为鼠标移动导致进入现代待机又马上被唤醒
    subprocess.run(["psshutdown64.exe", "-x", "/accepteula"])  # 如果系统支持，将进入现代待机状态，默认接受协议，以免跳出窗口阻碍正常待机

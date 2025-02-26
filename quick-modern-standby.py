import subprocess
import time
import pyautogui


pyautogui.hotkey("alt", "shift", "e")  # 用户自定义的退出 MyKeymap 的快捷键
time.sleep(2)  # 等待两秒再操作，防止因为鼠标移动导致进入现代待机又马上被唤醒
subprocess.run(["psshutdown64.exe", "-x"])  # 如果系统支持，将进入现代待机状态

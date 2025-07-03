import subprocess
import time


time.sleep(2)  # 等待两秒再操作，防止因为鼠标移动导致进入现代待机又马上被唤醒
subprocess.run(["psshutdown64.exe", "-x", "/accepteula"])  # 如果系统支持，将进入现代待机状态，默认接受协议，以免跳出窗口阻碍正常待机

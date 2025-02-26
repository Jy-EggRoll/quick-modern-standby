# 快速调用现代待机

**功能**：通过模拟快捷键操作，实现退出MyKeymap（这是我个人的需求，如果软电脑上没有此软件，通常不会产生任何效果），并在等待两秒后尝试让系统进入现代待机状态。

**运行要求**：保证软件目录结构正确。

## 用法

下载最新的 Release 压缩包，把软件解压到任意目录下，对其中的 `quick-modern-standy.exe` 创建快捷方式到任意地方，双击即可在两秒后调用现代待机功能。

## 代码

代码实在是非常简单，我直接写在下面。

```python
import subprocess
import time
import pyautogui


pyautogui.hotkey("alt", "shift", "e")  # 用户自定义的退出 MyKeymap 的快捷键
time.sleep(2)  # 等待两秒再操作，防止因为鼠标移动导致进入现代待机又马上被唤醒
subprocess.run(["psshutdown64.exe", "-x"])  # 如果系统支持，将进入现代待机状态

```

Release 中的软件采用 PyInstaller 构建。

```python
pyinstaller -w --onefile quick-modern-standby.py
```

---

注：[PsShutdown](https://learn.microsoft.com/zh-cn/sysinternals/downloads/psshutdown) 是 Sysinternals 工具集的一部分，Sysinternals 由 Mark Russinovich 和 Bryce Cogswell 创建，后被微软收购，所以可视为微软产品。鉴于人人都可以下载该软件，方便起见，我集成了此软件，并未对其进行任何修改。

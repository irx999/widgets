
try:
    import mitmproxy,json
    import pandas as pd
    import  xlwings
except ImportError:
    import os
    os.system('pip3 install -r requirements.txt')
    



import subprocess
def run_terminal_program():
    # 使用subprocess.run启动终端程序
    process = subprocess.Popen(("mitmweb  -s addons.py"), shell=False)
    # 返回子进程对象，以便在函数外部操作
    return process
terminal_process = run_terminal_program()
while True:
    # 当控制台输入 y 的时候 将停止子进程
    user_input = input("Press 'y' to terminate the second program:\n  请按Y结束 该子进程 ")
    if user_input.lower() == 'y':
        terminal_process.terminate()
        break
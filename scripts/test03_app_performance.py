"""
    目标：通过python语言调用adb命令
    需求：获取黑马头条内存使用情况、CPU 使用情况、电量
    命令：adb shell dumpsys meminfo +包名(com.itcast.toutiaoApp)
"""
import os
from time import sleep

# 封装内存读取函数
def get_mem_data():
    data = os.popen("adb shell dumpsys meminfo com.itcast.toutiaoApp")
    for line in data:
        if "TOTAL" in line:
            return line.split()[1]

if __name__ == '__main__':
    for i in range(10):
        mem = get_mem_data()
        print("mem=", mem)
        sleep(1)


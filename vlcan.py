import time

def start_countdown(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print('发射！')

def start_rocket():
    print('飞船正在准备起飞......')
    start_countdown(3)
    print('飞船成功起飞！')
  start_rocket()

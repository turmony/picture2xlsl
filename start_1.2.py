import keyboard
import pyautogui as pyui
import pandas as pd
import get_response
import handle_response
import winsound
import time
import sys


def beep():
    duration = 400
    freq = 400
    winsound.Beep(freq, duration)


def get_token_fun():
    token_input = pyui.prompt(text='请输入百度文字识别(高精度版)access_token,'
                                   '默认有效期30天,access_token文件在当前目录,若没有请运行一次get_access_token.py生成 ,点击取消或关闭按钮将结束程序运行', title='token获取')
    b = None
    if token_input is b:
        sys.exit()
    else:
        print(token_input)
    return token_input


# 获取token,一般有效期30天
access_token = get_token_fun()
pyui.alert(text='token正确,程序正在运行,请根据dos窗口指令操作', title='提示')

screen = pyui.size()
position = []
numbers = []
names = []
total = 0
flag = True
num = 1
while flag:
    print('点击ctrl开始获取第一个点')
    keyboard.wait('ctrl')
    x1, y1 = pyui.position()
    print('点击alt开始获取第二个点')
    keyboard.wait('alt')
    x2, y2 = pyui.position()
    screen_shot = pyui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    beep()
    # file_name = f'{x1}-{y1}-{x2 - x1}-{y2 - y1}-{random.randint(0, 100)}.jpeg'
    tmp_str = time.strftime('%Y年%m月%d日%H时%M分%S秒', time.localtime()) + '' + f'{num}'
    print(tmp_str)
    file_name = f'{tmp_str}.jpeg'
    print(file_name)
    # file_name = f'{num}.jpeg'
    screen_shot.save(f'./{file_name}')
    response = get_response.get_response_fun(file_name, access_token)
    tmp_position, tmp_numbers, tmp_names, tmp_total = handle_response.handle_response_fun(response)
    position.extend(tmp_position)
    print(f'-----------------当前获取({tmp_total})条信息------------------')
    total = total + tmp_total
    print(f'-----------------总共获取({total})条信息------------------')
    numbers.extend(tmp_numbers)
    names.extend(tmp_names)
    # 新方法
    dialog_box = pyui.confirm(
        text=f'第{num}次获取,本次获取{int(tmp_total)}条记录,具体信息查看dos窗口,目前共获取{int(total)}条记录,确定要继续获取吗?',
        title='提示', buttons=['确定', '取消'])
    num = num + 1
    if dialog_box == '取消':
        flag = False
    # 旧方法
    # tmp = int(input('输入1继续,0结束:'))
    # print(f'输入的是:{tmp}')
    # if tmp == 0:
    #     flag = False
total = int(total)
pyui.alert(text=f'执行获取动作{num - 1}次,共获取{total}条记录,写入当前目录成功,文件名:data{total}.xlsx', title='提示',
           button='确定')
print(position)
print(numbers)
print(names)
df = pd.DataFrame({'床号': position, '住院号': numbers, '姓名': names})
print(df)
# 需要openpyxl
df.to_excel(f'./data{total}.xlsx', sheet_name='Sheet1')
print(f'写入当前目录成功,文件名:data{total}.xlsx')

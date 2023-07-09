
# encoding:utf-8
import requests
import json
import pyautogui as pyui

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=i1Atoc1hCfbSu6GAvj4lFoDe' \
       '&client_secret=pUTEWjKefXoOkKY1Wt2Y5qtzkGYQ1pRK'
response = requests.get(host)
if response:
    a = {}
    a = json.loads(response.content)
    expires = a['expires_in']
    access_token = a['access_token']
    with open('./access_token.txt', mode='w') as f:
        f.write(access_token)
    pyui.alert(text=f'access_token已写入当前文件,文件名:access_token.txt:，access_token:{access_token}', title='提示')
    print(response.json())
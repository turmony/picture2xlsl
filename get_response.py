import requests
import base64

'''
通用文字识别（高精度版）
'''


def get_response_fun(file_name, access_token):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(f'./{file_name}', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    # access_token = '24.3365bc6627262c12b16387fdb8d07b65.2592000.1691202298.282335-35773855'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    return response
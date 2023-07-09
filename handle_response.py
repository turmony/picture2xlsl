import json


def handle_response_fun(response):
    my_dict = {}
    detail = []
    if response:
        # print(response.text)
        json_str = "'" + response.text + "'"
        result = json.loads(response.content)
        my_dict = result
        # print(result)
        # print(type(result))
    data = my_dict['words_result']
    total = my_dict['words_result_num'] / 3
    # print(data)
    # print(total)
    for i in data:
        detail.append(i['words'])
    # print(detail)
    # tmp = []
    # distance = 3
    # for i in range(0,len(detail),distance):
    #     tmp.append(detail[i:i+distance])
    #     print(detail[i:i+distance])
    position = []
    numbers = []
    names = []
    position = detail[::3]
    numbers = detail[1::3]
    names = detail[2::3]
    print(position)
    print(numbers)
    print(names)
    return position, numbers, names, total

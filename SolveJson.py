import json
import sys


def GetString(filename):  # 将json文件读取并转化为program-actions的格式存入对应名称txt中
    data = []
    f = open("./data/" + filename + ".txt", "w")
    sys.stdout = f
    for lines in open("./data/" + filename + ".json", 'r'):
        data.append(json.loads(lines))  # 读json文件数据
    for examples in data:
        for example in eval(str(examples['examples'])):
            temp = str(example).replace('\'', '\"')
            example_dic = eval(temp)  # 按json字典方式读取
            #print(example_dic['example_index'], end="")
            print("Action:",end="")
            print(example_dic['actions'])
            print("Input:",end="")
            print(example_dic['inpgrid_json'])
            print("Output:", end="")
            print(example_dic['outgrid_json'])
        print("Code:", end="")
        print(str(examples['program_tokens']).replace('\'', '').replace(',', '')[1:-1])
        print()
import re

Data = []


class robot:  # 机器人位置，朝向信息
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = ""
karel = robot()

dir_list = ['<','^','>','v']
def PrintData():
    for i in Data:
        for j in i:
            print(re.sub("|'|,| |\[|\]", '', str(j)))
        print("__________")


def Simu(filename, codename):  # 根据代码在地图中运行，返回True False
    GetMap(filename)
    code =  open("./Program/" + codename + ".txt", "r").readlines()
    print(code)
    for i in range(5):
        for j in range(len(Data[0])):
            for m in range(len(Data[0][0])):
                if(Data[i][j][m] in dir_list):
                    karel.x = j
                    karel.y = m
                    karel.dir = Data[i][j][m]

    PrintData()


def GetMap(filename):  # 读取地图文件
    for i in range(5):
        tempname = filename + str(i)
        Map = []
        for line in open("./TempMap/" + tempname + ".txt", "r"):
            temp = []
            for i in line.strip():
                temp.append(i)
            Map.append(temp)
        Data.append(Map)

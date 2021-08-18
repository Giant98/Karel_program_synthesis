import  SolveJson
import  GetCode
import numpy as np
from stanfordkarel import *

#声明处理的文件
filename = "2"

'''
#Karel图形界面
def main():
    """ Karel code goes here! """
    path = GetCode.search_path(filename)
    exec("".join(path))
'''

if __name__ == '__main__':
    #SolveJson.GetString(filename)#Json文件处理
    #run_karel_program(filename_to_save="test2.w")#Karel图形界面
    GetCode.search_path(filename)
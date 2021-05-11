import  SolveJson
import  GetCode
from karel import KarelForSynthesisParser
#from stanfordkarel import *

#声明处理的文件
filename = "test"

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
    '''
    #用Karel库运行程序
    parser = KarelForSynthesisParser()
    parser.new_game(world_size=(8, 8))
    
    code = "DEF run m( move REPEAT R=3 r( putMarker r) move m)"
    parser.draw("Input:  ", with_color=True)
    #input = parser.get_state()
    parser.run(code,debug=False)
    #output = parser.get_state()
    #print((input == output).all())
    parser.draw("Output: ")
    '''
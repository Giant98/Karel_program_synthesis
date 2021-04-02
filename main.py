import  SolveJson
import Simulate
from stanfordkarel import *

def search_path(param):
    ans = []
    print("I'm a ", param)
    # 找到如下路径
    # if front_is_clear():
    #     turn_left()
    # while front_is_clear():
    #     move()
    # 构造出这条路径,用\n\t表示对应的缩进
    ans.append("if front_is_clear() :")
    ans.append("\n\tturn_left()")
    ans.append("\nwhile front_is_clear():")
    ans.append("\n\tmove()")
    return ans


def main():
    """ Karel code goes here! """
    move()
    while(not (beepers_present())):
        if(front_is_clear()):
            move()
        else:
            turn_left()
    pick_beeper()
    '''
    path=search_path("some param")
    exec("".join(path))
    print("find it !")
    
    '''
if __name__ == '__main__':

    filename = "2"
    'SolveJson.GetString(filename)'
    Simulate.Simu("Env1-","code1")
    run_karel_program()

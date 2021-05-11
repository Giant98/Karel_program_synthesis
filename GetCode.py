from karel import KarelForSynthesisParser
from karel.utils import TimeoutError
import numpy as np

def search_path(filename):
    trace = []
    ans = ""
    f = open("./data/" + filename + ".txt", "r")
    line = f.readline()
    while line:
        if line[:4]=="Code":
            code = line[5:]
            print("Code: ", end="")
            print(code, end="")
            ans = train_path(trace,code)
            trace = []
        else:
            trace.append(line[:-1])
        line = f.readline()
    f.close()

    return ans

def train_path(trace,code):#利用传过来的6条trace搜索path
    token = ["move ", "turnRight ", "turnLeft ", "pickMarker", "putMarker"]
    Cond = ["frontIsClear", "leftIsClear", "rightIsClear", "markersPresent", "noMarkersPresent"]
    output = []
    '''
    if(len(set(trace))==1):
        print(set(trace))
    '''
    #获得预期output
    parser = KarelForSynthesisParser()
    parser.new_game(world_size=(8, 8))
    parser.draw("Input:  ", with_color=True)
    try:
        parser.run(code, debug=False)
    except TimeoutError as e:
        print("引发异常：",repr(e))
    else:
        parser.draw("Output: ")
        output = parser.get_state()


    ans = ""

    return ans

def test_path(code):
    return True
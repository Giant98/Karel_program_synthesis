from karel import KarelForSynthesisParser
from karel.utils import TimeoutError
from karel.Search import Prog

def search_path(filename):
    trace = []
    ans = ""
    f = open("./data/" + filename + ".txt", "r")
    line = f.readline()
    while line:
        if line[:4] == "Code":
            code = line[5:]
            ans = train_path(trace, code)
            trace = []
        else:
            trace.append(line[:-1])
        line = f.readline()
    f.close()

    return ans


def train_path(trace, code):  # 利用传过来的6条trace搜索path
    '''
    if(len(set(trace))==1):
        print(set(trace))
    '''
    '''
    output = []
    #获得预期output
    code = "DEF run m( WHILE c( frontIsClear c) w( move w) m)"
    print("Code:  ",end="")
    print(code,end="")
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
    '''
    codes = Prog(2)
    for code in codes:
        print(code)


    ans = ""

    return ans


def test_path(code):
    return True

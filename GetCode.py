def search_path(filename):
    '''
    # 找到如下路径
    # move()
    # if front_is_clear():
    #     turn_left()
    # while front_is_clear():
    #     move()
    # 构造出这条路径,用\n\t表示对应的缩进
    ans = []
    ans.append("move()")
    ans.append("\nif front_is_clear() :")
    ans.append("\tturn_left()")
    ans.append("\nwhile front_is_clear():")
    ans.append("\n\tmove()")
    '''
    trace = []
    ans = ""
    f = open("./data/" + filename + ".txt", "r")
    line = f.readline()
    while line:
        if line[:4]=="Code":
            ans = train_path(trace)
            trace = []
        else:
            trace.append(line[:-1])
        line = f.readline()
    f.close()

    return ans

def train_path(trace):#利用传过来的6条trace搜索path
    token = ["move()", "turn_right()", "turn_left()", "pick_beeper()", "put_beeper()"]
    Cond = ["front_is_clear()", "left_is_clear()", "right_is_clear()", "beepers_present()", "no_beepers_present()"]
    if(len(set(trace))==1):
        print(set(trace))
    code = ""
    return code

def test_path(code):
    return True
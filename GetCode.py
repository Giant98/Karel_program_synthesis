def search_path():
    ans = []
    '''
    # 找到如下路径
    # move()
    # if front_is_clear():
    #     turn_left()
    # while front_is_clear():
    #     move()
    # 构造出这条路径,用\n\t表示对应的缩进
    ans.append("move()")
    ans.append("\nif front_is_clear() :")
    ans.append("\tturn_left()")
    ans.append("\nwhile front_is_clear():")
    ans.append("\n\tmove()")
    '''
    action = ["move()","turn_right()","turn_left()","pick_beeper()","put_beeper()"]
    Cond = ["front_is_clear()","left_is_clear()","right_is_clear()","beepers_present()","no_beepers_present()"]
    ans.append("")

    return ans
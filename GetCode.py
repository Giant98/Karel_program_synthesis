def search_path(ans):
    ans = []
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

    return ans
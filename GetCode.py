from karel import KarelForSynthesisParser
from karel.utils import TimeoutError
from karel.Search import Prog

class TreeNode():#二叉树节点(用来模拟if_else)
    def __init__(self,val,lchild=None,rchild=None):
        self.val=val		#二叉树的节点值
        self.lchild=lchild		#左孩子
        self.rchild=rchild		#右孩子

def search_path(filename):
    trace = []
    ans = ""
    f = open("./data/" + filename + ".txt", "r")
    line = f.readline()
    while line:#根据txt数据格式读取trace,code
        if line[:4] == "Code":
            code = line[5:]
            ans = train_path(trace, code)
            trace = []
        else:
            trace.append(line[:-1])
        line = f.readline()
    f.close()

    return ans


def train_path(traces, code):  # 利用传过来的6条trace搜索path
    ans = ""

    if(len(set(traces))==1):#全部相同情况
        ans = traces[0]
    else:
        temptraces = []
        for trace in traces:
            temptraces.append(str(trace).replace(' ','').replace('[','').replace(']','').replace('\'','').split(','))
        Root = TreeNode(temptraces[0])#构建二叉树表示if.else
        for trace in temptraces[1:]:
            if(not dfs(Root,trace)):
                Root = change(Root,trace)
        ans = getans(Root)
        print(ans)
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
    
    codes = Prog(2)
    for code in codes:
        print(code)
    '''

    print("ans: DEF run m( "+str(ans).replace('[','').replace(']','').replace('\'','').replace(',','')+" m)")
    return ans


def dfs(Root,trace):#查看当前trace在树中能否查找到
    if not Root:
        return False
    trace_length = len(trace)
    root_length = len(Root.val)
    if(trace_length<=root_length):
        for i in range(trace_length):
            if(trace[i]!=Root.val[i]):
                return False
        return True
    else:
        for i in range(root_length):
            if(trace[i]!=Root.val[i]):
                return False
        return dfs(Root.lchild,trace[root_length:]) or dfs(Root.rchild,trace[root_length:])


def getans(Root):
    ans = Root.val
    if(Root.lchild!=None):
        ans.append('IFELSE c( cond c) i(')
        ans.extend(getans(Root.lchild))
        ans.append('i) ')
    if(Root.rchild!=None):
        ans.append('ELSE e(')
        ans.extend(getans(Root.rchild))
        ans.append('e)')
    return ans


def change(Root,trace):#根据新trace修改二叉树
    trace_length = len(trace)
    root_length = len(Root.val)
    minlength = min(trace_length,root_length)
    for i in range(minlength):#处理前minlength位就存在不一致的情况
        if (trace[i] != Root.val[i]):
            NewRoot = TreeNode(trace[:i])
            NewRoot.lchild = Root
            NewRoot.rchild = TreeNode(trace[i:])
            Root.val = Root.val[i:]
            return NewRoot
    #处理trace_length>root+length且trace[0-root_length]与root[0-root_length]全部相同的情况
    #需要对多余部分到root的下一层节点中修改
    lchild_ans = findmaxmatch(Root.lchild, trace[root_length:])
    rchild_ans = findmaxmatch(Root.rchild, trace[root_length:])
    maxtrace = ""
    if (lchild_ans[0] >= rchild_ans[0]):
        maxtrace = "l" + lchild_ans[1]
    else:
        maxtrace = "r" + rchild_ans[1]
    TempRoot = Root
    ParentRoot = None
    num = 0
    for i in maxtrace:
        ParentRoot = TempRoot
        num = num + len(TempRoot.val)
        if(i=="l"):
            TempRoot = TempRoot.lchild
        else:
            TempRoot = TempRoot.rchild
    if(TempRoot==None):
        TempRoot = TreeNode("#")
    trace = trace[num:]
    trace_length = len(trace)
    root_length = len(TempRoot.val)
    minlength = min(trace_length, root_length)
    for i in range(minlength):
        if (trace[i] != TempRoot.val[i]):
            NewRoot = TreeNode(trace[:i])
            if(maxtrace[-1]=="l"):
                ParentRoot.lchild = NewRoot
            else:
                ParentRoot.rchild = NewRoot
            NewRoot.lchild = TempRoot
            NewRoot.rchild = TreeNode(trace[i:])
            TempRoot.val = TempRoot.val[i:]
            return Root


def findmaxmatch(Root,trace):#寻找匹配程度最高的结点,返回[当前最大匹配量,路径]
    if not Root:
        return [0,""]
    trace_length = len(trace)
    root_length = len(Root.val)
    if(trace_length<=root_length):
        for i in range(trace_length):
            if(trace[i]!=Root.val[i]):
                return [i,""]
        print("Find Error 01!")
    else:
        for i in range(root_length):
            if(trace[i]!=Root.val[i]):
                return [i,""]
        lchild_ans = findmaxmatch(Root.lchild,trace[root_length:])
        rchild_ans = findmaxmatch(Root.rchild,trace[root_length:])
        if(lchild_ans[0]>=rchild_ans[0]):
            return [(root_length+lchild_ans[0]),("l"+lchild_ans[1])]
        else:
            return [(root_length + rchild_ans[0]), ("r" + rchild_ans[1])]


def test_path(code):
    return True

from karel import KarelForSynthesisParser
from karel.utils import TimeoutError
from karel.Search import Prog
from Base import loadJson,Draw,Run

class TreeNode():#二叉树节点(用来模拟if_else)
    def __init__(self,val,lchild=None,rchild=None):
        self.val=val		#二叉树的节点值
        self.lchild=lchild		#左孩子
        self.rchild=rchild		#右孩子


def takelength(elem):
    return len(elem)


def search_path(filename):
    trace = []
    input = []
    output = []
    ans = ""
    f = open("./data/" + filename + ".txt", "r")
    line = f.readline()
    datalength = 0
    matchnum = 0
    while line:#根据txt数据格式读取trace,code
        if line[:4] == "Code":
            datalength = datalength+1
            code = line[5:-1]
            trace.sort(key=takelength)
            ans = train_path(input,output,trace, code)
            if(ans == code):
                matchnum = matchnum + 1
            else:
                print(code)
                print(ans, end="\n\n")
            trace = []
            input = []
            output = []
        elif line[:6] == "Action":
            trace.append(line[7:-1])
        elif line[:5] == "Input":
            input.append(loadJson(line[6:-1]))
        elif line[:6] == "Output":
            output.append(loadJson(line[7:-1]))
            '''
            print(trace[-1])
            print('Input:')
            Draw(input[-1])
            print('Output')
            Draw(Run(input[-1],trace[-1]))
            '''
        line = f.readline()
    f.close()
    print(matchnum/datalength)
    return ans


def train_path(input,output,traces, code):  # 利用传过来的6条trace搜索path
    ans = ""
    if(len(set(traces))==1):#全部相同情况
        ans = traces[0]
        tempans = "DEF run m( "+str(ans).replace('[','').replace(']','').replace('\'','').replace(',','')+" m)"
        if tempans != code:#加入了code判断
            ans = solverepeat(ans)
    else:
        temptraces = []
        for trace in traces:
            temptraces.append(str(trace).replace(' ','').replace('[','').replace(']','').replace('\'','').split(','))
        Root = TreeNode(temptraces[0])#构建二叉树表示if.else
        for trace in temptraces[1:]:
            if(not dfs(Root,trace)):
                Root = change(Root,trace)
        ans = getans(Root)
        tempans = "DEF run m( " + str(ans).replace('[', '').replace(']', '').replace('\'', '').replace(',', '') + " m)"

        if tempans != code:#加入了code判断
            Root = findrepeat(Root)
            ans = getans(Root)
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

    ans = "DEF run m( "+str(ans).replace('[','').replace(']','').replace('\'','').replace(',','')+" m)"
    ans = ans.replace("  "," ")
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
        ParentRoot.lchild = TreeNode(trace[num:])
        return Root
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


def findrepeat(Root):#对节点中的Repeat数据进行压缩
    if(Root==None):
        return;
    Root.val = solverepeat(Root.val)
    findrepeat(Root.lchild)
    findrepeat(Root.rchild)
    return Root


def solverepeat(datastring):
    datastring = str(datastring).replace('[','').replace(']','').replace('\'','').replace(',','')
    datastring = datastring.split(" ")
    maxcount = 1
    sub = []
    index = 0
    length = len(datastring)
    for i in range(length-1):
        for j in range(i+1,length):
            count = 1
            if datastring[i:j] == datastring[j:j+j-i]:
                #j-i为字串长度
                count = count + 1
                templist = datastring[i:j]
                for k in range(j+j-i,length,j-i):
                    if templist == datastring[k:k+j-i]:
                        count = count + 1
                    else:
                        break
                if count > maxcount:
                    maxcount = count
                    sub = templist
                    index = i
    if(maxcount<2):
        return datastring
    else:
        prelist = str(datastring[0:index])
        if (prelist != "[]"):
            prelist = prelist + " "
        lastlist = str(datastring[index+maxcount*len(sub):])
        if(lastlist!="[]"):
            lastlist = " "+lastlist
        repeatstring = "REPEAT R="+str(maxcount)+" r( "+str(sub)+" r)"
        return prelist+repeatstring+lastlist


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


def delsamestring(Root):
    print(1)


def getans(Root):
    ans = str(Root.val)
    if(Root.lchild!=None):
        if(ans == "[]"):
            block = ""
        else:
            block = " "
        if(Root.rchild==None):
            ans = ans + block + 'IF c( cond c) i( ' + str(Root.lchild.val) + ' i) '
        else:
            ans = ans + block + 'IFELSE c( cond c) i( ' + str(getans(Root.lchild))+' i) '
    if(Root.rchild!=None):
        ans = ans + 'ELSE e( ' + str(getans(Root.rchild))+' e)'
    ans = ans.replace("  "," ")
    return ans


def trycond(ans,code):
    ans = ans.replace("  ", " ")
    conditiondict = ['frontIsClear', 'leftIsClear', 'rightIsClear', 'markersPresent', 'noMarkersPresent']
    for cond in conditiondict:
        if code == ans.replace("cond", cond):
            ans = code
            break
    if(ans!=code):
        for cond in conditiondict:
            if code == ans.replace("cond", "not c( "+cond+" c)"):
                ans = code
                break
    return ans


def test_path(code):
    return True

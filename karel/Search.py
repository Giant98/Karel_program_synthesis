Conds = ['frontIsClear','leftIsClear','rightIsClear','markersPresent','noMarkersPresent',
        'not c( frontIsClear c)','not c( leftIsClear c)','not c( rightIsClear c)','not c( markersPresent c)','not c( noMarkersPresent c)']
def Prog(stmt_max_depth = 4):
    if(stmt_max_depth<1):
        print("Error!层数过低")
    Stmt_ans = Stmt(stmt_max_depth-1)
    ans = []
    for stmt in Stmt_ans:
        ans.append("DEF run m( "+stmt+" m)")
    return ans

def Stmt(stmt_max_depth = 3):
    if(stmt_max_depth == 0):#Action
        return ["move","turnRight","turnLeft","pickMarker","putMarker"]
    else:
        return While(stmt_max_depth-1)+If(stmt_max_depth-1)+IFELSE(stmt_max_depth-1)+Repeat(stmt_max_depth-1)+Stmt_Stmt(stmt_max_depth-1)

def While(stmt_max_depth = 2):
    ans = []
    Stmt_ans = Stmt(stmt_max_depth)
    for cond in Conds:
        for stmt in Stmt_ans:
            ans.append("WHILE c( "+cond+" c) w( "+stmt+" w)")
    return ans

def If(stmt_max_depth = 2):
    ans = []
    Stmt_ans = Stmt(stmt_max_depth)
    for cond in Conds:
        for stmt in Stmt_ans:
            ans.append("IF c( "+cond+" c) i( "+stmt+" i)")
    return ans

def IFELSE(stmt_max_depth = 2):
    ans = []
    Stmt_ans = Stmt(stmt_max_depth)
    Stmt_ans2 = Stmt(stmt_max_depth)
    for cond in Conds:
        for s1 in Stmt_ans:
            for s2 in Stmt_ans2:
                if(s1!=s2):
                    ans.append("IFELSE c( "+cond+" c) i( "+s1+" i) ELSE e( "+s2+" e)")
    return ans

def Repeat(stmt_max_depth = 2):
    ans = []
    Stmt_ans = Stmt(stmt_max_depth)
    for i in range(0,20):
        for stmt in Stmt_ans:
            ans.append("REPEAT R="+str(i)+" r( "+stmt+" r)")
    return ans

def Stmt_Stmt(stmt_max_depth = 2):
    ans = []
    Stmt_ans = Stmt(stmt_max_depth)
    for s1 in Stmt_ans:
        for s2 in Stmt_ans:
            ans.append(s1+" "+s2)
    return ans
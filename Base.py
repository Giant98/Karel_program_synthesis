import json
import copy

def loadJson(texts):
    texts = str(texts).replace('\'', '\"').replace('False', 'false').replace('True', 'true')
    datas = json.loads(texts)
    if datas['crashed'] == True:
        print("crashed is False!")

    if datas['blocked']!='':
        datas['blocked'] = datas['blocked'].split(" ")
    else:
        datas['blocked'] = []

    if datas['markers']!='':
        datas['markers'] = datas['markers'].split(" ")
    else:
        datas['markers'] = []
    return datas

def Draw(datas):
    height = datas['rows']
    width = datas['cols']
    print(datas)
    world = []
    for i in range(height):
        world.append(["." for _ in range(width)])
    if datas['blocked']!=[]:
        for block in datas['blocked']:
            temp = block.split(":")
            world[int(temp[0])][int(temp[1])] = "#"
    if datas['markers']!=[]:
        for marker in datas['markers']:
            temp = marker.split(":")
            world[int(temp[0])][int(temp[1])] = temp[2]
    if datas['hero']!='':
        temp = datas['hero'].split(":")
        if(temp[2]=='north'):
            dir = 'v'
        elif(temp[2]=='south'):
            dir = '^'
        elif (temp[2] == 'west'):
            dir = '<'
        else:
            dir = '>'
        world[int(temp[0])][int(temp[1])] = dir
    print('____________')
    for i in world:
        print(str(i).replace('[','').replace(']','').replace('\'','').replace(',',''))
    print('------------')
    return world

def Run(innerdatas,datastring):
    datastring = str(datastring).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
    datastring = datastring.split(" ")
    datas = copy.deepcopy(innerdatas)
    #print(datas)
    dir = ['south','west','north','east']
    markerchange = False

    for action in datastring:
        #print(checkCond(datas))
        if(action == 'move'):
            if datas['hero'] != '':
                temp = datas['hero'].split(":")
                x = int(temp[0])
                y = int(temp[1])
                if (temp[2] == 'north'):
                    x = x + 1
                elif (temp[2] == 'south'):
                    x = x -1
                elif (temp[2] == 'west'):
                    y = y -1
                else:
                    y = y + 1
                if(x<0 or x>= datas['rows'] or y<0 or y>=datas['cols']):
                    continue
                temp2 = str(x)+":"+str(y)
                if datas['blocked'] != '':
                    if temp2 in datas['blocked']:
                        continue
                    else:
                        datas['hero'] = temp2 + ":" +temp[2]
        elif (action == 'turnRight'):
            if datas['hero'] != '':
                temp = datas['hero'].split(":")
                newdir = dir[(dir.index(temp[2])+1)%len(dir)]
                datas['hero'] = temp[0]+":"+temp[1]+":"+newdir
        elif (action == 'turnLeft'):
            if datas['hero'] != '':
                temp = datas['hero'].split(":")
                newdir = dir[(dir.index(temp[2])-1)]
                datas['hero'] = temp[0] + ":" + temp[1] + ":" + newdir
        elif (action == 'putMarker'):
            temp = datas['hero'].split(":")
            pos = temp[0] + ":" + temp[1]
            flag = False
            for i in range(len(datas['markers'])):
                temp = datas['markers'][i].split(":")
                markerpos = temp[0] + ":" + temp[1]
                if pos == markerpos:
                    flag = True
                    newnum = int(temp[2])+1
                    datas['markers'][i] = pos + ":" +str(newnum)
                    break
            if(not flag):
                markerchange = True
                datas['markers'].append(pos+":1")
        elif (action == 'pickMarker'):
            temp = datas['hero'].split(":")
            pos = temp[0] + ":" + temp[1]
            for i in range(len(datas['markers'])):
                temp = datas['markers'][i].split(":")
                markerpos = temp[0] + ":" + temp[1]
                if pos == markerpos:
                    newnum = int(temp[2])-1
                    if(newnum):
                        datas['markers'][i] = pos + ":" +str(newnum)
                        break
                    else:
                        datas['markers'].remove(datas['markers'][i])
                        break
    if markerchange:
        datas['markers'] = sorted(datas['markers'],key=lambda s:(-int(s.split(":")[0]),int(s.split(":")[1])))
    return datas

def checkCond(datas):
    conditiondict = {'frontIsClear':True,'leftIsClear':True,'rightIsClear':True,'markersPresent':False}

    temp = datas['hero'].split(":")
    heropos = temp[0] + ":" + temp[1]
    x = int(temp[0])
    y = int(temp[1])
    if (temp[2] == 'north'):
        if(x+1==datas['rows']):
            conditiondict['frontIsClear'] = False
        if (y == 0):
            conditiondict['leftIsClear'] = False
        if (y+1 == datas['cols']):
            conditiondict['rightIsClear'] = False
        frontpos = str(x+1)+":"+str(y)
        leftpos = str(x)+":"+str(y-1)
        rightpos = str(x)+":"+str(y+1)
    elif (temp[2] == 'south'):
        if (x == 0):
            conditiondict['frontIsClear'] = False
        if (y == 0):
            conditiondict['rightIsClear'] = False
        if (y + 1 == datas['cols']):
            conditiondict['leftIsClear'] = False
        frontpos = str(x-1)+":"+str(y)
        leftpos = str(x) + ":" + str(y + 1)
        rightpos = str(x) + ":" + str(y - 1)
    elif (temp[2] == 'west'):
        if (y == 0):
            conditiondict['frontIsClear'] = False
        if (x == 0):
            conditiondict['leftIsClear'] = False
        if (x + 1 == datas['rows']):
            conditiondict['rightIsClear'] = False
        frontpos = str(x)+":"+str(y-1)
        leftpos = str(x - 1) + ":" + str(y)
        rightpos = str(x + 1) + ":" + str(y)
    else:
        if (y+1 == datas['cols']):
            conditiondict['frontIsClear'] = False
        if (x == 0):
            conditiondict['rightIsClear'] = False
        if (x + 1 == datas['rows']):
            conditiondict['leftIsClear'] = False
        frontpos = str(x)+":"+str(y+1)
        leftpos = str(x + 1) + ":" + str(y)
        rightpos = str(x - 1) + ":" + str(y)

    for block in datas['blocked']:
        if(block == frontpos):
            conditiondict['frontIsClear'] = False
        elif(block == leftpos):
            conditiondict['leftIsClear'] = False
        elif(block == rightpos):
            conditiondict['rightIsClear'] = False

    for marker in datas['markers']:
        temp = marker.split(":")
        markerpos = temp[0] + ":" + temp[1]
        if heropos == markerpos:
            conditiondict['markersPresent'] = True

    return conditiondict
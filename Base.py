import json

def Draw(texts):
    texts = str(texts).replace('\'', '\"').replace('False','false').replace('True','true')
    datas= json.loads(texts)
    print(datas)

    if datas['crashed'] == True:
        print("crashed is False")
        return

    height = datas['rows']
    width = datas['cols']

    world = []
    for i in range(height):
        world.append(["." for _ in range(width)])
    if datas['blocked']!='':
        for block in datas['blocked'].split(" "):
            temp = block.split(":")
            world[int(temp[0])][int(temp[1])] = "#"
    if datas['markers']!='':
        for marker in datas['markers'].split(" "):
            temp = marker.split(":")
            world[int(temp[0])][int(temp[1])] = temp[2]
    if datas['hero']!='':
        temp = datas['hero'].split(":")
        if(temp[2]=='north'):
            dir = '^'
        elif(temp[2]=='south'):
            dir = 'v'
        elif (temp[2] == 'west'):
            dir = '<'
        else:
            dir = '>'
        world[int(temp[0])][int(temp[1])] = dir
    print('____________')
    for i in world:
        print(str(i).replace('[','').replace(']','').replace('\'','').replace(',',''))
    print('------------')
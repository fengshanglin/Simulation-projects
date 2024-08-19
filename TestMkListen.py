import os
import uuid
import json
import time
import sys

cDir = os.getcwd()

listDirs = os.listdir(cDir)
# print(listDirs)
print(os.path.dirname(cDir))

parentPath = os.path.dirname(cDir)
listOnlyFiles = []
listOnlyDirs = []
jsonDir = "pathFiles"
jsonFileName = "pathComment.json"


def getUIDD():
    return str(uuid.uuid4())


def getDirs():
    for path in listDirs:
        if os.path.isfile(os.path.join(cDir, path)):
            listOnlyFiles.append(path)
            print("---output dirs:",path)
        else:
            listOnlyDirs.append(path)
            print("***output files:",path)

def getDirsByParams(childPath,flag=0):
    # 0 list of directory
    # 1 list of file
    childListDirs = os.listdir(childPath)
    cListOnlyFiles = []
    cListOnlyDirs = []
    for path in childListDirs:
        if os.path.isfile(os.path.join(childPath, path)):
            cListOnlyFiles.append(path)
            print("---output dirs:",path)
        else:
            cListOnlyDirs.append(path)
            print("***output files:",path)
    if flag == 0:
        return cListOnlyDirs
    elif flag == 1:
        return cListOnlyFiles

def createDir():
    if not os.path.exists(jsonDir):
        os.mkdir(jsonDir)
        print("Directory {} created successfully".format(jsonDir))
    else:
        print("Directory {} already exists".format(jsonDir))
def createJsonFile(checkJsons):
    saveJons = {}
    cListFiles = []
    if len(checkJsons) == 0:
        cListFiles = listOnlyFiles
    elif len(checkJsons) != 0 and checkJsons[0]==-1:
        return -1
    else:
        pathJson = cDir + "\\" + \
           jsonDir + "\\" + \
           jsonFileName
        fJson = open(pathJson,'r')
        saveJons = json.load(fJson)
        fJson.close()
        cListFiles = cListFiles + checkJsons
        for keyName,itemJson in saveJons.items():
            for itemFile in cListFiles:
                if itemJson == itemFile:
                    del saveJons[keyName]
                    cListFiles.remove(itemFile)
                    break

    # temp = "path:" + "\n" + "createTime:"+"\n" + "comment:"+"\n"
    temp = "comment:"+"\n"
    dateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for itemFileName in cListFiles:
        uuidObj = getUIDD()
        uuidObjStr = cDir+ "\\" + jsonDir + "\\" + uuidObj  + '.txt'
        saveJons[uuidObj] = itemFileName
        temp = "fileName:"+itemFileName+"\n"+ \
            "path:" + uuidObjStr+ "\n" + \
            "createTime:"+dateTime+"\n"+ temp
        commentFile = open(uuidObjStr,'w')
        commentFile.write(temp)
        commentFile.close()
        temp = "comment:" + "\n"
        pahtJson = str(os.path.join(cDir,jsonDir,jsonFileName))
        with open(pahtJson, 'w') as f:
            json.dump(saveJons, f)
        print(saveJons)
def checkFiles():
    checkJsons = []
    pathJson = cDir + "\\" + \
           jsonDir + "\\" + \
           jsonFileName
    try:
        fJson = open(pathJson,'r')
        jsonDatas = json.load(fJson)
        print("---output jsonDatas:",jsonDatas)
        fJson.close()
        flagExist = True
        for itemFile in listOnlyFiles:
            flagExist = False
            # for itemJson in jsonDatas.values():
            for keyName,itemJson in jsonDatas.items():
                # print(itemJson)
                if itemFile == itemJson:
                    print("A File has been exist already")
                    del jsonDatas[keyName]
                    flagExist = True
                    break
            if flagExist == False:
                checkJsons.append(itemFile)
        #delete file
        if len(jsonDatas) == 0:
            print("A file is deleted")
        else:
            for itemFile in jsonDatas.values():
               checkJsons.append(itemFile)
                # os.remove(os.path.join(cDir,jsonDir,keyName))
        print("***checkJsons***:",checkJsons)
        if len(checkJsons) == 0:
            checkJsons.append(-1)
        return checkJsons
    except FileNotFoundError:
        print("File not found, please is that file path")
        createDir()
        createJsonFile(checkJsons)
        sys.exit(-1)

if __name__ == "__main__":
    getDirs()
    res = checkFiles()
    createJsonFile(res)

'''
if not os.path.exists(jsonDir):
    os.mkdir(jsonDir)
    print("Directory {} created successfully".format(jsonDir))
else:
    print("Directory {} already exists".format(jsonDir))

saveJons = {}
# temp = "path:" + "\n" + "createTime:"+"\n" + "comment:"+"\n"
temp =   "comment:"+"\n"
dateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
for itemFileName in listOnlyFiles:
    uuidObj = getUIDD()
    uuidObjStr = cDir+ "\\" + jsonDir + "\\" + uuidObj  + '.txt'
    saveJons[uuidObj] = itemFileName
    temp = "fileName:"+itemFileName+"\n"+ \
         "path:" + uuidObjStr+ "\n" + \
         "createTime:"+dateTime+"\n"+ temp
    commentFile = open(uuidObjStr,'w')
    commentFile.write(temp)
    commentFile.close()
    temp = "comment:" + "\n"
pahtJson = str(os.path.join(cDir,jsonDir,jsonFileName))
with open(pahtJson, 'w') as f:
    json.dump(saveJons, f)
print(saveJons)
'''

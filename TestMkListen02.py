import os
import uuid
import json
import time
import sys
import tkinter as tk

cDir = os.getcwd()

listDirs = os.listdir(cDir)
# print(listDirs)
print(os.path.dirname(cDir))

root = tk.Tk()
winHeight = 700
winWidth = 600

parentPath = os.path.dirname(cDir)
listOnlyFiles = []
listOnlyDirs = []
jsonDir = "pathFiles"
jsonFileName = "pathComment.json"





def getUIDD():
    return str(uuid.uuid4())
# self-define exceptions
class FileReadExceptions(Exception):
    def __init__(self, msg):
        self.msg=msg



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
        # dictionary changed size during iteration
        # Deleting key-value can lead to a error above
        recordDelDicts = []
        for keyName,itemJson in saveJons.items():
            for itemFile in cListFiles:
                if itemJson == itemFile:
                    recordDelDicts.append(keyName)
                    # del saveJons[keyName]
                    cListFiles.remove(itemFile)
                    break
        # Delete key-value in the Dicts
        for record in recordDelDicts:
            del saveJons[record]
    # create and add
    # temp = "path:" + "\n" + "createTime:"+"\n" + "comment:"+"\n"
    temp = "comment:"+"\n"
    dateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Only file were deleted
    if len(cListFiles) == 0:
        pahtJson = str(os.path.join(cDir,jsonDir,jsonFileName))
        with open(pahtJson, 'w') as f:
            json.dump(saveJons, f)
        print(saveJons)

    # create the json and comment files
    # add some comment files
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
        recordDelDicts = []
        for itemFile in listOnlyFiles:
            flagExist = False
            # for itemJson in jsonDatas.values():
            for keyName,itemJson in jsonDatas.items():
                # print(itemJson)
                if itemFile == itemJson:
                    print("A File has been exist already")
                    recordDelDicts.append(keyName)
                    # del jsonDatas[keyName]
                    flagExist = True
                    break
            if flagExist == False:
                checkJsons.append(itemFile)
        for record in recordDelDicts:
            del jsonDatas[record]
        #delete file
        if len(jsonDatas) == 0 and len(checkJsons) == 0:
            raise FileReadExceptions("Files not any changes")
        else:
            for keyName,itemFile in jsonDatas.items():
                checkJsons.append(itemFile)
                keyName = str(keyName+".txt")
                if os.path.exists(os.path.join(cDir,jsonDir,keyName)):
                    os.remove(os.path.join(cDir,jsonDir,keyName))
                else:
                    raise FileReadExceptions("A File fail to delete")
        print("***checkJsons***:",checkJsons)
        if len(checkJsons) == 0:
            checkJsons.append(-1)
        return checkJsons
    except FileNotFoundError:
        print("File not found, please is that file path")
        createDir()
        createJsonFile(checkJsons)
        sys.exit(-1)
    except FileReadExceptions as e:
        print("---error:",e.msg)
        sys.exit(-1)

def center_window(croot,width,height):
    screen_width = croot.winfo_screenwidth()
    screen_height = croot.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    croot.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

def createGUI():
    saveJons={}
    pahtJson = str(os.path.join(cDir,jsonDir,jsonFileName))
    with open(pahtJson,'r') as f:
        saveJons = json.load(f)
        print("Test GUI",saveJons)
    cTitles = ["Number","FileName","Time"]
    titleFrame = tk.Frame(root)
    # listBoxTitles = tk.Listbox(titleFrame)
    iLocation = 0
    for numTitle in cTitles:
        listBoxTitles = tk.Label(titleFrame,text=numTitle,width=10, anchor='center',bg='green')
        # listBoxTitles.insert(0,numTitle)
        listBoxTitles.grid(row=0,column=iLocation,padx=50)
        iLocation = iLocation + 1
    titleFrame.grid(row=0,column=0)

    listLabels = tk.Listbox(titleFrame)
    # listLabels.pack(fill='both',expand=True,side="left")
    listLabels.grid(row=1,column=0)
    for jsonValues in saveJons.values():
        listLabels.insert(0,jsonValues)

    for num in range(len(saveJons)):
        listBut = tk.Button(titleFrame,text="Submit",bg='red',pady=1)
        listBut.grid(row=num+1,column=3)

    root.title("Test comment")
    center_window(root,winHeight,winWidth)
    mainFrame = tk.Frame(root,height=winHeight,width=winWidth)
    mainFrame.grid(row=1,column=0)

    mainFrame01 = tk.Frame(root,height=winHeight,width=winWidth)
    mainFrame01.grid(row=1,column=1)

    # listLabels = tk.Listbox(mainFrame)
    # listLabels.pack(fill='both',expand=True,side="left")
    # for jsonValues in saveJons.values():
    #     listLabels.insert(0,jsonValues)

    # for num in range(len(saveJons)):
    #     listBut = tk.Button(mainFrame01,text="Submit")
    #     listBut.pack()
    root.mainloop()


if __name__ == "__main__":

    # getDirs()
    # res = checkFiles()
    # createJsonFile(res)
    createGUI()

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

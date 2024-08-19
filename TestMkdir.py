import os

workDirLists = ["GeometryModels","FEA_Results","ProFiles","Tests","Iteration"]
countDisNum = 0
print("--->Current directory path:{}".format(os.getcwd()))
for workDir in workDirLists:
    if not os.path.exists(workDir):
        os.mkdir(workDir)
        countDisNum = countDisNum+1
        print("--->Directory {} created successfully".format(workDir))
    else:
        print("--->Directory {} arealdy exists".format(workDir))
if countDisNum==0:
    print("--->********Director is not created********")
else:
    print("The total of {} directors are created".format(countDisNum))


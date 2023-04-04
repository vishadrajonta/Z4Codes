# this Python program read the Z4ParametersBest.txt
# and see whether it is smaller than the free cyclic codes we found
from pathlib import Path
import subprocess

subprocess.Popen(["rm", "-r", "leeComparedOutput"]).communicate()
subprocess.Popen(["mkdir", "leeComparedOutput"]).communicate()

file = open('LinearZ4ParametersBest.txt')
paraList = []
for i in file:
    paraList.append(i[:-1].split(","))
file.close()

lenStart = 1
lenLimit = 125
for i in range(lenStart,lenLimit+2,2):
    cyclicListFinal = []
    file_path = Path("/home/lu1/AllFreeCyclicZ_4/leeOutput/CyclicCodesLen" + str(i) + ".txt")
    outputFile = open(file_path,"r")
    cyclicParaList = outputFile.read().split("&&&")
    cyclicParaList = cyclicParaList[1:-1] # get rid of first and last entry (they are empty)
    for j in cyclicParaList[:-1]: # get rid of zero dimension(k1)
        j = j.replace("\n","")
        cyclicPara = j.split("&")
        cyclicPara.insert(1,i) # insert length
        cyclicPara.insert(3,0) # insert k2 which is always 0 for free codes
        cyclicPara[2] = int(cyclicPara[2]) # change K1 to integer
        cyclicPara[4] = int(cyclicPara[4]) # change the minimum Lee weight to integer
        cyclicPara[-1] = float(cyclicPara[-1]) # change the time to float
        index = ((i-1)**2)/4 + int(cyclicPara[2]) - 1
        if int(paraList[int(index)][3]) <= int(cyclicPara[4]):
            if int(paraList[int(index)][3]) < int(cyclicPara[4]):
                cyclicPara.append("New Linear Z4 Code")
            else: # when their minimum Lee weights are equal
                cyclicPara.append("Good Linear Z4 Code")
        else:
            cyclicPara.append("Normal Code")
        cyclicListFinal.append(cyclicPara)
    file_path = Path("/home/lu1/AllFreeCyclicZ_4/leeComparedOutput/comparedResultsLen" + str(i) + ".txt")
    f = open(file_path,"w")
    for i in cyclicListFinal:
        for j in i:
            f.write(str(j)+",")
        f.write("\n")
    f.close()
    outputFile.close()

# This Python program reads the file of all generator polynomials and then create a search file for each of them
import shutil
import subprocess
import sys

lenStart=1
lenLimit=125

# clear the input and output directories
subprocess.Popen(["rm", "-r", "leeInput"]).communicate() # communicate() makes sure that the next process will run after this process is completed
subprocess.Popen(["rm", "-r", "leeOutput"]).communicate()
subprocess.Popen(["mkdir", "leeInput"]).communicate()
subprocess.Popen(["mkdir", "leeOutput"]).communicate()

for length in range(lenStart,lenLimit+2,2):
	original = "lenTemplate.txt"
	target = "len" + str(length) + "Generator.txt"
	shutil.copyfile(original,"/home/lu1/AllFreeCyclicZ_4/leeInput/"+target) # this command copies the template and create a copy of it having a different name
	targetFile_path = "/home/lu1/AllFreeCyclicZ_4/leeInput/" + target
	with open(targetFile_path, "r") as f:
		contents = f.readlines()
		contents.insert(68, "n:=" + str(length) + ";") # this command insert a line right after line 22 of the template
	with open(targetFile_path, "w") as f:
		contents = "".join(contents)
		f.write(contents)

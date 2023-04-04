# This program kills all the PIDs stored in the file called PID.txt and then clear it at the end
import os

PIDFile=open("PIDs.txt","r")
for i in PIDFile:
    os.popen("kill "+str(i)) # run shell command in Python
os.popen("> PIDs.txt") # clear all the content of PIDs.txt
PIDFile.close()

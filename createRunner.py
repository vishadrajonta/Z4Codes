import subprocess
lenStart=1
lenLimit=125

subprocess.Popen(["rm", "-r", "leeTime"]).communicate()
subprocess.Popen(["mkdir", "leeTime"]).communicate()

file=open("runner.txt","w")

for length in range(lenStart,lenLimit+2,2):
	file.write("> " + "/home/lu1/AllFreeCyclicZ_4/leeTime/leeTimeOutputLen" + str(length) + ".txt\n")
	file.write("nohup magma " + "/home/lu1/AllFreeCyclicZ_4/leeInput/len" + str(length) + "Generator.txt >> " + "/home/lu1/AllFreeCyclicZ_4/leeTime/leeTimeOutputLen" + str(length) + ".txt &\n")
	file.write("echo $! >> PIDs.txt\n")
file.close()
subprocess.Popen(["bash", "runner.txt"], stdout=subprocess.PIPE, universal_newlines=True)

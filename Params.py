import os
import shutil

###############################################################################
#PARAMS
#Initial proportions
W0= 0.5
M0= 0.5

#Fitness
F = 0.99

#Mutation Rate
Mu = 0.001

#Migration influx of mutants
G = 0.002

#Noise Magnitude
N =0.05# 0.01

#Number of time steps
T = 1000

#RandomSeed for reproducibility
RandomSeed = 1
###############################################################################

SaveDirName = ("SaveFiles/" + 
        "T_%d"%(T) +
        "_W0_%0.1f_M0_%0.1f"%(W0,M0) + 
        "_F_%0.2f"%(F) + 
        "_Mu_" + f"{Mu:.{1}e}" +
        "_G_" + f"{G:.{1}e}" +
        "_N_" + f"{N:.{1}e}" +
        "_seed_%d"%(RandomSeed))


if not os.path.isdir("SaveFiles"):
    os.mkdir("SaveFiles")

if not os.path.isdir(SaveDirName):
    os.mkdir(SaveDirName)
    print("Created Savefile:",SaveDirName)

shutil.copyfile("Params.py", SaveDirName+"/Params.py")
shutil.copyfile("Script.py", SaveDirName+"/Script.py")


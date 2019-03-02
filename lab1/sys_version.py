
#!/usr/bin/env python

import os
import time
import glob

homedir = os.environ['HOME']
os.chdir(homedir)	#Enter home directory
print(os.getcwd())	#Test 

#Create folder steps
path=homedir+"/os_lab_0"

try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" %path)
else:
    print("Successfully created the directory %s " % path)
os.chdir(path)
print(os.getcwd())


#Create text and python files
f = open("first.txt", "w")
f=open("second.txt", "w")
f=open("myfile.py", "w")


#Printing text files last modified time

print("last modified: %s" % time.ctime(os.path.getmtime("first.txt")))
print("last modified: %s" % time.ctime(os.path.getmtime("second.txt")))
print("last modified: %s" % time.ctime(os.path.getmtime("myfile.py")))


#Finding txt files


for file in glob.glob("*.txt"):
    print(file)

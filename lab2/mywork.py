#!/usr/bin/python

import os
import errno, shutil, subprocess

def copyanything(src, dst):
	try:
		shutil.copytree(src, dst)
	except OSError as exc: 
		if exc.errno == errno.ENOTDIR:
			shutil.copy(src, dst)
	else: raise


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def startWith(start, path):
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.startswith(start):
				return os.path.join(root, file)

from os.path import expanduser
home = expanduser("~")
# the actual code
try:
	os.makedirs(home+"/newroot")
	rootPath=home+"/newroot"

	os.makedirs(rootPath+"/lib")
	os.makedirs(rootPath+"/bin")
	os.makedirs(rootPath+"/lib64")
	os.chdir(rootPath)
	print(os.getcwd())

	try:
		copyanything("/bin/bash", rootPath+"/bin")
		copyanything("/bin/ls", rootPath+"/bin")
		libPath=find("libtinfo.so.5","/")
		copyanything(libPath, rootPath+"/lib")
		libPath=find("libdl.so.2","/")
		copyanything(libPath, rootPath+"/lib")
		libPath=find("libc.so.6","/")
		copyanything(libPath, rootPath+"/lib")
		libPath=startWith("ld-linux","/lib")
		copyanything(libPath, rootPath+"/lib64")
		libPath=find("libselinux.so.1","/lib")
		copyanything(libPath, rootPath+"/lib")
		libPath=find("libpcre.so.3","/lib")
		copyanything(libPath, rootPath+"/lib")
		libPath=find("libpthread.so.0","/lib")
		copyanything(libPath, rootPath+"/lib")
		try:
			os.chroot(rootPath)
			os.chdir("/")
			print ("Changed root path successfully!!")
			print(os.getcwd())
			f=open("script.sh","w+")
			f.write("#! /bin/bash\r\necho 'Smile'\r\n")
			f.close()
			print(os.listdir())
			try:
				print(os.system("/bin/bash script.sh"))
			except OSError:
				print ("Failed execute")
		except OSError:
			print ("Failed chroot")
		
	except OSError:
		print("Copying failed")
	else:
		print("Succesful")


except OSError as exc: 
    if exc.errno == errno.EEXIST and os.path.isdir(directory_name):
        pass



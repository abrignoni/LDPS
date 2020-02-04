import os
from pathlib import Path
import tarfile
from zipfile import ZipFile
import fnmatch
import shutil
from ldpsfuncs import *

def search(pathto, filename, reportfolderbase):
	temp = reportfolderbase+'Extraction/'
	list = []
	for file in Path(pathto).rglob(filename):
		list.append(file)
		tempf, end = os.path.split(file)
		ends = '/'+end
		if os.path.isdir(temp+tempf):
			if os.path.isfile(file):
				shutil.copy2(file, temp+tempf)
			else:
				copytree(file, temp+tempf+ends)
		else:
			if os.path.isfile(file):
				os.makedirs(temp+tempf)
				shutil.copy2(file, temp+tempf)
			else:
				copytree(file, temp+tempf+ends)
		
	return list

def searchtar(t, val, reportfolderbase):
	temp = reportfolderbase+'Extraction/'
	pathlist = []
	for member in t.getmembers():
		if fnmatch.fnmatch(member.name, val):
			t.extract(member.name, path=temp)
			pathlist.append(temp+member.name)
	return pathlist

def searchzip(z, name_list, val, reportfolderbase):
	temp = reportfolderbase+'Extraction'
	pathlist = []
	for member in name_list:
		if fnmatch.fnmatch(member, val):
			z.extract(member, path=temp)
			pathlist.append(temp+member)
	return pathlist
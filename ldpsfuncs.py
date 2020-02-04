import sqlite3
import sys, os, re
import glob
import datetime
import plistlib
import codecs
import json
import sqlite3
import io
import sys
import csv
import pathlib
import shutil
import textwrap
import base64
from time import process_time

nl = '\n' 
now = datetime.datetime.now()
currenttime = str(now.strftime('%Y-%m-%d_%A_%H%M%S'))
reportfolderbase = './LDPS_Run_'+currenttime+'/'
base = '/LDPS_Run_'+currenttime+'/'
temp = reportfolderbase+'temp/'

def logfunc(message=""):
	if pathlib.Path(reportfolderbase+'Script Logs/Screen Output.html').is_file():
		with open(reportfolderbase+'Script Logs/Screen Output.html', 'a', encoding='utf8') as a:
			print(message)
			a.write(message+'<br>')
	else:
		with open(reportfolderbase+'Script Logs/Screen Output.html', 'a', encoding='utf8') as a:
			print(message)
			a.write(message+'<br>')

def copytree(src, dst, symlinks=False, ignore=None):
	if not os.path.exists(dst):
		os.makedirs(dst)
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		if os.path.isdir(s):
			copytree(s, d, symlinks, ignore)
		else:
			if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
				shutil.copy2(s, d)

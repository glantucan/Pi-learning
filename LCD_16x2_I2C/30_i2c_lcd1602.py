#!/usr/bin/env python
import LCD1602
import time
from subprocess import *

def write_ips():
	eth = "ip -4 addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
	wlan = "ip -4 addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"
	eth = run_cmd(eth)
	wlan = run_cmd(wlan)
	
	print(eth)
	LCD1602.write(0, 0, 'e:%s  ' % eth.rstrip())
	LCD1602.write(0, 1, 'w:%s  ' % wlan.rstrip())
	time.sleep(2)

def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output


def destroy():
	pass	

if __name__ == "__main__":
	try:
		LCD1602.init(0x27, 1)	# init(slave address, background light)
		LCD1602.clear()
		counter = 0
		while counter < 10:
			write_ips()
			time.sleep(3)
			counter += 1
			print('Counting...%s/10' % counter)
		destroy()
			
			
	except KeyboardInterrupt:
		destroy()

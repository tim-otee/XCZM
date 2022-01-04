#!/usr/bin/env python

##\file paravis_dump_csv_concatinate.py
#
# This script concatinates 0 -> n CSV files dumped from Paravis/Paraview using the column head name.
#
# Author - Timothy Crump
#
# Inputs prompts for -
#
# - Directory location
# - Name of file
# - Number of files to interate over
#
# Outputs- to a "RESULTS" dated directory on the desktop 
#
# - Individual files labelled using column name


import csv, sys, os, numpy,subprocess, smtplib, time, shutil, datetime
import Tkinter, tkFileDialog, Tkconstants 
from Tkinter import * 
import matplotlib.pyplot as plt
import pylab as np
class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

DESKTOP=os.path.join(os.path.expanduser('~'), 'Desktop') 
SALOME=os.path.join(os.path.expanduser('~'), '/salome_meca/appli_V2015_2')
WORKING = os.path.join(os.path.expanduser('~'), DESKTOP + "/RESULTS_"+ datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) 
attempts=2 # Error attempts
os.makedirs(WORKING) # creates Working directory on desktop
# Landing page
def title():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("------------------------------------------------------------------------------")
	print("***"+colour.BLUE+ colour.BOLD +"                    Welcome to Tim's Code_Aster Tool Set                "+ colour.END+"***")
	print("------------------------------------------------------------------------------")	
	print("***"+colour.GREEN+"                      This contains a csv concatinater                  "+ colour.END+"***")	
	print("------------------------------------------------------------------------------")
	print("")
	print('                                       .                           ')  	
	print('                                      .:.                           ')  
	print('                                     .:::.                            ')
	print('                                    .:::::.')
	print('                                ***.:::::::.*** ')                                       
	print('                           *******.:::::::::.******* ')                                         
	print('                         ********.:::::::::::.******** ')                                      
	print('                        ********.:::::::::::::.********  ')                                        
	print("                        *******.::::::'***`::::.*******    ")                                       
	print("                        ******.::::'*********`::.******      ")                                       
	print("                         ****.:::'*************`:.****         ")                                     
	print("                           *.::'*****************`.*             ")                                  
	print("                           .:'  ***************    .               ")                              
	print("                          .")
	print("")
	raw_input("Press the <ENTER> key to start..."+colour.RED+ colour.BOLD +"                     - To infinity and beyond! "+ colour.END) #Pause torun when happy			

	return 

#def pp_multi_crack():
	
os.system('cls' if os.name == 'nt' else 'clear') # clears screen
root = Tk()
root.withdraw()
print('Choose your REPE_OUT with the RMEDs:')
REPE = tkFileDialog.askdirectory(parent=root, initialdir=DESKTOP, title='Select your REPE_OUT')
os.chdir(REPE)

for i in range(105):
	subprocess.check_output("convert -delay 50 g.gif image."+str(i)+".png g.gif", shell=True,)		

#    return

'''
while attempts > 0:
	try:
		#title()
		pp_multi_crack()
		os.system('cls' if os.name == 'nt' else 'clear')	
		print("-------------------------------------------")			
		print("END- Please close the terminal")
		print("-------------------------------------------")			
		break
		
	except:
		try:
			os.remove(new_file) #trys to remove temp files created
		except:
			pass
		print("------------------------------------------------------------------------")	
		print "You made a mistake you " + colour.YELLOW + colour.BOLD + "LEMON" + colour.END+"... Try again... Pick a RESU (CTRL+Z =Exit)."
		print str(attempts-1) + " attempts left:"
		print("------------------------------------------------------------------------")	
		attempts= attempts-1 
'''

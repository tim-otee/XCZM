#/usr/bin/python
'''This file runs has a suite of scripts to make code_aster nicer to use!'''

import csv 
import sys
import os
import numpy
import subprocess 
import smtplib
import time
import shutil
import datetime
import Tkinter
import tkFileDialog
import Tkconstants 
from Tkinter import * 
import matplotlib.pyplot as plt
import pylab as np

DESKTOP=os.path.join(os.path.expanduser('~'), 'Desktop') # Desktop quick loc
DROPBOX=os.path.join(os.path.expanduser('~'), 'Dropbox') # Dropbox quick loc
SALOME=os.path.join(os.path.expanduser('~'), '/salome_meca/appli_V2016')
WORKING = os.path.join(os.path.expanduser('~'), DESKTOP + "/Results/RESULTS_"+ datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) 
# Working directory made in choose()
attempts=1 # Error attempts

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

# Landing page
def title():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("------------------------------------------------------------------------------")
	print("***"+colour.BLUE+ colour.BOLD +"               Welcome to Tim's Code_Aster user suite v0.5              "+ colour.END+"***")
	print("------------------------------------------------------------------------------")	
	print("***"+colour.GREEN+"  This contains 5 simple tools to aide your every day Code_Aster life!  "+ colour.END+"***")	
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
#	print('                                .-.                                 ')
#	print('                               /_ _\                               ')
#	print('                               |o^o|                               ')
#	print('                               \ _ /                               ')
#	print("                              .-'-'-.              BLEEP BOOP BLOOP ")
#	print('                            /`)  .  (`\            (THIS MEANS YES) ')
#	print("                           / /|.-'-.|\ \         /                 ")
#	print('                           \ \| (_) |/ /  .-""-.                   ')
#	print("                            \_\'-.-'/_/   /[] _ _\                  ")
#	print('                            /_/ \_/ \_\ _|_o_LII|_                 ')
#	print("                              |'._.'|  / | ==== | \                ")
#	print('                              |  |  |  |_| ==== |_|                ')
#	print('                               \_|_/    ||" ||  ||                 ')
#	print('                               |-|-|    ||LI  o ||                 ')
#	print("                               |_|_|    ||'----'||                 ")
#	print('                              /_/ \_\  /__|    |__\       ')
	raw_input("Press the <ENTER> key to start..."+colour.RED+ colour.BOLD +"                     - To infinity and beyond! "+ colour.END) #Pause torun when happy			

	return 

# Video converter
def videoconvert():
	print("-------------------------------------------")	
	print("Salome Run Finished Images Converting to GIF")
	print("-------------------------------------------")	
	RESULTS=os.path.join(os.path.expanduser('~'), WORKING) # desktop path
	os.chdir(RESULTS) # change back to desktop
	os.system("convert -delay 20 -loop 0   image*.png   animated.gif")
	pass

# Email contact
msg=None
def contact(msg):
	MSG=msg
		

	fromaddr = ''
	toaddrs  = ''

# Credentials (if needed)
	username = ''
	password = ''

	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, MSG)
	server.quit()

	del MSG
	
	pass

# Post processes with Salome
def post_multi_files():
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print("------------------------------------------------------------------------------")
	print(colour.BOLD +"***                            Salome-script repeater                      ***"+ colour.END)
	print("------------------------------------------------------------------------------")
	print("This involves:")	
	print("")	
	print("- Selecting the directory (REPE_OUT) containing your result meshes")	
	print("- Selecting the study-dump script to repeat from Salome-Meca (2015.2 currently)")
	print("- And within that script setting the INPUT and OUTPUT flags")		
	print("  for where  the input file name is and out file name is in this script")	
	print("")
	print("EXAMPLE:")
	print("")
	print(colour.GREEN + colour.BOLD +"INPUT FLAG" + colour.END +"- RESULTSrmed = MEDReader(FileName="+colour.RED + colour.BOLD +"INPUT"+ colour.END+")")
	print(colour.GREEN + colour.BOLD +"OUTPUT FLAG" +colour.END + "- SaveScreenshot("+colour.RED + colour.BOLD +"OUTPUT"+ colour.END+",magnification=1,quality=100,view=renderView1)")
	print(colour.BLUE+ colour.BOLD +"- NOTE you may need to hash-out the field selections, ie"+ colour.END)
	print("   ls_1med.AllArrays #"+colour.PURPLE + colour.BOLD +"EVERYTHING BEOYND THIS IN THIS LINE"+ colour.END)
	print("")
	#---------- Choosing working directory and study dump to use ------#
	root = Tk()
	root.withdraw()
	print('Choose your REPE_OUT with the RMEDs:')
	REPE = tkFileDialog.askdirectory(parent=root, initialdir=DESKTOP, title='Select your REPE_OUT')
	# Test if chosen a dir
	
	if REPE != "":
		pass
	else:
		return True		
	print('---------------------------------------------------')	
	print ("Directory Chosen:" + REPE)
	count = subprocess.check_output("ls "+ REPE+  " | grep .med  | wc -l", shell=True,)
	print (".med files in directory: " + count)
	count1 = subprocess.check_output("ls "+ REPE+  " | grep .rmed  | wc -l", shell=True,)
	print (".rmed files in directory: " + count1)
	print('---------------------------------------------------')
	# --- TEST input if empty end
	if int(count) != 0 or int(count1) != 0:
		pass
	else:
		return True	

	
	n=raw_input("Number (n) of output files to repeat over (0 -> n): ")
	x=int(n)
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print('Pick study dump (the post process you want to repeat):')
	study = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your Study dump file', filetypes=[('Study dump (Python)', '.py')]) 
	
		# --- TEST input if empty end
	if study != "":
		pass
	else:
		return True
	
	WR=None
	iname=None
	oname=None
	iend=None
	oend=None
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print('---------------------------------------------------')
	over=raw_input("Default is to process ls_[i].med to output[i].png. To use own please type[y]: ")
	wr=str(over)
	WR=wr
	# overwrite variables

	if WR != "y":
		pass
	else:
		iname=raw_input("OK, Great. Please enter" + colour.RED+ colour.BOLD + " INPUT "  + colour.END +"filename that is iteratered over (1/4): ")	
		iend=raw_input("Now please enter INPUT" + colour.RED+ colour.BOLD + " .Filextension "  + colour.END +"(2/4): ")	
		oname=raw_input("Now please enter" + colour.RED+ colour.BOLD + " OUTPUT "  + colour.END +" filename that is iteratered over (3/4): ")			
		oend=raw_input("Now please enter OUTPUT"+ colour.RED+ colour.BOLD + " .Filextension " + colour.END + "(4/4): ")	
		pass
	print('---------------------------------------------------')
		
	SALOME=os.path.join(os.path.expanduser('~'), 'salome_meca/appli_V2015_2') #Salome installation path
	os.chdir(SALOME) # change run directory to salome
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print("--------------------------------------------")
	print(colour.RED+ colour.BOLD + "Have you set the INPUT and OUTPUT file flags in:"+ colour.END +study +colour.RED+ colour.BOLD + "  ?"+ colour.END  )
	print("--------------------------------------------")		
	raw_input("If so, press the <ENTER> key to repeat study "+ colour.RED+ colour.BOLD + str(x) + colour.END +" times (2/2)...") #Pause to run when happy	
	STUDYNEW='repeated_study'+'.py'
	new_file =os.path.join(os.path.expanduser('~'), WORKING, STUDYNEW)	
	shutil.copy2(study, new_file)
	INPUT=[]   # Flags for dumpfile
	OUTPUT=[]

	STUDY= new_file 


	#------------------------ Main repeat loop ------------------------#
	for i in range(0,x): 
		
		IN="INPUT="+"'"+REPE+"/SIGM_NOEU_PSC_s17_refined"+str(i)+".rmed'"
		OUT="OUTPUT='"+WORKING+"/image."+str(i)+".png'"
		# OVERWRITES flags if y
		if WR == "y":
			IN="INPUT="+"'"+REPE+"/"+iname+str(i)+iend+"'"
			OUT="OUTPUT='"+WORKING+"/"+oname+str(i)+oend+"'"		
			pass
		else:
			pass
		
		os.system('cls' if os.name == 'nt' else 'clear')# clears screen
		INPUT.append(IN)
		OUTPUT.append(OUT)	
		
		#Prints at top of screen the working reuslt file	

		print('---------------------------------------------------')
		print(INPUT[i])		
		print(OUTPUT[i])
				
		with open(STUDY, "r+") as f:
			old = f.read() # read everything in the file
			f.seek(0) # rewind
			f.write(OUTPUT[i] +"\n"+ old) # write the new line before
		f.close()
		
		with open(STUDY, "r+") as f:
			old = f.read() # read everything in the file
			f.seek(0) # rewind
			f.write(INPUT[i] +"\n"+ old) # write the new line before
		f.close()
		
		X=str("./runSession -t " + STUDY)
		
		print("Running CTRL + Z to Stop")
		print('---------------------------------------------------')		
		#os.system("./salome -t " + STUDY+ "> /dev/null 2>&1")
		
		os.system("./salome -t ") # turn salome on
		p=str("'"+"./salome -t "+ STUDY+"'")
		process=os.system("./runSession python "+ STUDY) 
		
		print 'process id:', os.getpid()
		# Needs improvement to stop naming service running out of ports
	
		
		lines = open(STUDY, 'r').readlines()
		lines[0] = ""
		lines[1] = ""
		file = open(STUDY, 'w')
		for line in lines:
			file.write(line)
		file.close()	
		os.system('cls' if os.name == 'nt' else 'clear')
		print("-------------------------------------------")
		print("Ending Salome server")
		print("-------------------------------------------")	
		process=os.system("./runSession killSalome.py ")  # turn salome off
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Salome Run Finished")
	#------------------------------------------------------------------#
	os.remove(new_file)	
	videoconvert()	
	return

# Post Salome script different timesteps 
def post_same_file_different_time_steps():
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print("------------------------------------------------------------------------------")
	print(colour.BOLD +"***                   Paravis RMED Time-step post-processor                ***"+ colour.END)
	print("------------------------------------------------------------------------------")
	print("This involves:")	
	print(" - Selecting the RMED/MED to process")
	print(" - Selecting the study-dump script to repeat from Salome-Meca (2015.2 currently)")
	print(" - And within that script setting the INPUT, TIME and OUTPUT flags")	
	print("")
	print(colour.RED + colour.BOLD + "EXAMPLE:" + colour.END)
	print(colour.GREEN + colour.BOLD +"INPUT FLAG" + colour.END +"- REULSTrmed = MEDReader(FileName="+colour.RED + colour.BOLD +"INPUT"+ colour.END+")")
	print(colour.GREEN + colour.BOLD +"TIME FLAG" + colour.END + "- Uses annotate time filter to iterate over time. Needs to be inserted before OUTPUT & should not be in study dump prior to avoid clash:")
	print("    tsteps = REULSTrmed.TimestepValues")
	print("    annTime = AnnotateTimeFilter(REULSTrmed)")
	print("    annTime.Format = 'Time: %g'")
	print("    Show(annTime)")
	print("    renderView1.ViewTime = tsteps["+colour.RED + colour.BOLD +"TIME"+ colour.END+"]")
	print("    Render()")
	print(colour.GREEN + colour.BOLD +"OUTPUT FLAG" +colour.END + "- SaveScreenshot("+colour.RED + colour.BOLD +"OUTPUT"+ colour.END+",magnification=1,quality=100,view=renderView1)")
	print(colour.BLUE+ colour.BOLD +"- NOTE you may need to hash-out the field selections, ie"+ colour.END)
	print("   ls_16med.AllArrays #"+colour.PURPLE + colour.BOLD +"EVERYTHING BEOYND THIS IN THIS LINE"+ colour.END)
	print("")
	#---------- Choosing RMED to use ------#
	root = Tk()
	root.withdraw()
	print('Choose your large RMED:')
	REPE = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your .RMED file', filetypes=[('Result mesh', '.rmed'),('mesh', '.med')]) 
	# Test if chosen a dir
	
	if REPE != "":
		pass
	else:
		return True		
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen	
	

	print('Pick study dump (the post process you want to repeat):')
	study = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your Study dump file', filetypes=[('Study dump (Python)', '.py')]) 
	
	# --- TEST input if empty end
	if study != "":
		pass
	else:
		return True
		
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen	
	print('---------------------------------------------------')	
	print ("Chosen RMED file:" + REPE)	
	print ("Chosen Study Dump file:" + study)
	print('---------------------------------------------------')
	n=raw_input("Number (n) of timesteps to repeat over (0 -> n): ")
	x=int(n)
	
		
	SALOME=os.path.join(os.path.expanduser('~'), '/home/mbgnktc2/salome_meca/appli_V2016')
	os.chdir(SALOME) # change run directory to salome
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print("--------------------------------------------")
	print(colour.RED+ colour.BOLD + "Have you set the INPUT, TIME and OUTPUT file flags in:"+ colour.END +study +colour.RED+ colour.BOLD + "  ?"+ colour.END  )
	print("--------------------------------------------")		
	raw_input("If so, press the <ENTER> key to sparse memory process: "+ REPE + "...") #Pause to run when happy	
	STUDYNEW='repeated_study'+'.py'
	new_file =os.path.join(os.path.expanduser('~'), WORKING, STUDYNEW)	
	shutil.copy2(study, new_file)
	INPUT=[]   # Flags for dumpfile
	OUTPUT=[]
	TIME=[]
	STUDY= new_file 
	print "TEST"
	
	#------------------------ Main repeat loop ------------------------#
	for i in range(0,x): 
		
		IN="INPUT='"+str(REPE)+"'"
		OUT="OUTPUT='"+WORKING+"/image"+str(i)+".png'"
		Time="TIME=int("+str(i)+")" #str(i*10)
		
		os.system('cls' if os.name == 'nt' else 'clear')# clears screen
		INPUT.append(IN)
		OUTPUT.append(OUT)	
		TIME.append(Time)
		
		#Prints at top of screen the working reuslt file	

		print('---------------------------------------------------')
		print(INPUT[i])		
		print(OUTPUT[i])
		print(TIME[i])
					
		with open(STUDY, "r+") as f:
			old = f.read() # read everything in the file
			f.seek(0) # rewind
			f.write(OUTPUT[i] +"\n"+ old) # write the new line before
		f.close()
		
		with open(STUDY, "r+") as f:
			old = f.read() # read everything in the file
			f.seek(0) # rewind
			f.write(INPUT[i] +"\n"+ old) # write the new line before
		f.close()

		with open(STUDY, "r+") as f:
			old = f.read() # read everything in the file
			f.seek(0) # rewind
			f.write(TIME[i] +"\n"+ old) # write the new line before
		f.close()		 

		X=str("./runSession -t " + STUDY)
		
		print("Running CTRL + Z to Stop")
		print('---------------------------------------------------')		
		#os.system("./salome -t " + STUDY+ "> /dev/null 2>&1")
		
		os.system("./salome -t ") # turn salome on
		p=str("'"+"./salome -t "+ STUDY+"'")
		process=os.system("./runSession python "+ STUDY) 
		
		print 'process id:', os.getpid()
		# Needs improvement to stop naming service running out of ports
	
		
		lines = open(STUDY, 'r').readlines() #deleteing lines added
		lines[0] = ""
		lines[1] = ""
		lines[2] = ""		
		file = open(STUDY, 'w')
		for line in lines:
			file.write(line)
		file.close()	
		os.system('cls' if os.name == 'nt' else 'clear')
		print("-------------------------------------------")
		print("Ending Salome server")
		print("-------------------------------------------")	
		process=os.system("./runSession killSalome.py ")  # turn salome off
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Salome Run Finished")
	#------------------------------------------------------------------#

	os.remove(new_file)		
	videoconvert()
	return

# Plotting RESU via node name
def plotter():
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print("------------------------------------------------------------------------------")
	print(colour.BOLD +"***                               RESU PLOTTER                             ***"+ colour.END)
	print(colour.BOLD +"***                        Currently just 2 columns                        ***"+ colour.END)
	print("------------------------------------------------------------------------------")
	print("This involves:")	
	print("- Selecting a .resu file")	
	print("- Entering node number or name ")
	print("- Selecting 2 columns to print")
	print("- It then saves .csv or data and then a .png image and presents graph")			
	print("")
	#---------- Choosing Resu to use ------#
	root = Tk()
	root.withdraw()
	print('Choose your .resu file:')
	resu = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your RESU file', filetypes=[('Aster_RESU', '.resu'),('Concatinated (csv)', '.csv')]) 
	# Test if chosen a dir
	CURRENT=os.path.dirname(os.path.realpath(resu))
	xx=[]
	yy=[]
	nodes=[]
	Varibles=[]

	file=open(resu,'r')
	print "- File opened:  " + resu

	for line in file:
	   
	   if ' NOEUD    :' in line: # finds node list ... needs improvement to be used on any resu
		   nodes= line
	   if ' NOEUD ' in line: # finds node list ... needs improvement to be used on any resu
		   words=line.split()
		   Varibles= words	   
		   
	file.close()

	print ("- Nodes that can be plotted: " + str(nodes))
	print ("- Columns that can be plotted: " + str(Varibles))
	print("------------------------------------------------------------------")
	f=open(resu,'r')

	#############################Input_Vars###############################   
	input_var = raw_input("Enter node number/name: ")
	Column1= raw_input("Column1: ")
	Column2= raw_input("Column2: ")
	x1=int(Column1)
	x2=int(Column2)

	while input_var != "":

		f=open(resu,'r')

		n=" " + input_var +" "
		
		#############################Finds_ nodes#############################
		nx=Nx=[]
		ny=Ny=[] 
		INST=[]	   
		xlabel=['Time']
		ylabel1=[]
		ylabel2=[]
		
		for line in f:
			if line.startswith(' NUMERO'):
				words=line.split()
				INST.append(words[4])
			
			if line.startswith(' NOEUD'):
				words=line.split()
				ylabel1.append(words[x1])
				ylabel2.append(words[x2])
			 
			if line.startswith(n):
				if line.startswith(n):
					words=line.split()
					nx.append(words[x1])
					ny.append(words[x2])		 
		######################### PRINTS CSV##################################
		CSV='result_'+ylabel1[1]+'_'+input_var+'.xls'
		csv_file =os.path.join(os.path.expanduser('~'), WORKING, CSV)
		#csv_file = r"results.csv"
		l=[INST,nx,ny]
		#print l
		with open(csv_file, "wb") as f:
			writer = csv.writer(f)
			writer.writerows(zip(*l))
	######################### PRINTS GRAPH################################
		#for x in ny:
		#	Ny[i]=int(ny[:x])/density
		#plt.ion()
		
		ax1=plt.subplot(211)
		plt.title(n)
		plt.plot(INST, nx, 'r-')
		ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))
		plt.xlabel('Time (INST) [s]')
		plt.ylabel(ylabel1[1],)
		
		ax2=plt.subplot(212)
		plt.plot(INST, ny, 'r-')
		ax2.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
		plt.xlabel('Time (INST) [s]')
		plt.ylabel(ylabel2[2],)
		
		
		PLOT='plots_'+ylabel1[1]+'_'+input_var +'.png'
		plt.savefig(os.path.join(os.path.expanduser('~'), WORKING, PLOT)) 
		
		os.system('cls' if os.name == 'nt' else 'clear')
		print("------------------------------------------------------------------")	
		print("- You have opened: " + resu )
		print("- For Node: " + colour.RED + colour.BOLD + input_var + colour.END)
		print("- Figure and Excel file saved in" +WORKING)
		print("- Clever you!!! =]  ...CTL+Z = exit")

		
		plt.show(block=False) #stops the blocking of command running 
			
		print ("- Nodes that can be plotted: " + str(nodes))
		print("------------------------------------------------------------------")	
		
		input_var = raw_input("Enter node number/name: ") # new node number
		plt.figure()  # new plot window

			
		del n,nx,ny
		
	f.close()		
	return	

# Run Code_Aster Case
def runcase():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("------------------------------------------------------------------------------")
	print(colour.BOLD +"***                   Welcome to Tim's Aster case executor                 ***"+ colour.END)
	print("------------------------------------------------------------------------------")
	print("This involves:")		
	print(" ")	
	print("- Runs Aster Case")
	print("- Post-processes it with Paravis")
	print("- Then contacts you by email")
	print(" ")
	raw_input("Press the <ENTER> key to start (1/2)...") #Pause torun when happy
	

	# Error checking

	root = Tk()
	root.withdraw() # we don't want a full GUI, so keep the root window from appearing
	print('Choose Export file from ASTK:') 
	EXPORT = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your export file', filetypes=[('ASTK_export_file', '.export'),]) 
	Asterexport='Asterexportrun'+'.py'
	new_file =os.path.join(os.path.expanduser('~'), WORKING, Asterexport)	
	shutil.copy2(EXPORT, new_file)
	#/home/mbgnktc2/Documents/Salome_post_process/post_process_GBrick.py

	print('Pick study dump (the post process you want to repeat):')
	study = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your Study dump file', filetypes=[('Study dump (Python)', '.py')]) 
	#show an "Open" dialog box and return the path to the selected file
	CURRENT=os.path.dirname(os.path.realpath(EXPORT))
	ASRUN=os.path.join(os.path.expanduser('~'), '/opt/aster/bin/')
	os.chdir(ASRUN) 
	print("--------------------------------------------")
	raw_input("Press the <ENTER> key to run case (2/2)...") #Pause torun when happy
	os.system("./as_run " + new_file +" | tee "+ WORKING +"/log_astercase.txt") 
	
	msg = 'Model has finished and results should be on Desktop in log in' + str(WORKING)
	contact(msg)	
	
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen	
	os.chdir(SALOME) # change run directory to salome
	os.system("./salome -t " + study)
	#videoconvert() #Global video convert
	
	#r=os.path.join(os.path.expanduser('~'), WORKING +"/log_astercase.txt")

	msg = 'Postprocessing has finished and results should be on Desktop' + str(WORKING)
	contact(msg)	
	
	return

# Collect data from csv's exported from paravis
def concatinate_csv():
	
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen

			
	print("------------------------------------------------------------------------------")
	print(colour.BOLD +"***                             CSV Concatinate                            ***"+ colour.END)
	print("------------------------------------------------------------------------------")
	print(" ")	
	print("Concatinates columns from 0->n files using column title in first cell in a CSV.")
	print(" ")	
	root = Tk()
	root.withdraw()
	print('Choose the directory/folder with the CSVs:')
	csvs = tkFileDialog.askdirectory(parent=root, initialdir=DESKTOP, title='Select your dir')	

	NAME=str(raw_input("File Name: "))
	name=[NAME]# Add to list of N names for more file names in directory to concatinate

	n=int(raw_input("Number (n) of output files to repeat over (0 -> n): "))
	CSVS=os.path.join(os.path.expanduser('~'), csvs )

	FILE_NAMES=[]
	DATA=[]
	CLIST=[]
	CLISTL=[]
	X=[]
	D=[]
	N=int(len(name))
	os.chdir(CSVS)	

	################################
	# LOOP
	# - z names
	################################
	for z in range(0,N):
		file=name[z]+'.'+str(0)+'0.csv' #file='results0.0.csv'
		FILE_NAMES.append(file)
		
		# Getting number to run loop over
		with open(file, 'r') as f:
			csvReader1 = csv.reader(f,delimiter=',')
			for row in csvReader1:
				row1 = csvReader1.next()
				D=int(len(row1))
			f.close()


			for Y in range(0,D): 
				os.system('cls' if os.name == 'nt' else 'clear') # clears screen
				print "Concatinating column ",Y+1," of ",D, " of file", N, " named ", name[z],".csv"
				
				for x in range(0,n): 
					file=name[z]+'.'+str(x)+'.csv' #file='results0.0.csv'
					FILE_NAMES.append(file)
					# Getting list of headers to work over, 
					# repeats count to check, if not error
					with open(file, 'r') as f:
						csvReader1 = csv.reader(f,delimiter=',')
						for row in csvReader1:

							row1 = csvReader1.next()
							CLISTL=int(len(row1))
							for t in range(0,CLISTL+1):
								CLIST.append(list(row[0:t]))		
					X= CLIST[CLISTL]
					# New name
					CT= str(X[Y])
					
					# open the file in universal line ending mode 
					with open(file, 'rU') as infile:
					  # read the file as a dictionary for each row ({header : value})
					  reader = csv.DictReader(infile)
					  data = {}
					  for row in reader:
						for header, value in row.items():
						  try:
							data[header].append(value)
						  except KeyError:
							data[header] = [value]
					#Appending column data to array		
					DATA.append(data[CT])
				# Write CSV
				CSV='CONCATINATED_'+str(name[z])+'_'+CT+'.csv'
				csv_file =os.path.join(os.path.expanduser('~'), WORKING, CSV)	
				with open(csv_file, "wb") as f:
					writer = csv.writer(f)	
					writer.writerows(zip(*DATA))
					f.close()	
				
				# clear arrays each file!
				del DATA[:], csv_file, CSV
	print(" ")
	print("DONE! ")
	print "Please see csv file's in:", str(WORKING)
	return

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
# gif_maker for multi_cracks case run
def gif_maker():
	os.chdir(WORKING)
	count1 = subprocess.check_output("ls "+ WORKING+  " | grep .png | wc -l", shell=True,)
	print (".png files in directory: " + count1)
	print "Processing image 1/"+str(count1)
	subprocess.check_output("convert -delay 50 image."+str(0)+".png ani.gif", shell=True,)	

	for i in range(1,int(count1)):
		subprocess.check_output("convert -delay 50 ani.gif image."+str(i)+".png ani.gif", shell=True,)		
		print "Processing image "+str(i+1)+"/"+str(count1)	
	return	

# graph production for multi_cracks case run
def produce_graphs_data():

	print('Choose your .resu file:')
	#resu = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your RESU file', filetypes=[('Aster_RESU', '.resu'),('Concatinated (csv)', '.csv')]) 
	resu =os.path.join(os.path.expanduser('~'), '/home/mbgnktc2/Desktop/TEST_XCZM_MC/textresultstest.resu')
	#resu =os.path.join(os.path.expanduser('~'), CURRENT_CASE, 'textresultstest.resu')
	print('Choose your .mess file:')
	#mess = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your MESS file', filetypes=[('Aster_RESU', '.mess'),('Concatinated (csv)', '.csv')]) 
	mess =os.path.join(os.path.expanduser('~'), '/home/mbgnktc2/Desktop/TEST_XCZM_MC/messagestest.mess')
	#mess = os.path.join(os.path.expanduser('~'), CURRENT_CASE, 'messagestest.mess')

	print resu
	print mess
	STUDYNEW='working_file'+'.resu'
	new_file =os.path.join(os.path.expanduser('~'), WORKING, STUDYNEW)	
	shutil.copy2(resu, new_file)

	STUDYNEW1='working_file'+'.mess'
	new_file1 =os.path.join(os.path.expanduser('~'), WORKING, STUDYNEW1)	
	shutil.copy2(mess, new_file1)
	#n=int(raw_input("Number (n) of cracks: "))
	n=2
	nb_front=2
	inst=[]; angle=[]; k1=[]; k2=[]; k3=[]; g=[]; gi=[]; da=[]
	# Find list of insts from resu... n is the crack interval 
	f=open(new_file,'r')
	for line in f:
		# Time - isnt
		if line.startswith('# Time '):
			words=line.split()
			inst.append(float(words[2]))

		# From SD_table 
		if line.startswith('            1'):
			words=line.split()
			k1.append(float(words[5]))
			k2.append(float(words[6]))
			k3.append(float(words[7]))
			g.append(float(words[8]))
			angle.append(float(words[9]))
			gi.append(float(words[10]))
	f.close        

	k1=zip(k1) # zip the list together
	k2=zip(k2)
	k3=zip(k3)
	g=zip(g)
	gi=zip(gi)
	angle=zip(angle)

	# Crack advance   
	file = open(new_file, 'r')
	for line in file:
		if "CRACK0" in str(line): 
			for i in range(1):# print to extension
				X=file.next()
				x=X.strip()
				da.append(float(x)) 
				
				
	#-----------------------------------------------------------------------
	# Stripping speeds from .mess file
	#-----------------------------------------------------------------------
	'''
	w_file =os.path.join(os.path.expanduser('~'), WORKING, 'WORKING_.csv') 
	with open(w_file, "wr+") as f:
		f.write(" "+' \n') # write the new line before   
	file = open(new_file1, 'r')
	SPEED=[]
	TABLET="  NUM_PT    VITESSE         BETA          VT            VN"
	with open(w_file, "r+") as f:
		for line in file:
			if TABLET in str(line): 
				X=file.next()
				x=X.strip().replace("D", "E")# converts fortran D to python E
				x=x.replace("     ", ",")
				x=x.replace("    ", ",")
				x=x.replace("   ", ",")
				old=f.read()
				f.write(old+str(x)+', \n') # write the new line before
	f.close()
	file.close()
	n=[]
	with open(w_file, 'rU') as data:
		reader = csv.reader(data, delimiter=',')
		for column in reader:
			SPEED.append(column[3:4])#VT, VN = column[4:5]
	print SPEED
	'''

	#-------------------------------------------------------------------------
	# Ordering lists                                  
	#-------------------------------------------------------------------------                                  

	INST=inst[1::n]; ANGLE=[]; K1=[]; K2=[]; K3=[]; G=[]; GI=[]; DA=[]; DDA=[]
	ANGLE1=[]; K11=[]; K21=[]; K31=[]; G1=[]; GI1=[]; DA1=[]; DDA1=[]
	ANGLE2=[]; K12=[]; K22=[]; K32=[]; G2=[]; GI2=[]; DA2=[]; DDA2=[]
	DA=[]

	# create a list for each crack 1 - n
	for N in range(0,len(angle),4):

		ANGLE1.extend(angle[N])
		K11.extend(k1[N])
		K21.extend(k2[N])
		K31.extend(k3[N])
		G1.extend(g[N])
		GI1.extend(gi[N])

	K1.append(K11)
	K2.append(K21)
	K3.append(K31)
	G.append(G1)
	GI.append(GI1)
	ANGLE.append(ANGLE1)

	# create a list for each crack 1 - n
	for N in range(2,len(angle),4):

		ANGLE2.extend(angle[N])
		K12.extend(k1[N])
		K22.extend(k2[N])
		K32.extend(k3[N])
		G2.extend(g[N])
		GI2.extend(gi[N])

	K1.append(K12)
	K2.append(K22)
	K3.append(K32)
	G.append(G2)
	GI.append(GI2)
	ANGLE.append(ANGLE2)

	DA.append(da[0::2])# Evens
	DA.append(da[1::2])#odds    

	#-------------------------------------------------------------------------
	# Saving CSV                                
	#-------------------------------------------------------------------------      
	CSV='result_'+'_'+'.xls'
	csv_file =os.path.join(os.path.expanduser('~'), WORKING, CSV)
	#csv_file = r"results.csv"
	l=[INST,DA[0],DA[1],ANGLE[0],ANGLE[1],K1[0],K1[1],K2[0],K2[1],K3[0],K3[1],G[0],G[1],GI[0],GI[1]]
	L=[str("PRINT_ORDER"),str("INST"),str("DA[0]"),str("DA[1]"),str("ANGLE[0]"),str("ANGLE[1]"),str("K1[0]"),str("K1[1]"),str("K2[0]"),str("K2[1]"),str("K3[0]"),str("K3[1]"),str("G[0]"),str("G[1]"),str("GI[0]"),str("GI[1]")]
	#print l
	with open(csv_file, "wb") as f:
		writer = csv.writer(f,delimiter =",")
		writer.writerows(zip(*l))
		writer.writerows(zip(L))


	#-------------------------------------------------------------------------
	# Plotting                        
	#-------------------------------------------------------------------------          
		
	plt.figure(1)
	ax1=plt.subplot(211) # 3 graphs = 311
	plt.title("Crack Extension")
	plt.plot(INST,np.cumsum(DA[0]), color='Red', linewidth=3)
	plt.plot(INST,np.cumsum(DA[1]), color='Blue', linewidth=3)
	ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))

	ax1.legend( ("Crack_0", "Crack_1"), loc='best')
	plt.xlabel('Time (INST) [s]')
	plt.ylabel("Crack extenstion",)


	ax1=plt.subplot(212) # 3 graphs = 311
	plt.title("Crack ANGLE")
	plt.plot(INST,ANGLE[0], color='Red', linewidth=3)
	plt.plot(INST, ANGLE[1], color='Blue', linewidth=3)
	ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))
	ax1.legend( ("Crack_0", "Crack_1"), loc='best')
	plt.xlabel('Time (INST) [s]')
	plt.ylabel("ANGLE [RADS]",)

	my_dpi=300
	PLOT='FIGURE_1'+'.png'
	# TkAgg backend
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())
	plt.show(block=False)
	plt.savefig(os.path.join(os.path.expanduser('~'), WORKING, PLOT),  dpi=my_dpi) 

	plt.figure(2)
	ax1=plt.subplot(311) # 3 graphs = 311
	plt.title("K1")
	plt.plot(INST,K1[0], color='Red', linewidth=3)
	plt.plot(INST, K1[1], color='Blue', linewidth=3)
	ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))

	ax1.legend( ("Crack_0", "Crack_1"), loc='best')
	plt.xlabel('Time (INST) [s]')
	plt.ylabel("Stress Intensity",)

	ax2=plt.subplot(312) # 3 graphs = 311
	plt.title("K2")
	plt.plot(INST,K2[1], color='Red', linewidth=3)
	plt.plot(INST, K2[0], color='Blue', linewidth=3)
	ax2.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))

	ax2.legend( ("Crack_0", "Crack_1"), loc='best')
	plt.xlabel('Time (INST) [s]')
	plt.ylabel("Stress Intensity",)

	ax3=plt.subplot(313) # 3 graphs = 311
	plt.title("K3")
	plt.plot(INST,K3[0], color='Red', linewidth=3)
	plt.plot(INST, K3[1], color='Blue', linewidth=3)
	ax3.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))

	ax3.legend( ("Crack_0", "Crack_1"), loc='best')
	plt.xlabel('Time (INST) [s]')
	plt.ylabel("Stress Intensity",)


	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())
	PLOT='FIGURE_2'+'.png'
	plt.show(block=False)
	plt.savefig(os.path.join(os.path.expanduser('~'), WORKING, PLOT),  dpi=my_dpi) 

	plt.figure(3)
	ax1=plt.subplot(211) # 3 graphs = 311
	plt.title("G")
	plt.plot(INST,G[0], color='Red', linewidth=3)
	plt.plot(INST, G[1], color='Blue', linewidth=3)
	ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))

	ax1.legend( ("Crack_0", "Crack_1"), loc='best')
	plt.xlabel('Time (INST) [s]')
	plt.ylabel("Strain energy release rate [G]",)

	ax2=plt.subplot(212) # 3 graphs = 311
	plt.title("G_IRWIN")
	plt.plot(INST,GI[0], color='Red', linewidth=3)
	plt.plot(INST, GI[1], color='Blue', linewidth=3)
	ax2.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))

	ax2.legend( ("Crack_0", "Crack_1"), loc='best')
	plt.xlabel('Time (INST) [s]')
	plt.ylabel("Strain energy release rate [G_IRWIN]",)

	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())

	PLOT='FIGURE_3'+'.png'
	plt.show(block=False)
	plt.savefig(os.path.join(os.path.expanduser('~'), WORKING, PLOT),  dpi=my_dpi) 

	plt.show(block=False)

	return	

# POST PROCESSING FOR MULTI
def post_different_time_steps_MUTLI():
	#os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print("------------------------------------------------------------------------------")
	print(colour.BOLD +"***                   Paravis RMED Time-step post-processor                ***"+ colour.END)
	print("------------------------------------------------------------------------------")
	print("This involves:")	
	print(" - Selecting the RMED/MED to process")
	print(" - Selecting the study-dump script to repeat from Salome-Meca (2015.2 currently)")
	print(" - And within that script setting the INPUT, TIME and OUTPUT flags")	
	print("")
	print(colour.RED + colour.BOLD + "EXAMPLE:" + colour.END)
	print(colour.GREEN + colour.BOLD +"INPUT FLAG" + colour.END +"- REULSTrmed = MEDReader(FileName="+colour.RED + colour.BOLD +"INPUT"+ colour.END+")")
	print(colour.GREEN + colour.BOLD +"TIME FLAG" + colour.END + "- Uses annotate time filter to iterate over time. Needs to be inserted before OUTPUT & should not be in study dump prior to avoid clash:")
	print("    tsteps = REULSTrmed.TimestepValues")
	print("    annTime = AnnotateTimeFilter(REULSTrmed)")
	print("    annTime.Format = 'Time: %g'")
	print("    Show(annTime)")
	print("    renderView1.ViewTime = tsteps["+colour.RED + colour.BOLD +"TIME"+ colour.END+"]")
	print("    Render()")
	print(colour.GREEN + colour.BOLD +"OUTPUT FLAG" +colour.END + "- SaveScreenshot("+colour.RED + colour.BOLD +"OUTPUT"+ colour.END+",magnification=1,quality=100,view=renderView1)")
	print(colour.BLUE+ colour.BOLD +"- NOTE you may need to hash-out the field selections, ie"+ colour.END)
	print("   ls_16med.AllArrays #"+colour.PURPLE + colour.BOLD +"EVERYTHING BEOYND THIS IN THIS LINE"+ colour.END)
	print("")
	#---------- Choosing RMED to use ------#
	#root = Tk()
	#root.withdraw()
	print('Choose your large RMED:')
	#REPE = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your .RMED file', filetypes=[('Result mesh', '.rmed'),('mesh', '.med')]) 
	#REPE = os.path.join(os.path.expanduser('~'), '/home/mbgnktc2/Desktop/TEST_XCZM_MC/visualresultstest1.rmed')
	REPE = os.path.join(os.path.expanduser('~'), CURRENT_CASE, 'visualresultstest1.rmed')
	# Test if chosen a dir

	os.system('cls' if os.name == 'nt' else 'clear') # clears screen	


	print('Pick study dump (the post process you want to repeat):')
	#study = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your Study dump file', filetypes=[('Study dump (Python)', '.py')]) 
	#study = os.path.join(os.path.expanduser('~'), '/home/mbgnktc2/Desktop/TEST_XCZM_MC/Double_crack_study_dump.py')
	study = os.path.join(os.path.expanduser('~'), CURRENT_CASE, 'Double_crack_study_dump.py')
	# --- TEST input if empty end
	
		
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen	
	print('---------------------------------------------------')	
	print ("Chosen RMED file:" + REPE)	
	print ("Chosen Study Dump file:" + study)
	print('---------------------------------------------------')
	#n=raw_input("Number (n) of timesteps to repeat over (0 -> n): ")
	n=3
	x=int(n)

		
	SALOME=os.path.join(os.path.expanduser('~'), 'salome_meca/appli_V2015_2') #Salome installation path
	os.chdir(SALOME) # change run directory to salome
	os.system('cls' if os.name == 'nt' else 'clear') # clears screen
	print("--------------------------------------------")
	print(colour.RED+ colour.BOLD + "Have you set the INPUT, TIME and OUTPUT file flags in:"+ colour.END +study +colour.RED+ colour.BOLD + "  ?"+ colour.END  )
	print("--------------------------------------------")		
	print("If so, press the <ENTER> key to sparse memory process: "+ REPE + "...") #Pause to run when happy	
	#raw_input("If so, press the <ENTER> key to sparse memory process: "+ REPE + "...") #Pause to run when happy	
	STUDYNEW='repeated_study'+'.py'
	new_file =os.path.join(os.path.expanduser('~'), WORKING, STUDYNEW)	
	shutil.copy2(study, new_file)
	INPUT=[]   # Flags for dumpfile
	OUTPUT=[]
	TIME=[]
	STUDY= new_file 
	print "TEST"

	#------------------------ Main repeat loop ------------------------#
	for i in range(0,x): 
		
		IN="INPUT='"+str(REPE)+"'"
		OUT="OUTPUT='"+WORKING+"/image."+str(i)+".png'"
		Time="TIME=int("+str(i)+")" #str(i*10)
		
		os.system('cls' if os.name == 'nt' else 'clear')# clears screen
		INPUT.append(IN)
		OUTPUT.append(OUT)	
		TIME.append(Time)
		
		#Prints at top of screen the working reuslt file	

		print('---------------------------------------------------')
		print(INPUT[i])		
		print(OUTPUT[i])
		print(TIME[i])
					
		with open(STUDY, "r+") as f:
			old = f.read() # read everything in the file
			f.seek(0) # rewind
			f.write(OUTPUT[i] +"\n"+ old) # write the new line before
		f.close()
		
		with open(STUDY, "r+") as f:
			old = f.read() # read everything in the file
			f.seek(0) # rewind
			f.write(INPUT[i] +"\n"+ old) # write the new line before
		f.close()

		with open(STUDY, "r+") as f:
			old = f.read() # read everything in the file
			f.seek(0) # rewind
			f.write(TIME[i] +"\n"+ old) # write the new line before
		f.close()		 

		X=str("./runSession -t " + STUDY)
		
		print("Running CTRL + Z to Stop")
		print('---------------------------------------------------')		
		#os.system("./salome -t " + STUDY+ "> /dev/null 2>&1")
		
		os.system("./salome -t ") # turn salome on
		p=str("'"+"./salome -t "+ STUDY+"'")
		process=os.system("./runSession python "+ STUDY) 
		
		print 'process id:', os.getpid()
		# Needs improvement to stop naming service running out of ports

		
		lines = open(STUDY, 'r').readlines() #deleteing lines added
		lines[0] = ""
		lines[1] = ""
		lines[2] = ""		
		file = open(STUDY, 'w')
		for line in lines:
			file.write(line)
		file.close()	
		os.system('cls' if os.name == 'nt' else 'clear')
		print("-------------------------------------------")
		print("Ending Salome server")
		print("-------------------------------------------")	
		process=os.system("./runSession killSalome.py ")  # turn salome off
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Salome Run Finished")
	#------------------------------------------------------------------#

	os.remove(new_file)		
	return

def runcase_multi_cracks():
	#---------------------------------------------------------------
	#os.system('cls' if os.name == 'nt' else 'clear')
	#root = Tk()
	#root.withdraw()
	#print('Choose your ASTER_CASE directory :')
	#CURRENT_CASE= tkFileDialog.askdirectory(parent=root, initialdir=DESKTOP, title='Select your ASTER_CASE')
	#---------------------------------------------------------------
	os.system('cls' if os.name == 'nt' else 'clear')
	print("------------------------------------------------------------------------------")
	print(colour.BOLD +"***                   Welcome to Tim's Aster case executor                 ***"+ colour.END)
	print("------------------------------------------------------------------------------")
	print("This involves:")		
	print(" ")	
	print("- Runs Aster Case")
	print("- Post-processes it with Paravis")
	print("- Then contacts you by email")
	print(" ")
	raw_input("Press the <ENTER> key to start (1/2)...") #Pause torun when happy
	

	# Error checking

	root = Tk()
	root.withdraw() # we don't want a full GUI, so keep the root window from appearing
	print('Choose Export file from ASTK:') 
	EXPORT = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your export file', filetypes=[('ASTK_export_file', '.export'),]) 
	Asterexport='Asterexportrun'+'.py'
	new_file =os.path.join(os.path.expanduser('~'), WORKING, Asterexport)	
	shutil.copy2(EXPORT, new_file)
	#/home/mbgnktc2/Documents/Salome_post_process/post_process_GBrick.py

	print('Choose post_processing_script:') 
	#study = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your pp.py file', filetypes=[('PP py script', '.py'),]) 
	study =os.path.join(os.path.expanduser('~'),'/home/mbgnktc2/Desktop/TEST_XCZM_MC/POST_PROCESS_MULTI_CRACKS_ALL.py')	
	
	#show an "Open" dialog box and return the path to the selected file
	CURRENT=os.path.dirname(os.path.realpath(EXPORT))
	ASRUN=os.path.join(os.path.expanduser('~'), '/opt/aster/bin/')
	os.chdir(ASRUN) 
	print("--------------------------------------------")
	raw_input("Press the <ENTER> key to run case (2/2)...") #Pause torun when happy
	os.system("./as_run " + new_file +" | tee "+ WORKING +"/log_astercase.txt") 
	
	msg = 'Model has finished and results should be on Desktop in log in' + str(WORKING)
	contact(msg)	

	#/home/mbgnktc2/Desktop/TEST_XCZM_MC/POST_PROCESS_MULTI_CRACKS_ALL.py
	process=os.system("python "+ study) 
	msg = 'Postprocessing has finished and results should be on Desktop' + str(WORKING)
	contact(msg)	
	
	return
	
def mem():
    try:
		refresh=input("Refresh rate [seconds] (Default 60):")
		int(refresh)
    except:
        refresh=60
        pass               

    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------------------------------------------------")
    print "Running memory saving \n"
    Asterexport='Aster_run_mem_started_'+ '.csv'
    new_file =os.path.join(os.path.expanduser('~'), WORKING, Asterexport)   
    print "saving to data (CSV) and image to : \n "+ str(WORKING)+" of every "+str(refresh)+" seconds \n "
    print("------------------------------------------------------------------------------")
    with open(new_file, "wr+") as f:
        f.write("PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND  "+' \n') # write the new line before
    f.close()
    # time.sleep(60)
    TEST=True
    i= 0
    INST=[]
    Memory=[]
    
    #print("------------------------------------------------------------------------------")
    #print "Running memory saving with interval "+str(refresh)+" seconds \n"
    #print "saving to data (CSV) and image to : \n"+ str(WORKING)+" \n "
    #print "Inst =  "+str(i)+'\r'
    #print "Time =  "+str(int(i*refresh)/60)+" minutes "+'\r'
    #print("------------------------------------------------------------------------------")
    
    with open(new_file, "r+") as f:
     while (TEST==True):        
         INST.append(i)
         inst=[]
         for k in range(len(INST)):#minutes
			 inst.append(float(int(INST[k])*int(refresh))/float(60))
			 
         t=subprocess.check_output("top -b -n1 | grep aster", shell=True,)  
         print("------------------------------------------------------------------------------")
         print "Running memory saving with interval "+str(refresh)+" seconds \n"
         print "saving to data (CSV) and image to : \n"+ str(WORKING)+" \n "
         #print "Inst =  "+str(i)+'\r'
         #print "Time =  "+str(int(i*refresh)/60)+" minutes "+'\r'
         print("------------------------------------------------------------------------------")                
         old=f.read()
         f.write(old+str(t)+' \n') # write the new line before
         words=t.split()
         new_s = "".join(i for i in words[4] if i in "0123456789.")
         
         Memory.append(new_s)
         time.sleep(refresh)
         i=i+1
         os.system('cls' if os.name == 'nt' else 'clear')
         try:# Try to plot if not come back around
             ax1=plt.subplot(111)
             plt.title(" Memory (output per minute)")
             plt.plot(inst, Memory, 'r-')
             ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3,3))
             plt.xlabel('Time (INST) [Minutes]')
             plt.ylabel('Memory usage by Aster') 
             plt.draw()
             #plt.pause(0.005)
             PLOT='memory_'+'.png'
             plt.savefig(os.path.join(os.path.expanduser('~'), WORKING, PLOT))
             plt.close()
             del ax1
            
         except:
             print("------------------------------------------------------------------------------")
             print "Running memory saving with interval "+str(refresh)+" seconds \n"
             print "saving to data (CSV) and image to : \n"+ str(WORKING)+" \n "
             #print "Inst =  "+str(i)+'\r'
             #print "Time =  "+str(int(i*refresh)/60)+" minutes "+'\r'
             print("------------------------------------------------------------------------------")
    			 
             print "Failed to print graph"
             print Memory 
             print "len(Memory)"
             print len(Memory)
             print "len(INST)"
             print len(INST)
             del ax1
             print("------------------------------------------------------------------------------")             
             pass
             
 
             
         if ("aster" not in str(t)):
             TEST=False
         del t                   
    f.close()
    return	
    
def pp_mess_multi():
    crack_list=[]
    PRINT_OUT=[]

    STUDYNEW='OUTPUT_CRACK_PROPAGATION'+'.txt'
    new_file =os.path.join(os.path.expanduser('~'), WORKING, STUDYNEW)		
    STUDY= new_file 

    MESS=os.path.join(os.path.expanduser('~'), '/home/mbgnktc2/Desktop/workingL.mess')
    num_lines = sum(1 for line in open(MESS))    
    print "Number of lines:"+ str(num_lines)
    print "- File opened:  " + str(MESS)
    
    f=open(MESS,'r')
    
    for line in f:
        if line.startswith('   Dynamic Crack - '):
            words=line.split()
            crack_list.append(words[3])
    PRINT_OUT.append(str(crack_list)  +',')  
    
    f.seek(0)    
    
    for i in range(num_lines):
        first_line = f.readline()
        words=first_line.split()
        if first_line.startswith('   Dynamic Crack'): # crack name
            crack_list.append(words[3])
            PRINT_OUT.append( words[3] +',')   
        if first_line.startswith('   P_FISS'): # where crack is
            PRINT_OUT.append(first_line +',')   
        if first_line.startswith('   PN_FISS'):    
            PRINT_OUT.append(first_line +',' )       
        if first_line.startswith('   A_FISS'): 
            PRINT_OUT.append(first_line +',')   
        if first_line.startswith('   AA_FISS'):
            PRINT_OUT.append(first_line +',')   
        if first_line.startswith('  NUM_PT'):# speed and angle
            x=' '.join(first_line.split())
            PRINT_OUT.append(x +',')   
        if first_line.startswith('     3'): 
            x=' '.join(first_line.split())
            PRINT_OUT.append(x.replace('D', 'e') +',')   
        if first_line.startswith(' NUME_FOND'): # G,K etc
            x=' '.join(first_line.split())
            PRINT_OUT.append(x +',')   
        if first_line.startswith('            1'): 
            x=' '.join(first_line.split())
            PRINT_OUT.append(x.replace('E', 'e')  +',')   
        if first_line.startswith('   Propagation 22'): #Propagation summary
            for _ in range(50):
                PRINT_OUT.append(str(f.next())+",")   

	fff = open(STUDY, 'w')
	for line in PRINT_OUT:
		fff.write(line+"\n")
	fff.close()	
    return	    
      
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------	
# Converts Paravis output to MP4 and GIF
def choose():
	os.system('cls' if os.name == 'nt' else 'clear')	
	print("------------------------------------------------------------------------------")
	print(colour.BOLD +"***                               OPTION SELECTION                         ***"+ colour.END)
	print("------------------------------------------------------------------------------")
	print("")
	print(" [1] to repeat a Salome script over multiple RMED files;")
	print("")
	print(" [2] to repeat a Salome script over many time-steps in a large RMED file;")
	print("")
	print(" [3] to plot results from a RESU via node name; ")	
	print("")
	print(" [4] to run a full Code_Aster Case run (post processes and emails you the result); ")
	print("")
	print(" [5] to concatinate large numbers of CSV's from PARAVIS data dump; ")	
	print("")
	print(" [6] RUN A FULL MULTI_CRACKING-CASE; ")	
	print("")
	print(" [7] Monitor Aster Memory; ")	
	print("")
	print(" [7] Strip mess file (will need editing); ")	
	print("")
	print(colour.BOLD +" Each option will output into a dated result directory on your desktop!"+ colour.END)
	print("")
	n=raw_input(colour.GREEN+ " Select an option: "+ colour.END)

	if n == "1":
		os.makedirs(WORKING)# Make CASE Working Directory
		print("Selected mulitple files processing - Option " + n)
		try:
			post_multi_files()
		except:
			pass
	elif n=="2":
		os.makedirs(WORKING)# Make CASE Working Directory
		print("Selected mulitple time-step processing - Option " + n)	
		try:			
			post_same_file_different_time_steps()
		except:
			pass
	elif n=="3":
		os.makedirs(WORKING)# Make CASE Working Directory
		print("Selected plotter - Option " + n)	
		try:
			#print CURRENT_CASE	
			plotter()
		except:
			pass
	elif n=="4":
		os.makedirs(WORKING)# Make CASE Working Directory		
		print("Selected Aster Case run - Option " + n)	
		try:			
			runcase()
		except:
			pass
	elif n=="5":
		os.makedirs(WORKING)# Make CASE Working Directory		
		print("Selected Concatinating of CSV's  " + n)	
		try:			
			concatinate_csv()
		except:
			pass	
			
	elif n=="6":
		os.makedirs(WORKING)# Make CASE Working Directory		
		print("Selected Aster Case run - Option " + n)	
		try:			
			runcase_multi_cracks()
			#post_different_time_steps_MUTLI()
			#gif_maker()
			#produce_graphs_data()
		except:
			pass						
	elif n=="7":
		os.makedirs(WORKING)# Make CASE Working Directory		
		print("Selected Aster Case run - Option " + n)	
		try:			
			mem()
		except:
			pass	
	elif n=="8":
		os.makedirs(WORKING)# Make CASE Working Directory		
		print("Selected Aster Case run - Option " + n)	
		try:			
			pp_mess_multi()
		except:
			pass				
				
	else:
		pass	
	return	

# Error checking
while attempts > 0:
	try:
		title()
		choose()
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

#!/usr/bin/env python
import csv, sys, os, numpy,subprocess, smtplib, time, shutil, datetime, re
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

os.system('cls' if os.name == 'nt' else 'clear') # clears screen
print("------------------------------------------------------------------------------")
print(colour.BOLD +"***                           Multi_crack resu post processing                         ***"+ colour.END)
print("------------------------------------------------------------------------------")
print(" ")	
print("Re-orders data in resu and plots speed angles etc.")
print(" ")	
root = Tk()
root.withdraw()
print('Choose your .resu file:')
#resu = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your RESU file', filetypes=[('Aster_RESU', '.resu'),('Concatinated (csv)', '.csv')]) 
resu =os.path.join(os.path.expanduser('~'), '/home/mbgnktc2/Desktop/textresultstest.resu')
print('Choose your .mess file:')
#mess = tkFileDialog.askopenfilename(parent=root,initialdir=DESKTOP,title='Select your MESS file', filetypes=[('Aster_RESU', '.mess'),('Concatinated (csv)', '.csv')]) 
mess =os.path.join(os.path.expanduser('~'), '/home/mbgnktc2/Desktop/messagestest.mess')

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

plt.show()


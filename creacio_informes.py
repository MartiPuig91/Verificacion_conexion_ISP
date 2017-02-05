#!/usr/bin/env python

#RASPBERRY
#Crea un historic amb els resultats del test de velocitat

import os
import time

data = (time.strftime("%d_%m_%y"))
hora = (time.strftime("%H:%M:%S"))
os.chdir ('Informes')


archi=open('informe.txt','a') #Creem el document si no esta creat
archi.close()

os.system('curl ipinfo.io/ip > ip.txt')

archi=open('ip.txt', 'r') #Llegim el document on guardem la IP del ISP
isp=archi.readline()
print (isp)

archi=open('resultat.txt','r') #Llegim el document
down=archi.readline()
up=archi.readline()
print (down)
print(up)


archi=open('informe.txt', 'a')       #Grabem els resultats obtinguts en el document
archi.write(data+' '+hora+'\n')
archi.write(' '+'\n')
archi.write(isp+'\n')
archi.write(down+'\n')
archi.write(up+'\n')
archi.write(' '+'\n')
archi.write(' '+'\n')
archi.close()

if down <= 20:
    archi=open('report.txt','a')
    archi.write(data+' '+hora+'\n')
    archi.write(' '+'\n')
    archi.write(down+'\n')
    archi.write(' '+'\n')
    archi.close()

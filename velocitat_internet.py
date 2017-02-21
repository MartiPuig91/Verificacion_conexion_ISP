#!/usr/bin/env python
#RASPBERRY


#Conocer nuestra IP y la velocidad de internet
import socket
import os
import time



data = (time.strftime("%d_%m_%y"))
hora = (time.strftime("%H:%M:%S"))

ruta = os.path.dirname(os.path.abspath(__file__))


def Folder():
	if not os.path.exists(ruta+'/Informes'):
	    os.makedirs(ruta+'/Informes')

def IsInternet():

	testConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		testConn.connect(('10.227.19.1', 23))


		testConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			testConn.connect(('74.125.206.94', 80))
			testConn.close()

				
			os.chdir(ruta+"/Informes")
			os.system("speedtest >> resultat.txt")

			os.system("sed '8d' resultat.txt >> resultat2.txt")
			os.system("sed '1,6d' resultat2.txt >> resultat3.txt")
			os.system("rm resultat.txt")
			os.system("rm resultat2.txt")
			os.system("mv resultat3.txt resultat.txt")
				
			os.system("python "+ruta+"/creacio_informes.py")
					

			os.system("rm resultat.txt")

		except:
			testConn.close()
							
			os.chdir(ruta+"/Informes")
			archi=open('informe.txt', 'a')       #Grabem els resultats obtinguts en el document
			archi.write(data+' '+hora+'\n')
			archi.write(' '+'\n')
			archi.write('No se ha podido realizar la prueba debido a que no hay conexion con el exterior\n')
			archi.write(' '+'\n')
			archi.close()
			testConn.close()

	except:
		
		#os.chdir("Informes")
		archi=open(ruta+'/Informes/informe.txt', 'a')       #Grabem els resultats obtinguts en el document
		archi.write(data+' '+hora+'\n')
		archi.write(' '+'\n')
		archi.write('No se ha podido realizar la prueba debido a que el router esta apagado\n')
		archi.write(' '+'\n')
		archi.close()
		testConn.close()





Folder()
IsInternet()

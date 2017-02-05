# Verificacion_conexion_ISP
Con este script monitorizamos la conexión que nos está dando en todo momento nuestro ISP. Los resultados se guardan en un informe. En el caso de que no se puedan obtener los datos, se reporta el motivo por el cual no se han podido recoger los datos correctamente.


#Dependencias#

Para poder ejecutar este script solo hace falta ejecutar:

./velocitat_internet.py

Para poder ejecutar este script hay que tener instalado el programa speed-test. Lo podremos instalar con los siguientes comandos:
sudo apt-get install python-pip -y
sudo apt-get install speedtest-cli -y


Este script está desarrollado para Raspberry, ya que es un equipo que puede estar las 24h del día encendida. Pero puede ejecutarse en cualquier equipo con Linux y que satisfaga las dependencias, y se apliquen las adaptaciones en el script

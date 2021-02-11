# Se define la interfaz entre el webserver y la aplicación Python

# Se lee el entorno virtual de python
activate_this = '/home/lizbetharguello/Documentos/Redes/Chatbot/proyectoFinal/env/bin/activate_this.py'
with open(activate_this) as file:
        exec(file.read(), dict(__file__=activate_this))

import sys
import logging

# Se especifica a donde se van a escribir los errores
logging.basicConfig(stream=sys.stderr)

# Se agrega la carpeta del proyecto donde se encuentra la liga simbólica para importar la aplicación
sys.path.insert(0,"/var/www/html/proyectoFinal/")

from app import app as application

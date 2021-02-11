 
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.ext.dispatcher import run_async
from telegram import Update
import requests
import json
import logging
import re
import datetime

cache = {} 
lastCall = datetime.datetime.now() 
timeout = 20 
HTTPTimeout = 60 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update, context):
	update.message.reply_text('Bienvenido!')
	update.message.reply_text('¡Escribe /cpu para consultar el uso actual del CPU!')
	update.message.reply_text('¡Escribe /mem para consultar el uso actual de la memoria!')
	update.message.reply_text('¡Escribe /vel para consultar la velocidad de conexion')

def dameCPU(update: Update, context: CallbackContext) -> None:
    url = "http://127.0.0.1:5000/cpu"
    global lastCall
    global cache
    global timeout
    global HTTPTimeout
    if (datetime.datetime.now() - lastCall) > datetime.timedelta(seconds=timeout) or cache == {}:
        try:
            r = requests.get(url, timeout=HTTPTimeout) 
            r.raise_for_status()               
            cache = r.json()                   
            dato = json.dumps(cache, indent=4) 
            lastCall = datetime.datetime.now() 
            update.message.reply_text(dato)  
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            update.message.reply_text("El servidor ha tardado demasiado en responder.")  
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            update.message.reply_text("El servidor ha tenido un error de HTTP.")
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            update.message.reply_text("La conexión al servidor ha fallado.")     
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            update.message.reply_text("Inténtalo más tarde.")
    else:
        dato = json.dumps(cache, indent=4)
        update.message.reply_text(dato)


def dameVel(update: Update, context: CallbackContext) -> None:
    url = "http://127.0.0.1:5000/velocidad"
    global lastCall
    global cache
    global timeout
    global HTTPTimeout
    if (datetime.datetime.now() - lastCall) > datetime.timedelta(seconds=timeout) or cache == {}:
        try:
            r = requests.get(url, timeout=HTTPTimeout) 
            r.raise_for_status()               
            cache = r.json()                   
            dato = json.dumps(cache, indent=4) 
            lastCall = datetime.datetime.now() 
            update.message.reply_text(dato)  
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            update.message.reply_text("El servidor ha tardado demasiado en responder.")  
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            update.message.reply_text("El servidor ha tenido un error de HTTP.")
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            update.message.reply_text("La conexión al servidor ha fallado.")     
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            update.message.reply_text("Inténtalo más tarde.")
    else:
        dato = json.dumps(cache, indent=4)
        update.message.reply_text(dato)

def dameMem(update: Update, context: CallbackContext) -> None:
    url = "http://127.0.0.1:5000/memoria"
    global lastCall
    global cache
    global timeout
    global HTTPTimeout
    if (datetime.datetime.now() - lastCall) > datetime.timedelta(seconds=timeout) or cache == {}:
        try:
            r = requests.get(url, timeout=HTTPTimeout) 
            r.raise_for_status()               
            cache = r.json()                   
            dato = json.dumps(cache, indent=4) 
            lastCall = datetime.datetime.now() 
            update.message.reply_text(dato)  
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            update.message.reply_text("El servidor ha tardado demasiado en responder.")  
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            update.message.reply_text("El servidor ha tenido un error de HTTP.")
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            update.message.reply_text("La conexión al servidor ha fallado.")     
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            update.message.reply_text("Inténtalo más tarde.")
    else:
        dato = json.dumps(cache, indent=4)
        update.message.reply_text(dato)      

def main():
    updater = Updater('1586202212:AAFzqhTyqlbkGCgxHCXXdl1oyGplNG-8Gk4', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('cpu', dameCPU))
    dp.add_handler(CommandHandler('vel', dameVel))
    dp.add_handler(CommandHandler('mem', dameMem))
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
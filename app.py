#1. Primeiro vamos importar a bibliotecas

import pywhatkit as py 
import pywhatkit
import keyboard
import time
from datetime import datetime
import win32clipboard
#2. Definir para quais contatos iremos enviar as msgs
contatos = ['+5511numero', '+5511segundo numero']

image = "C:/Users/Aluno/Pictures/pao2.jpg"


# 3. vamos por um intervalo de envio de msgs

while len(contatos) >=1:
    #enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'Sei lá!', datetime.now().hour, datetime.now().minute + 1)
    pywhatkit.sendwhats_image(contatos[0], image, 'A IMAGEM FOI PORRA')
    del contatos[0]
    time.sleep(10)
    keyboard.press_and_release('crtl + w')

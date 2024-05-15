""" import pywhatkit
numero=input("ingresa el numero telefonico")
pywhatkit.sendwhatmsg(numero, "hola ", 10, 15) 
#envio de mensaje automatico whathsapp 
"""

import pywhatkit

# Lista de números de teléfono a los que deseas enviar mensajes
numeros_input = input("ingrese numeros de telefono separaos por coma y con el codigo del pais")
numeros_telefono = numeros_input.split(",") # se encarga de dar los espacios 

# Mensaje que deseas enviar
mensaje = input("ingrese ingrese el mensaje a enviar")

# Hora y minuto en que deseas enviar el mensaje (en formato de 24 horas)
hora = int(input("ingrese la hora"))
minuto = int(input("ingrese minutos"))

# Iterar sobre la lista de números de teléfono y enviar el mensaje a cada uno
for numero in numeros_telefono:
    pywhatkit.sendwhatmsg(numero, mensaje, hora, minuto)



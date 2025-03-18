import random
import time

opciones = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 
password = ""
lon = int(input("Cuantos caracteres va a tener su contraseña?"))
time.sleep(0.5)
print("Calculando tu contraseña...")
for i in range(lon):
    password += random.choice(opciones) 
time.sleep(2)
print("Tu contraseña es:", password)

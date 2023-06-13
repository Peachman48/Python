import os
import time


def hola(nombre, apellido):
    os.system("cls")
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")
    time.sleep(3)
    os.system("pause")


hola("Christian", "Lomeli")
os.system("cls")

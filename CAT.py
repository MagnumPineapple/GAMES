import time
import os
import turtle
import keyboard
import sys
import math
import pygame
import random

hambre = 0
sed = 0
aburrimiento = 0
higiene = 0
sueno = 0

nivel = 0
rango = 0

vida = 100

estado = "Bueno"

experiencia = 0
experienciaUp = 1000


menuStack = []


os.system('cls')



def menu():
    os.system('cls')
    print("\033[0;36m \033[4m" + " MOLTEN STUDIOS " + "\033[0m")
    print("\033[31m" + "      CAT       " + "\033[0m")
    print(" by MagnumPineapple ")

    print(" @ 2023, All rights Reserved")
    print(" ")
    print("1. Nueva Partida \n""2. Cargar Partida \n""3. Opciones \n""4. Créditos \n""5. Salir")

    print(" ")


# def menu():
os.system('cls')
print("\033[1;36m \033[4m" + " MOLTEN STUDIOS " + "\033[0m")
print("\033[1;31m" + "      CAT       " + "\033[0m")

print(" by MagnumPineapple ")

print(" @ 2023, All rights Reserved")
print(" ")
print("1. Nueva Partida \n""2. Cargar Partida \n""3. Opciones \n""4. Créditos \n""5. Salir")

print(" ")

def on_keypress(event):
    if event.name == "backspace" or event.name == "enter":
        keyboard.unhook_all()

while True:
    # menu()
    # keyboard.on_press(on_keypress)
    # on_keypress()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        os.system('cls')
        print("\033[31m" + " Nueva Partida " + "\033[0m")
        print("1. Nuevo CAT")
        print("6. Atrás")
        choice = input("Ingrese opción: ")
        
        if choice == "1" or choice == 1:
            os.system('cls')
            nombre = input("Introduce un nombre a tu CAT: \n")
            
            os.system('cls')
            print("\033[31m" + " Nueva Partida " + "\033[0m")
            owner = input("Introduce tu nombre (Dueño): \n")
    
            os.system('cls')
            print("\033[31m" + " Cargando... " + "\033[0m")
            time.sleep(1)
            break
        
        if choice == "6" or choice == 6:
            menu()
        
            
    
    
    elif (opcion == 2 or opcion == "2"):
        os.system('cls')
        print("\033[31m" + " Selecciona Partida: " + "\033[0m\n" " PRÓXIMAMENTE ")
        print("6. Atrás")
    
    elif (opcion == 3 or opcion == "3"):
        os.system('cls')
        print("\033[31m" + " Opciones " + "\033[0m\n" " PRÓXIMAMENTE ")
        print("6. Atrás")
    
    elif (opcion == 4 or opcion == "4"):
        os.system('cls')
        print("\033[31m" + " Créditos " + "\033[0m\n" " Creador: MagnumPineapple ")
        print("6. Atrás")
        
    elif(opcion == 5 or opcion == "5"):
        os.system('cls')
        sys.exit()
    
    elif(opcion == 6 or opcion == "6" ):
        menu()
    else:
        menu()
    
    
        
        
    
        
         
def levelUp():
    global experiencia, aburrimiento, experienciaUp
    
    if keyboard.is_pressed('e'):
        experiencia += 84
        
    if aburrimiento == 0:
        if keyboard.is_pressed('e'):
            experiencia -= 84
    else:
        
        pass

        

  
def estado_vida():
    global estado
    global vida
    global estado
    
    
    if(vida > 50):
        estado = "Bueno"
    
    elif (vida > 25 & vida <= 50):
        estado = "Precaución"
    elif (vida <= 25):
        estado = "Peligro"


def aumentar_hambre():
    global hambre
    global vida
    hambre += 3
    if (hambre >= 500):
        hambre = 500
        vida -= 1
        print(nombre, " necesita comer!")
        
def aumentar_sed():
    global sed
    global vida
    sed += 2
    if (sed >= 500):
        sed = 500
        vida -= 1
        print(nombre, " necesita beber!")
        
def aumentar_aburrimiento():
    global aburrimiento
    global vida
    aburrimiento += 7
    if (aburrimiento >= 500):
        aburrimiento = 500
        vida -= 1
        print(nombre, " necesita  entretenerse!")
        
def aumentar_higiene():
    global higiene
    global vida
    higiene += 4
    if (higiene  >= 500):
        higiene = 500
        vida -= 1
        print(nombre, " necesita un baño!")

def aumentar_sueno():
    global sueno
    global vida
    sueno += 6
    if (sueno >= 500):
        sueno = 500
        vida -= 1
        print(nombre, " necesita dormir!") 
        
        
        
# bajando = False        
   
        
def reducir_hambre():
    global hambre
    global vida
    if keyboard.is_pressed('q'):
        hambre -= 80
        print('Comiendo...')
    if (hambre <= 0):
            hambre = 0

def reducir_sed():
    global sed
    global vida
    if keyboard.is_pressed('w'):
        sed -= 80
        print('Bebiendo...')
        if (sed <= 0):
            sed = 0

def reducir_aburrimiento():
    global aburrimiento
    global vida
    global experiencia
    global experienciaUp
    if keyboard.is_pressed('e'):
        aburrimiento -= 80
        # experiencia += 16
        print('Jugando...')
        if (aburrimiento <= 0):
            experiencia += 0
            aburrimiento = 0

def reducir_higiene():
    global higiene
    global vida
    if keyboard.is_pressed('r'):
        higiene -= 80
        print('Bañando...')
        if (higiene <= 0):
            higiene = 0
            
            
def reducir_sueno():
    global sueno
    global vida
    if keyboard.is_pressed('t'):
        sueno-= 80
        print('Durmiendo...')
        if (sueno <= 0):
            sueno = 0 
            

while True:
    
    os.system('cls')
    
    aumentar_hambre()
    aumentar_sed()
    aumentar_aburrimiento()
    aumentar_higiene()
    aumentar_sueno()
    
    reducir_hambre()
    reducir_sed()
    reducir_aburrimiento()
    reducir_higiene()
    reducir_sueno()
    
    estado_vida()
    
    levelUp()
    
   # on_keypress()
    
    print(" /\_/\ ")
    print("( o.o )")
    print(" > ^ < ")
    
    print(" ")
    
    font = f"Vida: {vida}"
    
    
    print(nombre, end = '   ||   ')
    print("Dueño: ", owner)
     
    print(" ")
    
    print("Rango: ", rango, end = '   ||   ')
    print("Nivel: ", nivel, end = '   ||   ')
    print("EXP: ", experiencia," / ", experienciaUp)
    
    print(" ")

    print(font, " / ", 100, end = '   ||   ')
    
  #  print(" ")
    
    print("Estado de Salud: ", estado)
    
    print(" ")
    
    print("Hambre: ", hambre, " / ", 500, end = '   ||   ')
    print("Sed: ", sed, " / ", 500, end = '   ||   ')
    print("Aburrimiento: ", aburrimiento, " / ", 500, end = '   ||   ')
    print("Higiene: ", higiene, " / ", 500, end = '   ||   ')
    print("Sueño: ", sueno, " / ", 500)
    

    time.sleep(1)
    
    

    os.system('cls')
    
    aumentar_hambre()
    aumentar_sed()
    aumentar_aburrimiento()
    aumentar_higiene()
    aumentar_sueno()
    
    reducir_hambre()
    reducir_sed()
    reducir_aburrimiento()
    reducir_higiene()
    reducir_sueno()
    
    estado_vida()
    
    levelUp()
    
  #  on_keypress()
    
    
    print(" /\_/\ ")
    print("( -.- )")
    print(" > ^ < ")
    
    print(" ")
    
    font = f"Vida: {vida}"
    
   
    
    print(nombre, end = '   ||   ')
    print("Dueño: ", owner)
    
    print(" ")
    
    print("Rango: ", rango, end = '   ||   ')
    print("Nivel: ", nivel, end = '   ||   ')
    print("EXP: ", experiencia," / ", experienciaUp)
    
    print(" ")

    print(font, " / ", 100, end = '   ||   ')
    
    
   # print(" ")
    
    print("Estado de Salud: ", estado)
    
    print(" ")
    
    print("Hambre: ", hambre, " / ", 500, end = '   ||   ')
    print("Sed: ", sed, " / ", 500, end = '   ||   ')
    print("Aburrimiento: ", aburrimiento, " / ", 500, end = '   ||   ')
    print("Higiene: ", higiene, " / ", 500, end = '   ||   ')
    print("Sueño: ", sueno, " / ", 500)

    
 
    if vida == 0:
        os.system('cls')
        print(" /\_/\ ")
        print("( X X )")
        print(" > ^ < ")
        print(nombre, " ha muerto... ")
        break
        time.sleep(5)
        menu()
        
    

    time.sleep(1)

import time
import os
import turtle
import keyboard
import sys
import math
import pygame
import random

number = random.randint(1, 100)
guesses = 0

os.system('cls')

def menu():
    print(" GUESS THE NUMBER ")
    print(" by MagnumPineapple ")
    
    print(" ")
    
    print("1. Modo 1:   1 -> 10 ")
    print("2. Modo 2:   1 -> 100 ")
    print("3. Modo 3:   1 -> 1000 ")
    
    print("")
    
    print("4. Salir ")
    
    print(" ")
    
while True:
    os.system('cls')
    menu()
    try:
        choice = int(input("Selecciona una opción: "))
        if choice == 1:
            number = random.randint(1, 10)
            # print(number)
            break
        elif choice == 2:
            number = random.randint(1, 100)
            # print(number)
            break
        elif choice == 3:
            number = random.randint(1, 1000)
            # print(number)
            break
        elif choice == 4:
            sys.exit()
        elif (choice != 1 
              or choice != 2 
              or choice != 3 
              or choice != 4):
            print("")
            # break
    except ValueError:
            print("")
    
   
    
    
os.system('cls')

while True:
    # print(number)
    guess = int(input("Adivina el número: "))
    guesses += 1
    if guess < number:
        print("Número menor.")
    elif guess > number:
        print("Número mayor.")
    elif guess == number:
        os.system('cls')
        print(f"Has adivinado el número en {guesses} intentos.")
        print("Número adivinado: ", number)
        break
from msvcrt import getche
from msvcrt import putch
import os
import random
import time
"""
Programa para el menu del seg parcial
"""
def menu():
    x=' '
    while True:   
        os.system('cls')
        print("Metodos de ordenamiento")
        print("1. Tablas")
        print("2. numeros primos ")
        print("3. factorial de un numero ")
        print("4. adivinanza")
        print("5. mas ")
        # relaciono el resto
       
        print("0. Salir")
        print("Favor digite una opción")
        x=ord(getche())
        if (x == 27 or x== 48):
            print ("Gracias por todo")
            print ("By jheremy peinado")
            break
        elif x == 49:
            tablas()
        elif x == 50:
            funcion2()
        elif x == 51:
            funcion3()
        elif x == 52:
            adivinanza()
        pass 
            #Continuo con los otros

def tablas():
    for i in range(1,11,1):
        for j in range(1,11,1):
            print(i," x ", j, "=",i*j)
    getche()
    
    
def funcion2():
    print(" los primos")
    num= 1
    while num<=1000:
     contador=1
     x=0
     while contador<=num:
        if num%contador==0:
            x=x+1
        contador= contador +1
     if x==2:
        print(num)
     num = num + 1
    
    getche()
    
    
def funcion3():
    import math
    factorial=1
    print("Dame un numero:")
    x=eval (input())
    for i in range (1,x+1):
        factorial=factorial*i
        
        print(factorial)
        break 
                 
    getche()
    
        
def adivinanza(): 
    import os , random 
    ad=random.randint (1,10)
    print(59*"#")
    print(" Adivina el numero entre el 1 al 10 ,tienes tres intentos ")
    print(59*"#")

    while True:
        nu= int(input("Ingrese un numero entre 1 y 10 : "))
        if nu==ad:
            print("Felicidades has adivinado el numero ")
            break
        
    print("Hasta pronto ")
            

    getche()
            


    print("BY jheremy peinado ")
            
    getche()
    # asgkjsa
    #asdñgkljsd

    
menu()        # hago las funciones restantes

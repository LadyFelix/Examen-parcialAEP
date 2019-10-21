#hacer que el sistema genere un 
#numero aleatorio entre 1 y 10. Luego 
# hacer que el usuario adivine el numero. La
#aplicacion debe terminar cuando el usuario adivine.

import random,os
os.system("cls")

a = random.randint(1,10)
while True:
    b = int(input("Adivine el numero de 1 a 10:"))
    if a == b:
        print("Adivinaste")
        break
   
    else:
        print("Numero incorrecto")
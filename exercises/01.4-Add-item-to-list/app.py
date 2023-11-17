#Remember import random function here:
import random

my_list = [4,5,734,43,45]
def funcion():
    
    
    for x in range(10):
        numero_random = random.randint(1, 100)
        my_list.append(numero_random)
        
    return my_list

print(funcion())
#The magic is here:

#Import random
import random
#Create the function below:

def matrixBuilder (entero):
   
    matriz=[]
    
    for y in range(entero):
        fila=[]
        
        for x in range(entero):
            fila.append(1)
            matriz.append(fila)
    return matriz    


  
side = random.randint(2,10) 
#matrixBuilder(3)
print(matrixBuilder(1))




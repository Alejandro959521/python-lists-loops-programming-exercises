

# Your code go above, nothing to change after this line:


def lyrics_generator (array):
    count=0
    letra=""
    for valor in array:
        if valor == 1:
            valor = "Drop the base " 
            letra+=valor
            count+=1
            if count == 3:
                valor = "!!!Break the base!!! "
                letra+=valor
                count == 0     
        elif valor == 0:
            valor= "Boom "
            letra+=valor
    return letra    
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))        
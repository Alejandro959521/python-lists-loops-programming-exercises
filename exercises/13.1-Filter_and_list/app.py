
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def function (names):
    return names[0].upper()=="R" 

resulting_names=list(filter(function,all_names))
print(resulting_names)





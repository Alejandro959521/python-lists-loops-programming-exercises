theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def lista (list):
    if list == 1:
        list="wiki"
    else: list="woko"  
    return list
result=list(map(lista,theBools))
print(result)




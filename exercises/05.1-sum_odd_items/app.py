arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odds(array):
    total = 0
    for valor in array:
        if valor % 2 != 0:
            total+=valor
    return total            
print(sum_odds(arr))            

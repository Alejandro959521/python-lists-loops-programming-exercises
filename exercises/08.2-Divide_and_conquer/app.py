list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list (numbers):
    even=[]
    odd=[]
    unido=[]

    for numb in list_of_numbers:
        if numb %2 == 0:
            even.append(numb)
        else: odd.append(numb)
    unido.append(odd)        
    unido.append(even)
    return unido





print(merge_two_list(list_of_numbers))


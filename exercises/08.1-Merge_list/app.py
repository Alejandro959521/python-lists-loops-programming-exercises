chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    list=[]
    for names in list1:
        list.append(names)
    for names2 in list2:
        list.append(names2)
    return list            

print(merge_list(chunk_one, chunk_two))

people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    new_list=[]
    for names in people:
         if names != person_name:
            new_list.append(names)
    return new_list

    #Your code go here:
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))
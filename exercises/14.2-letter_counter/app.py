par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:

for letra in par:
    
    letra2=letra.lower()
    if letra2 == " ": continue
    elif letra2 in counts:       
        counts[letra2]+=1
    elif letra2 is not None: 
        counts[letra2]=1
       
       # print(counts[letra2])
    # elif counts[letra2]==None:
    #     counts[letra2]=1
    # else: counts[letra2]+1    


print(counts)


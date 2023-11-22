parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:

def get_parking_lot(matriz):
    state={
      "total_slots": 0,
      "available_slots": 0,
      "occupied_slots": 0
    }        
    for fila in matriz:  
        for valor in fila:
          if valor == 0: continue
          elif valor == 1:
              state["occupied_slots"]+=1
              state["total_slots"]+=1
          elif valor== 2:
              state["available_slots"]+=1
              state["total_slots"]+=1
    return state      
          
  

print(get_parking_lot(parking_state))



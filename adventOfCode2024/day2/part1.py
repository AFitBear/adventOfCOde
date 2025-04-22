import numpy as np

print("start")
with open("data.txt", "r") as file:
    DATA =  file.read().strip().splitlines()
rapports=list(map(str.split, DATA))

#print(rapports[0])
#print(rapports[0][3])

SafeRapports=0

def checkRapportSafe(rapport):
    global SafeRapports
    higher=False #mangler bedre variabel navn
    if rapport[0]<rapport[1]:#checker om den bliver stigende eller faldene
        higher=True 
    
    #print(rapport)


    for i in range(len(rapport)-1):
        if abs(int(rapport[i])-int(rapport[i+1])) not in (1, 2):
            return
        if (int(rapport[i])<int(rapport[i+1]))!=higher:
            return
        
    SafeRapports+=1

for rapport in rapports:
    checkRapportSafe(rapport)
    #print(rapport)

#print(len(rapports))
print(SafeRapports)
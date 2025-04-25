print("start")
with open("data/day2.txt", "r") as file:
    DATA =  file.read().strip().splitlines()
#rapports=list(map(str.split, DATA))
rapports = [list(map(int, line.split())) for line in DATA]

SafeRapports=0

def pDamper(rapport, i, recur):
    if recur:
        return False
    newrapport1=rapport.copy()
    newrapport2=rapport.copy()
    newrapport33=rapport.copy()
    newrapport1.pop(i)
    newrapport2.pop(i+1)
    if i!=0:
        newrapport33.pop(i-1)
        if checkRapportSafe(newrapport33,True):
            return True

    if checkRapportSafe(newrapport1,True) or checkRapportSafe(newrapport2, True):
        return True
    return False

def checkRapportSafe(rapport,recur):
    higher=False #mangler bedre variabel navn
    if rapport[0]<rapport[1]:#checker om den bliver stigende eller faldene
        higher=True 

    for i in range(len(rapport)-1):
        if abs(rapport[i]-rapport[i+1]) not in (1, 2, 3):#checker om springet er stiger korrekt.
            return pDamper(rapport,i,recur)
        
        if (rapport[i]<rapport[i+1])!=higher:#checker om den er stigende
            return pDamper(rapport,i,recur)
    
    return True

print("Raw safe")
for rapport in rapports:
    if checkRapportSafe(rapport,True):
        SafeRapports+=1
print(SafeRapports)

SafeRapports=0
print("safe with Problem dampener")
for rapport in rapports:
    if checkRapportSafe(rapport,False):
        SafeRapports+=1
print(SafeRapports)



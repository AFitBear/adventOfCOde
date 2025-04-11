import numpy as np

print("start")
with open("data.txt", "r") as file:
    DATA =  file.read().strip().splitlines()
pairlist=list(map(str.split, DATA))

distance1=[]
distance2=[]

for line in pairlist:
    distance1.append(line[0])
    distance2.append(line[1])
distance1.sort()
distance2.sort()
print(distance1[1])
print(distance1[6])
print(distance1[88])
print(len(distance1))

cum=0
for i in range(len(distance1)):
    cum+=abs(int(distance1[i])-int(distance2[i]))
print(cum)

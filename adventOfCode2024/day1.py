import numpy as np

print("start")
with open("day1.txt", "r") as file:
    DATA =  file.read().strip().splitlines()
pairlist=list(map(str.split, DATA))

distance1=[]
distance2=[]

for line in pairlist:
    distance1.append(line[0])
    distance2.append(line[1])
distance1.sort()
distance2.sort()

similar_score=0

for left in distance1:
    same=0
    for right in distance2:
        if int(left)==int(right):
            same+=1
    similar_score+=same*int(left)

cum=0
for i in range(len(distance1)):
    cum+=abs(int(distance1[i])-int(distance2[i]))

print(f"similar_score: {similar_score}")
print(f"cum: {cum}")

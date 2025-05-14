print("start")
with open("data/day3.txt", "r") as file:
    DATA =  file.read()

def find_data(sentence):
    for i in range(len(sentence)):
        if sentence[i]==")":
            sentence=sentence[:i]
            return sentence
    return

def mul(functions:str):
    if functions==None: 
        return 0
    functions=functions.split(",")
    if len(functions)==2:
        if functions[0].isdigit() and functions[1].isdigit():
            return (int(functions[0])*int(functions[1]))
    
        
        

data_split=DATA.split("mul(")
functions=[]
for sentence in data_split:
    functions.append(find_data(sentence))

functions = [item for item in functions if item is not None]

cum=0

for i in range(len(functions)):
    print(functions[i])
    cum+=mul(functions[i])
print(cum)
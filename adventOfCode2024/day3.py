print("start")

with open("data/day3.txt", "r") as file:
    DATA =  file.read()

data_split=DATA.split("mul")
for sentence in data_split:
    for i in range(len(sentence)):
        if sentence[i]==")":
            sentence=sentence[i:]
            sentence+="mudrgrgrdgl" + sentence
            break
for i in range(len(data_split)):
    print(data_split[i])
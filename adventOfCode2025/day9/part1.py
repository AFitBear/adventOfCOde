
def calcArea(pos1,pos2):
    temp=((pos1[0]-pos2[0])+1)*((pos1[1]-pos2[1])+1)
    return temp

def main():
    print("start")
    coordinates=[]
    temp_number=0
    highest_number=0
    #highest_number
    with open("input.txt") as f:
        for line in f:#kan sikkert gøres bedre. but it works
            x, y = line.strip().split(',')
            coordinates.append((int(x), int(y)))
        print(coordinates)
        print(coordinates[1])
        print(coordinates[1][1])
        for i in coordinates:
            for j in coordinates:
                temp_number=calcArea(i,j)
                if (temp_number>highest_number):
                    highest_number=temp_number


        print(highest_number)
        f.close

if (__name__=="__main__"):
    main()

def main():
    print("start")
    values=[]
    lines=[]
    patterns=[]
    with open("input.txt") as f:
        values = (f.readlines())
        lines=[line.strip() for line in values]
        #print(lines)
        i=0
        while i <len(lines):
            if (len(lines[i]) > 1 and lines[i][1] == ":"):
                idx=int(lines[i][:-1]) #remove colon
                grid=[]
                print("hello")
                for j in range (i+1,i+4):
                    if j < len(lines) and lines[j]:
                        grid.append(lines[j])
            patterns[idx]=grid
            i+=4
        i+=1



if (__name__=="__main__"):
    main()
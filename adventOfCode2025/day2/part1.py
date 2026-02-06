import math

def main(gg):
    print("start")
    x=23+gg
    cumm=0
    myset=set()
    with open("input.txt") as f:
        values = (f.readline().strip().split(','))
        values = [tuple(map(int, a.split("-"))) for a in values]
        #print(values)
        for ting in values:
            print("1",ting[0],"3",ting[1])
            for i in range(ting[0],ting[1],1):
                text=str(i)
                digits=len(text)
                half=digits//2
                #digits = len(str(abs(i)))
                if (digits%2!=0):
                    continue
                if (text[:half]==text[half:]):
                    print(i)
                    cumm+=i

        print("this is cumm:",cumm)
        #f.read
        f.close
        return 3












if __name__=="__main__":
    main(1)
    


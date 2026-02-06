def main():
    pos_x=0
    pos_y=0
    degrees=0
    distance=0
    cocio=set()
    cocio.add((pos_x,pos_y))

    with open("input.txt") as file:
        instructions =file.read().split(", ")
        for instcruct in instructions:
            if (instcruct[0]=="R"):
                degrees+=1
            elif (instcruct[0]=="L"):
                degrees-=1
            degrees%=4
            distance=int(instcruct[1:])
            for _ in range(distance):
              match degrees:
                  case 0:
                      pos_y+=1
                  case 1:
                      pos_x+=1
                  case 2:
                      pos_y-=1
                  case 3:
                      pos_x-=1
              if ((pos_x,pos_y) in cocio):
                  #print(f"{pos_x},{pos_y}")
                  #print(f"{abs(pos_x)+abs(pos_y)}")
                  break
              cocio.add((pos_x,pos_y))
            

        print(f"{pos_x},{pos_y}")
        print(f"{abs(pos_x)+abs(pos_y)}")
        return 23451

if (__name__=="__main__"):
    main()
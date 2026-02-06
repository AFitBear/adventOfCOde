#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    static int position=50;
    static int cumm;
    static char rightOrLeft;
    char line[10];
    FILE *fptr;

    char buff[10];

    printf("start day 1\n");

    fptr = fopen("input.txt", "r");
    while (fgets(line, sizeof(line), fptr)) {
    //seperates the values
    rightOrLeft=line[0];
    int value = atoi(&line[1]);
    //printf("%i\n",value);
    if (rightOrLeft=='L'){
        position-=value;
    }else {
    position+=value;
    }
    position%=100;
    printf("%i\n",position);
    if (position==0) {
        cumm++;
    }

    //printf("value: %i, rightOrLeft: %c",value,rightOrLeft);

    }

    printf("it is %i",cumm);
    return cumm;
}

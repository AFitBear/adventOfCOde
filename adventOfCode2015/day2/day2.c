#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const void *a, const void *b) { //function pointer used for qsort
    return (*(int *)a - *(int *)b);
}

int main(void){
    printf("start of day2\n");

    int cumm = 0;

    FILE *fptr;
    char ch;
    fptr = fopen("input.txt", "r");

    char line[20]; //line buffer
    int lenghts[3]; //place to store numbers
    int count=0;

    while (fgets(line, sizeof(line), fptr) != NULL) {

    line[strcspn(line, "\n")] = 0; //reset the line
    
    char *token = strtok(line, "x"); //makes a array of "tokes", each token is where the line is seperated by x
        count = 0;
        while (token != NULL && count < 3) {
            lenghts[count++] = atoi(token); //converts string to int
            token = strtok(NULL, "x");
        }
    int n = sizeof(lenghts) / sizeof(lenghts[0]);

    int l=lenghts[0];
    int w=lenghts[1];
    int h=lenghts[2];

    qsort(lenghts, n, sizeof(lenghts[0]), comp);

    cumm+=(2*l*w + 2*w*h + 2*h*l)+lenghts[0]*lenghts[1];

    }

    printf("%i",cumm);


   // qsort(void *base, size_t nmemb, size_t size, __compar_fn_t compar)
}
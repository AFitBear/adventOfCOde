#include <stdio.h>
#include <stdlib.h>

int main(void){
    printf("%s","hello!");
    int lenght=10;
    int arr[lenght];
    size_t gems = sizeof(arr);
    int* ptr = malloc(sizeof(int)*lenght);
    free(ptr);
    printf("better");




    char test[]="))(()()))))((())";
    int cumm=0;
    for (int i = 0; i < sizeof(test)/sizeof(char); i++)
    {
        //printf("%c",test[i]);
        switch (test[i])
        {
        case ')':
            printf("%c",')');
            cumm++;
            break;
        case '(':
            printf("%c",'(');
            cumm--;
            break;
        
        default:
            printf("not included ");
            break;
        }
    }
    
    printf("cumm: %d\n", cumm);
    printf("done!!\n");

}

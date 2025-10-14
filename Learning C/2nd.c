/*2nd*/
#include <stdio.h>
double GetArea(double radi){
    double pi = 3.1415926;
    return (pi*radi*radi);
}
double GetDiamiter(double radi){
    return radi*2.0;
}
double GetCurcumfrence(double radi){
    double pi = 3.1415926;
    return (2*pi*radi);
}

int opg2(void){
    double radius;
    printf("input radius: ");
    scanf("%lf",&radius);

    printf("Area: %lf\n", GetArea(radius));
    printf("CirCumFrance: %lf\n", GetCurcumfrence(radius));
    printf("Diameter: %lf\n",GetDiamiter(radius));
    return 2;
}


int main(void)
{
    printf("hello\n");
    opg2();
    return (420);
}

int opg1(void)
{
    char something;
    short shortValue;
    printf("write a char: ");
    something = getchar();
    printf("write an short value: ");
    scanf("%hi",&shortValue);

    printf("you typed: %c",something);
    printf("but also typed: %hi", shortValue);
    return 1;
}
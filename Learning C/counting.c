#include <stdio.h>

void runner(int arr_A[], int n, int k, int arr_B[]){
    int arr_C[k + 1];

    for (int i = 0; i <= k; i++)
        arr_C[i] = 0;

    for (int j = 0; j < n; j++)
        arr_C[arr_A[j]]++;

    for (int i = 1; i <= k; i++)
        arr_C[i] += arr_C[i - 1];

    for (int j = n - 1; j >= 0; j--) {
        arr_B[arr_C[arr_A[j]] - 1] = arr_A[j];
        arr_C[arr_A[j]]--;
    }
}

int findMax(int arr_A[], int n){
    int highest = arr_A[0];
    for (int i = 1; i < n; i++){
        if (arr_A[i] > highest)
            highest = arr_A[i];
    }
    return highest;
}

int main(){
    int arr_A[] = {1,34,65,6,4,3,6,23,2,34,6,7,3,5,4,3,5,3,5,76,4,2,4,56,32,54,6,3,4,6,345,334,346,416,32,345,420};
    int n = sizeof(arr_A) / sizeof(arr_A[0]);
    int r = findMax(arr_A, n);

    int arr_B[n];
    runner(arr_A, n, r, arr_B);

    for (int i = 0; i < n; i++)
        printf("%d\n", arr_B[i]);

    return 0;
}
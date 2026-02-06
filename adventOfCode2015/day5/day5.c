#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int containsVowels(char *sentence) {
    int cummVowel = 0;

    for (int i = 0; i < strlen(sentence); i++) {
        // printf("%s", sentence);
        if (strchr("aeiou",
                   sentence[i])) // checks if the char is in the string "aeiou"
            cummVowel++;
    }

    if (cummVowel >= 3) {
        printf("%s", sentence);
        return 1;
    } else
        return 0;
}

int containsBanned(char *sentence) {
    char *patterns[] = {"ab", "dc", "pq", "xy"};
    for (int i = 0; i < (sizeof(patterns) / sizeof(patterns[0])); i++) {
        if (strstr(sentence, patterns[i])) {
            return 1;
        }
    }
    return 0;
}

int containRepeat(char *sentence) {
    int isIt = 0;
    for (int i = 0; i + 1 < strlen(sentence); i++) {
        if (sentence[i] == sentence[i + 1]) {
            isIt = 1;
        }
    }
    return isIt;
}

int main() {
    printf("day: 5");

    int cumm;
    char str[20];

    FILE *fptr;
    fptr = fopen("input", "r");

    while (fgets(str, sizeof(str), fptr) != NULL) {
        if (containsVowels(str) && containRepeat(str) && !containsBanned(str)) {
            cumm++;
        }
    }

    printf("done: %i\n", cumm);
    fclose(fptr); // close file
    return 1;
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    FILE *infile, *outfile;
    char id[50];
    double latitude, longitude;
    time_t t;
    struct tm *tm_info;
    char time_str[20];
    int ID_counter=0;

    // Open input file for reading
    infile = fopen("some_cordinates.txt", "r");
    if (infile == NULL) {
        perror("Error opening input file");
        return 1;
    }

    // Open output file for writing
    outfile = fopen("output.csv", "w");
    if (outfile == NULL) {
        perror("Error opening output file");
        fclose(infile);
        return 1;
    }

    // Process each line
    while (fscanf(infile, "%lf %lf", &latitude, &longitude) == 2) {
        // Get current time
        t = time(NULL);
        tm_info = localtime(&t);
        strftime(time_str, sizeof(time_str), "%Y-%m-%d %H:%M:%S", tm_info);

        // Write formatted line to output file
        fprintf(outfile, "%i, %.6f, %.6f, 4, %s\n",ID_counter, latitude, longitude, time_str);
        ID_counter++;
    }

    fclose(infile);
    fclose(outfile);

    printf("File has been processed and saved as output.csv\n");

    return 0;
}


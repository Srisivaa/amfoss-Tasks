#include <stdio.h>
#include <stdlib.h>

void print_diamond(FILE *outfile, int n) {
    for (int i = 0; i < n; i++) {
        fprintf(outfile, "%*s%s\n", n - i - 1, "", "*");
        for (int j = 0; j < 2 * i - 1; j++) {
            fprintf(outfile, "*");
        }
        fprintf(outfile, "\n");
    }
    for (int i = n - 2; i >= 0; i--) {
        fprintf(outfile, "%*s%s\n", n - i - 1, "", "*");
        for (int j = 0; j < 2 * i - 1; j++) {
            fprintf(outfile, "*");
        }
        fprintf(outfile, "\n");
    }
}

int main() {
    FILE *infile = fopen("input.txt", "r");
    FILE *outfile = fopen("output.txt", "w");
    
    if (infile == NULL || outfile == NULL) {
        perror("Error opening file");
        return 1;
    }

    int n;
    fscanf(infile, "%d", &n);
    print_diamond(outfile, n);

    fclose(infile);
    fclose(outfile);

    return 0;
}



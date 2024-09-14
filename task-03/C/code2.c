#include <stdio.h>

int main() {
    char buffer[1024];
    FILE *input = fopen("input.txt", "r");
    FILE *output = fopen("output.txt", "w");
    
    if (input == NULL || output == NULL) {
        perror("Error opening file");
        return 1;
    }

    while (fgets(buffer, sizeof(buffer), input) != NULL) {
        fputs(buffer, output);
    }

    fclose(input);
    fclose(output);

    return 0;
}

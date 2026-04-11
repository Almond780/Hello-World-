//C Hello world child process

#include <stdio.h>
#include <string.h>

char Vinput[] = "Invalid input";
char line[] = "-------------------------";

int main() {
    char input[10];
    while (1) {
        printf("%s\n", line);
        printf("Hello World! \n");
        printf("%s\n", line);
        printf("Q - Quit\n> ");

        scanf("%s", input);
        if (strcmp(input, "Q") == 0) {
          break;
        } else {
            printf("%s\n", Vinput);
        }
    }
    return 0;
}
#include <stdio.h>
#include <string.h>
char *gets(char *); /* legacy function omitted from modern C headers */
int main(void) {
    char input[100], name[8];
    printf("Enter a short name: ");
    gets(input);                 /* unsafe: no input length limit */
    strcpy(name, input);         /* unsafe: name holds only 7 chars + '\0' */
    printf("Name: %s\n", name);
    return 0;
}

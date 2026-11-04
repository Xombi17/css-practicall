#include <stdio.h>
#include <string.h>
int main(void) {
    char message[16] = "Hello ";
    char name[32];
    int choice;
    printf("Enter a short name: ");
    fgets(name, sizeof name, stdin);
    name[strcspn(name, "\n")] = '\0';
    printf("1 = strcat, 2 = sprintf: ");
    scanf("%d", &choice);
    if (choice == 1) {
        strcat(message, name);             /* may exceed message[16] */
        puts(message);
    } else if (choice == 2) {
        sprintf(message, "Hello %s", name); /* no destination size limit */
        puts(message);
    }
    return 0;
}

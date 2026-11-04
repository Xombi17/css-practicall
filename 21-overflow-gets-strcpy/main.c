
#include <stdio.h>
#include <string.h>

struct Data {
    char buffer[8];     // comes first in memory
    int authorized;     // sits right after buffer
};

int main() {
    struct Data d;
    d.authorized = 0;

    char input[100];
    printf("Enter your name: ");
    gets(input);                 // unsafe: no length limit

    strcpy(d.buffer, input);     // unsafe: copies everything, no size check

    printf("Hello, %s\n", d.buffer);

    if (d.authorized != 0) {
        printf(">>> authorized was overwritten! Access granted (overflow worked)\n");
    } else {
        printf("Access denied (authorized still 0)\n");
    }
    return 0;
}

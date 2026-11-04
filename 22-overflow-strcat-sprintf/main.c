#include <stdio.h>
#include <string.h>

struct Data {
    char small[8];     // comes first in memory
    int flag;          // sits right after small
};

int main() {
    struct Data d;
    d.flag = 0;

    strcpy(d.small, "AB");          // short start

    strcat(d.small, "CDEFGHIJ");    // strcat keeps adding, no size check -> overflow

    sprintf(d.small, "%s", "LONGTEXT123");  // sprintf writes past the end too

    printf("small = %s\n", d.small);

    if (d.flag != 0) {
        printf(">>> flag was overwritten by the overflow!\n");
    } else {
        printf("flag still 0\n");
    }
    return 0;
}

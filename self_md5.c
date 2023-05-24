#include <stdio.h>
#include <string.h>

#define P "1111111111111111"
#define Q "2222222222222222"
#define PP P P P P P P P P
#define QQ Q Q Q Q Q Q Q Q
#define BIT PP QQ
#define DIGIT BIT BIT BIT BIT
#define DIGIT_4 DIGIT DIGIT DIGIT DIGIT
#define DIGIT_16 DIGIT_4 DIGIT_4 DIGIT_4 DIGIT_4
#define PLACEHOLDER DIGIT_16 DIGIT_16

char* padding = "PADDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDING";
char* data = PLACEHOLDER;
char* table = "0123456789ABCDEF";

int main() {
    printf("The md5sum of this program is: ");
    for (int i = 0; i < 32; i++) {
        int n = 0;
        if (memcmp(data, data + 128, 128) == 0) n += 1;
        data += 256;
        if (memcmp(data, data + 128, 128) == 0) n += 2;
        data += 256;
        if (memcmp(data, data + 128, 128) == 0) n += 4;
        data += 256;
        if (memcmp(data, data + 128, 128) == 0) n += 8;
        data += 256;
        printf("%c", table[n]);
    }
    printf("\n");
    return 0;
}
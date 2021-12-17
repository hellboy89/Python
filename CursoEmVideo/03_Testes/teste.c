#include <stdio.h>
#include <stdlib.h>

int main()
{
    double num, media;

    num = 1;

    printf("Digite as idades: \n");

    while (num >= 0) {
        scanf("%2lf", &num);
    }

    return 0;
}

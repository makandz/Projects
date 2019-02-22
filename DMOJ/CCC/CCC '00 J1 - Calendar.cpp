#include <stdio.h>

int main() {
    int s, a;
    scanf("%d %d", &s, &a);
    printf("Sun Mon Tue Wed Thr Fri Sat\n");

    for (int i = 1; i < s; i++)
        printf("    ");

    for (int i = 1; i <= a; i++) {
        if (i >= 10) printf(" %d", i);
        else printf("  %d", i);

        if ((s + i - 1) % 7 == 0 || i == a)
            printf("\n");
        else printf(" ");
    }

    return 0;
}
#include <stdio.h>

int main() {
    int n;
    int sum = 0;
    scanf("%d", &n);

    for(int i = 0; i < n; i++)
    {
        int x;
        scanf("%d", &x);
        sum = sum + x;
    }
    printf("%d\n", sum);
    return 0;
}
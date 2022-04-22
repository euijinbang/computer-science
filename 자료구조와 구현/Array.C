#include <stdio.h>

int main(int argc, char * argv[])
{   
    // 배열의 크기 : U, S, 그리고 배열이 끝났을 때의 한 자리 = 총 3자리
    char country[3] = "US";  
    printf("%c%c\n", country[0], country[1]);
    printf("%s\n", country);

    // 1차원 배열 : 선언과 동시에 초기화
    int a[5] = {1, 2, 3, 4, 5};
    int b[] = {1, 2, 3, 4, 5};

    printf("%d\n", a[3]);
    printf("%d\n", b[2]);

    // 2차원 배열 : 선언과 동시에 초기화
    int numArr[3][3] = {
      {1, 2, 3},
      {4, 5, 6},
      {7, 8, 9}
    };
    printf("%d\n", numArr[0][1]);
    printf("%d\n", numArr[0][2]);
    printf("%d\n", numArr[0][3]);

    // 배열 0으로 초기화
    int c[10] = { 0, };
    printf("%d\n", c[0]);
    printf("%d\n", c[5]);
    printf("%d\n", c[9]);

    return 0;
}
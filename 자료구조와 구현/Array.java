import java.util.Arrays;

class Array {
  public static void main(String[] args) {
    // 길이가 0인 배열
    int[] arr = new int[0];

    // 선언과 생성을 동시에
    int[] iArr1 = new int[10];
    int[] iArr2 = new int[10];
    int[] iArr3 = {100, 95, 80, 70, 60};
    char[] chArr = {'a', 'b', 'c', 'd'};

    for (int i = 0; i < iArr1.length; i++) {
      iArr1[i] = i + 1;
    }

    for (int i = 0; i < iArr2.length; i++) {
      iArr2[i] = (int) (Math.random() * 10) + 1;
    }

    for (int i = 0; i < iArr1.length; i++) {
      System.out.print(iArr1[i] + ",");
    }

    System.out.println(iArr1);  // [I@15db9742 | 참조변수이므로 '타입@배열의 주소' 가 출력된다.
    System.out.println(iArr2);  // [I@6d06d69c
    System.out.println(Arrays.toString(iArr2)); // [2, 5, 10, 9, 4, 9, 4, 2, 1, 8]
    System.out.println(Arrays.toString(iArr3)); // [100, 95, 80, 70, 60]
    System.out.println(Arrays.toString(chArr)); // [a, b, c, d]
    System.out.println(chArr);  // abcd | 예외적으로 char 배열은 구분자 없이 출력된다.

  }
}
/*
Pattern is:
1
2 1
3 2 1
4 3 2 1
*/
public class patternD2 {
    public static void main(String[] args) {
        int n = 4;
        for (int j = 1; j <= n; j++) {
            for (int i = j; i >= 1; i--) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
}

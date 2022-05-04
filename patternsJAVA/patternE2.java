/*
Pattern is: 
D
D C
D C B
D C B A
*/
public class patternE2 {
    public static void main(String[] args) {
        int n = 4;
        StringBuilder sb = new StringBuilder("ABCD");

        for (int i = n - 1; i >= 0; i--) {
            for (int j = sb.length() - 1; j >= 0; j--) {
                if (j >= i) {
                    System.out.print(sb.charAt(j) + " ");
                }
            }
            System.out.println();
        }
    }
}

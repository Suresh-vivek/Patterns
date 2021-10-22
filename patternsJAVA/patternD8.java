/*
Pattern is:
A
B A
C B A
D C B A
*/
public class patternD8 {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("ABCD");
        int n = 4;
        for (int i = 0; i <n; i++) {
            for (int j = i; j >=0; j--) {
                System.out.print(sb.charAt(j)+" ");
            }
            System.out.println();
        }
    }
}

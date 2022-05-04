/*
Pattern is: 
D C B A
C B A
B A
A
*/
public class patternE4 {
    public static void main(String[] args) {
        int n=4;
        StringBuilder sb= new StringBuilder("ABCD");

        for (int i = n-1; i >= 0; i--) {
            for (int j = sb.length()-1; j >= 0; j--) {
                if (j<=i) {
                    System.out.print(sb.charAt(j)+" ");
                }
            }
            System.out.println();
        }
    }
}

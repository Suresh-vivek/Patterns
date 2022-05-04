/*
Pattern is :
A B C D
B C D
C D
D
*/
public class patternE1{
    public static void main(String[] args) {
        int n=4;
        StringBuilder sb= new StringBuilder("ABCD");

        for (int i = 0; i < n; i++) {
            for (int j = i; j < sb.length(); j++) {
                System.out.print(sb.charAt(j)+" ");
            }
            System.out.println();
        }
    }
}
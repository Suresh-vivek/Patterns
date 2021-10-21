/*
Pattern is:
A B C D
A B C
A B 
A
*/
public class patternD9 {
    public static void main(String[] args) {
        StringBuilder sb= new StringBuilder("ABCD");
        int n=4;
        for (int i = 0; i <n; i++) {
            for (int j = i; j <n; j++) {
                System.out.print(sb.charAt(j)+" ");
            }
            System.out.println();
        }
    }
}

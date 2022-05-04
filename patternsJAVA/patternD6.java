/*
Pattern is:
4 3 2 1
4 3 2
4 3 
4
*/
public class patternD6 {
    public static void main(String[] args) {
        int n=4;
        for (int i = 1; i <= n; i++) {
            for (int j = n; j >=i; j--) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}

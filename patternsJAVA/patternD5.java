/*
Pattern is:
4 
4 3
4 3 2
4 3 2 1
*/
public class patternD5 {
    public static void main(String[] args) {
        int n=4;
        for (int i = n; i >=1; i--) {
            for (int j = n; j >=i; j--) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}

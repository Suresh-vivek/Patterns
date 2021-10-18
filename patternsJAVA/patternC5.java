/*
Pattern is: 
4 3 2 1
4 3 2 1
4 3 2 1
4 3 2 1
*/
public class patternC5 {
    public static void main(String[] args) {
        int n=4;
        for (int i =1; i <=n; i++) {
            for (int j = n; j >=1; j--) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}

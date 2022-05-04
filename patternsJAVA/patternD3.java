/*
Patten is:
1 2 3 4
1 2 3 
1 2 
1
*/
public class patternD3 {
    public static void main(String[] args) {
        int n=4;
        for (int i = n; i >= 1; i--) {
            //space
            for (int j = 1; j <=i ; j++) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}

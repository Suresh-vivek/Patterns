/*
Pattern is :
4 3 2 1
3 2 1
2 1
1
*/
public class patternD7 {
    public static void main(String[] args) {
        int n=4;
        for (int i = n; i >=1; i--) {
            for (int j = i; j >=1; j--) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}

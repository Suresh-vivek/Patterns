/*
Pattern is:
1 2 3 4
2 3 4
3 4
4
*/
public class patternD4 {
    public static void main(String[] args) {
        int n=4;
        for (int i = 1; i <=n; i++) {
            for (int j = i; j <=n; j++) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}

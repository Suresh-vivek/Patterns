/*
Pattern is :
D C B A
D C B
D C
D
*/
public class patternE3 {
    public static void main(String[] args) {
        int n=4;
        StringBuilder sb= new StringBuilder("ABCD");

        for (int i = 0; i < n; i++) {
            for (int j = sb.length()-1; j >= 0; j--) {
                if(i<=j){
                    System.out.print(sb.charAt(j)+" ");
                }
            }
            System.out.println();
        }
    }
}

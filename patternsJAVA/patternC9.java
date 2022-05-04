/*
Pattern is :
A 
A B
A B C
A B C D
*/
public class patternC9 {
    public static void main(String[] args) {
        int n=4;
        StringBuilder s= new StringBuilder("ABCD");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < s.length(); j++) {
                if(i>=j){
                    System.out.print(s.charAt(j)+" ");
                }
            }
            System.out.println();
        }
    }
}

/*
Pattern is: 
A B C D
A B C D
A B C D
A B C D
*/
public class patternC4 {
    public static void main(String[] args) {
        int n = 4;
        StringBuilder s = new StringBuilder("A B C D");
        for (int i = 0; i < n; i++) {
            System.out.print(s);
            System.out.println();
        }
    }
}

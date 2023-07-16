package inflearn;

import java.util.Scanner;

public class I0104 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        StringBuffer reveString = new StringBuffer();
        
        for(int i = 0; i < N; i++) {
            String input = sc.next();

            StringBuffer sb = new StringBuffer(input);
            reveString.append(sb.reverse().toString());
            reveString.append("\n");
            
        }
        System.out.println(reveString);
    }
}


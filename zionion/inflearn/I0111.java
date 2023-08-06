package inflearn;

import java.util.Scanner;

public class I0111 {

    public static String solution(String input) {
        String result = "";
        input = input + " ";
        int cnt = 0;

        for(int i = 0; i < input.length()-1; i++) {
            if(input.charAt(i) == input.charAt(i+1)) cnt++;
            else {
                result += input.charAt(i);
                if(cnt > 1) {
                    result += String.valueOf(cnt);
                    cnt = 1;
                }
            }
        }

        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        
        System.out.println(solution(input));

        sc.close();
    }
}  


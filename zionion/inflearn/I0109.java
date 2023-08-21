package inflearn;

import java.util.Scanner;

public class I0109 {

    public static String solution(String input) {
        String result = "";
        input = input.replaceAll("[^0-9]", "");

        for(int i = 0; i < input.length(); i++) {
            if(input.charAt(i) == '0') {
                continue;
            } else {
                result = input.substring(i);
                break;
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


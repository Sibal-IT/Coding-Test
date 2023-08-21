package inflearn;

import java.util.Scanner;

public class I0107 {

    public static String solution(String input) {
        //String answer = "";
        String str = input.toLowerCase();

        for(int i = 0; i < str.length()/2; i++) {
            if(!(str.charAt(i) == str.charAt((str.length()-1)-i))) {
                return "NO";
            }
        }
        return "YES";
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        System.out.println(solution(input));
    }
}


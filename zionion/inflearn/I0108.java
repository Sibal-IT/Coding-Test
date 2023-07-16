package inflearn;

import java.util.Scanner;

public class I0108 {

    public static Boolean solution(String input) {
        for(int i = 0; i < input.length()/2; i++) {
            if(input.charAt(i) != input.charAt(input.length()-1-i)) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        
        input = input.replaceAll(" ","");
        input = input.replaceAll("[^a-zA-Z]", "");
        input = input.toLowerCase();

        if(solution(input)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}


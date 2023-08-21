package inflearn;

import java.util.Scanner;

public class I0106 {

    public static String solution(String input) {
        String answer = "";

        for(int i = 0; i < input.length(); i++) {
            //System.out.println(input.charAt(i) + " " + i + " " + input.indexOf(input.charAt(i)));

            if(input.indexOf(input.charAt(i)) == i) {
                answer += input.charAt(i);
            }
            //indexOf : 해당 문자열이 가장 처음 발견될 때의 인덱스를 반환
        }
        return answer;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        System.out.println(solution(input));
    }
}


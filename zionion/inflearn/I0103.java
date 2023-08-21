package inflearn;

import java.util.Scanner;

public class I0103 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int maxLen = Integer.MIN_VALUE;
        String result = new String();

        String[] arr = input.split(" ");
        for(String str : arr) { 
            //System.out.println("temp : " + str);
            int strLen = str.length();
            if(strLen > maxLen) {
                result = str;
                maxLen = strLen;
            }
        }
        System.out.println(result);
    }
}


package inflearn;

import java.util.Scanner;

public class I0102 {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        String str = in.nextLine();
        
        System.out.println(caseChange(str));
        return ;
    }

    static String caseChange(String s1) {
        char[] arr = s1.toCharArray();

        for(int i = 0; i < arr.length; i++) {
            char c = arr[i];
            if(Character.isUpperCase(c)) {
                arr[i] = Character.toLowerCase(c);
            } else {
                arr[i] = Character.toUpperCase(c);
            }
        }
        
        return new String(arr);
    }
}

package inflearn;

import java.util.Scanner;
 
public class I0101 {
  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    String input1 = in.nextLine().toLowerCase();
    String input2 = in.nextLine().toLowerCase();
    
    int answer = countLetter(input1, input2);

    //System.out.println(answer);
  }

  static int countLetter(String input1, String input2) {
    int cnt = 0;

    char[] arr = input1.toCharArray();
    char c = input2.charAt(0);
    for(char e : arr) {
      if(e == c) {
        cnt++;
      }
    }
    
    return cnt;
  }
}
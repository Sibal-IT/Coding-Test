package inflearn;

import java.util.Scanner;

/*
* title : 가위 바위 보
* */
public class I0203 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[] a = new int[N];
        int[] b = new int[N];
        for(int i = 0; i < N; i++) {
            a[i] = in.nextInt();
        }
        for(int i = 0; i < N; i++) {
            b[i] = in.nextInt();
        }

        for(int i = 0; i < N; i++) {
            System.out.println(returnWinner(a[i], b[i]));
        }
        in.close(); 
        return ;
    }

    /*
    * 1:가위, 2:바위, 3:보
    * */
    static String returnWinner(int a, int b) {
        String winner = "";

        if(a == b) winner = "D";
        else if(a == 1 && b == 3) winner = "A";
        else if(a == 2 && b == 1) winner = "A";
        else if(a == 3 && b == 2) winner = "A";
        else winner = "B";

        return winner;
    }
}

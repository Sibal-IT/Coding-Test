package inflearn;

import java.util.Scanner;

/*
* title : 피보나치 수열
* */
public class I0204 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[] a = new int[N];

        for(int i = 1; i < N; i++) {
            if(i == 1) {
                a[0] = 1;
                a[1] = 1;
                continue;
            }
            a[i] = a[i-1] + a[i-2];
        }

        for(int i = 0;i < N; i++) {
            System.out.print(a[i] + " ");
        }
        in.close(); 
    }

}

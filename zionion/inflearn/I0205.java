package inflearn;

import java.util.Scanner;

/*
* title : 소수(에라토스테네스 체)
* 에라토스테네스 체 - 소수가 되는 수의 배수를 지우면 남은 건 소수가 되는 알고리즘
* 제한시간 1초
* */
public class I0205 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        boolean[] isPrime = new boolean[N+1];
        isPrime = checkedPrimeNum(isPrime, N);

        int prime = 0;
        for(int i = 1; i <= N; i++) {
            if (isPrime[i]) {
                //System.out.print(i+" ");
                prime++;
            }
        }
        System.out.println(prime);
        in.close();
    }
    static boolean[] checkedPrimeNum(boolean[] arr, int N) {
        // 소수 true, 소수아니면 false
        for(int i = 0; i < arr.length; i++) {
            arr[i] = true;
        }
        arr[0] = arr[1] = false;

        for(int i = 2; i <= N; i++) {
            if(arr[i]) {
                for(int j = i*i; j <= N; j += i) {
                    arr[j] = false;
                }
            }
        }
        return arr;
    }
}

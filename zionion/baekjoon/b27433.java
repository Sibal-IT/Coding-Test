package baekjoon;

import java.io.*;

public class b27433 {

    /* 팩토리얼2 */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine()); // 0~20까지의 정수

        br.close();
        System.out.println(factorial(N));

    }

    // 20까지므로 int아니고 long
    static long factorial(int N) {
        if(N <= 0) {
            return 1;
        }

        return N * factorial(N-1);
    }
}
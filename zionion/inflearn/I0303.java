package inflearn;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/*
* title : 최대매출
* 슬라이딩 윈도우 풀이
* 모든 출력을 구하게 되면 N x K -> 너무 큼!
*
* */
public class I0303 {
    public int solution(int N, int K, int[] arr) {
        int sum = 0;
        for (int i = 0; i < K; i++) {
            sum += arr[i];
        }
        int answer = sum;

        for (int i = K; i < N; i++) {
            sum += (arr[i] - arr[i - K]);
            if(sum > answer)answer = sum;
        }
        return answer;
    }

    public static void main(String[] args) {
        I0303 T = new I0303();
        Scanner kb = new Scanner(System.in);
        int N = kb.nextInt();
        int K = kb.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i < N; i++){
            arr[i] = kb.nextInt();
        }

        int answer = T.solution(N, K, arr);
        System.out.println(answer);
    }
}

package inflearn;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/*
* title : 공통원소 구하기
* */
public class I0302 {
    public ArrayList<Integer> solution(int n, int m, int[] a, int[] b) {
        ArrayList<Integer> answer = new ArrayList<>();
        Arrays.sort(a);
        Arrays.sort(b);

        int p1 = 0, p2 = 0;
        while(p1 < n && p2 < m) {
            if (a[p1] == b[p2]) {
                answer.add(a[p1++]);
                p2++;
            }
            else if  (a[p1] < b[p2]) {
                p1++;
            }
            else {
                p2++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        I0302 T = new I0302();
        Scanner kb = new Scanner(System.in);
        int N = kb.nextInt();
        int[] a = new int[N];
        for(int i = 0; i < N; i++){
            a[i] = kb.nextInt();
        }
        int M = kb.nextInt();
        int[] b = new int[M];
        for(int i = 0; i < M; i++){
            b[i] = kb.nextInt();
        }
        for(int x : T.solution(N, M, a, b)) System.out.print(x + " ");

    }
}

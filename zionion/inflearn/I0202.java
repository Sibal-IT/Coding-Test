package inflearn;

import java.util.*;
/*
* title : 보이는 학생
* */
public class I0202 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
        }

        int cnt = 1;
        int max = arr[0];
        for(int i = 1; i < N; i++) {
            int height = arr[i];
            if(max < height) {
                cnt++;
                max = height;
            }
        }
        System.out.println(cnt);
        
        in.close(); 
        return ;
    }
}

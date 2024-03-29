package complete;

import java.util.*;
import java.io.*;

public class boj10804 {
    /**
     * b2 카드역배치
     * 완전탐색으로 진행했는데, 효율적인 풀이로는 뭐가 있을까?
     * */
    public static void main(String[] args) throws IOException{

        int[] arr = new int[20];
        for(int i=0; i<20; ++i){
            arr[i]=(i+1);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i=0; i<10; ++i){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int[] arr2 = new int[b-a+1];
            int idx = 0;
            for(int j=a-1; j<b; ++j){
                arr2[idx] = arr[j];
                ++idx;
            }
            int idx2 = a-1;
            for(int j=b-a; j>=0; --j){
                arr[idx2] = arr2[j];
                ++idx2;
            }
        }

        for(int i=0; i<20; ++i){
            System.out.print(arr[i]+" ");
        }

        br.close();
    }
}

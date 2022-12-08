package complete;

import java.util.*;
import java.io.*;

public class boj14659 {
    /**
     * b1 한조서열정리하고옴ㅋㅋ
     * 1. 완탐 가능?? -> 가능.
     * 다른 방법은 받으면서 그 즉시 비교하면서 cnt를 초기화하는 방법도 있는것 같음.
     * * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if(n==1){
            System.out.println(0);
        }else{
            int[] arr = new int[n];
            int max = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i=0; i<n; ++i){
                arr[i] = Integer.parseInt(st.nextToken());
            }

            for(int i=0; i<n-1; ++i){
                int cnt = 0;
                for(int j=i+1; j<n; ++j){
                    if(arr[i]>arr[j]){
                        ++cnt;
                    }else{//중복없으므로
                        break;
                    }
                }
                if(max<cnt){
                    max=cnt;
                }
            }
            System.out.println(max);
        }


        br.close();
    }
}

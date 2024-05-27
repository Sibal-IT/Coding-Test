package complete;

import java.util.*;
import java.io.*;

public class boj11047 {
    /**
     * s4 돟전 0
     * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        int sum = 0;
        int cnt = 0;
        for(int i=0; i<n; ++i){
            arr[i]=Integer.parseInt(br.readLine());
        }
        for(int i=n-1; i>=0; --i){
            cnt+=(k/arr[i]);
            if((k/arr[i])>0){
                k=(k%arr[i]);
            }
            if(k==0){
                break;
            }
        }
        System.out.println(cnt);
        br.close();
    }
}

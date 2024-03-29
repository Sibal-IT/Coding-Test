package complete;

import java.util.*;
import java.io.*;

public class boj10093 {
    /**
     * b2 숫자
     * Long
     * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long n = Long.parseLong(st.nextToken());
        long m = Long.parseLong(st.nextToken());
        if(n<m){
            System.out.println(m-n-1);
            for(long i=n+1; i<m; ++i){
                System.out.print(i+" ");
            }
        }else if(n>m){
            System.out.println(n-m-1);
            for(long i=m+1; i<n; ++i){
                System.out.print(i+" ");
            }
        }else{
            //n==m
            System.out.println(0);
        }

        br.close();
    }
}

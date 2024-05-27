package complete;

import java.util.*;
import java.io.*;
import java.math.*;

public class boj18110 {
    /**
     * s4 solved.ac
     * 항상 메인 메소드 안에서 풀었으니까, 이제 메소드를 만들어서 풀어보는 걸루.
     * Math.round() 자바 반올림
     * */
    public static int solve(int[] arr2){
        int index = (int) Math.round(arr2.length * 0.15);
        float sum = 0;
        for(int i=index; i<arr2.length-index; ++i){
            sum += arr2[i];
        }
        return Math.round(sum/(arr2.length - (2*index)));
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        if(tc == 0){
            System.out.println(0);
        }else{
            int[] arr = new int[tc];
            for(int i=0; i<tc; ++i){
                arr[i] = Integer.parseInt(br.readLine());
            }
            Arrays.sort(arr);
            System.out.println(solve(arr));
        }

        br.close();
    }
}

package inflearn;

import java.nio.Buffer;
import java.util.*;
import java.io.*;

/*
* title : 두 배열 합치기
* */
public class I0301 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        StringTokenizer  st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int M = Integer.parseInt(br.readLine());
        int[] arr2 = new int[M];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < M; i++){
            arr2[i] = Integer.parseInt(st.nextToken());
        }

        int[] arr3 = new int[N+M];
        System.arraycopy(arr, 0, arr3, 0, N);
        System.arraycopy(arr2, 0, arr3, N, M);

        //System.out.println(Arrays.toString(arr3));
        Arrays.sort(arr3);
        for(int i = 0; i < arr3.length; i++){
            System.out.print(arr3[i] + " ");
        }

        br.close();
        bw.flush();
        bw.close();;
    }
}

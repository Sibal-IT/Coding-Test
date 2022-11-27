package complete;

import java.util.*;
import java.io.*;

public class boj2217 {
    /**
     * s4 로프
     *
     * 최대길이를 구해야하므로, 배열에 저장하고 정렬시킨다음,
     * 최소값부터 배열의 크기만큼 곱해준 것을 최대길이로 저장한다.
     * 그 다음 배열의 인덱스를 늘리면서 배열이 같은 ㄱ여우는 제하고, 더 큰경우에서 앞으로 남은 항수를 곱해주는 식으로 tmp를 계산.
     * tmp와 최대 길이를 비교.
     * ex) 1 1 4 -> 4(>3)
     *
     * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for(int i=0; i<n; ++i){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
        int maxSum = arr[0] * n;
        if(n!=1){
            for(int i=1; i<arr.length; ++i){
                if(arr[i]==arr[i-1]){
                    continue;
                }else{
                    int tmp = arr[i]*(n-i);
                    if(maxSum < tmp){
                        maxSum = tmp;
                    }
                }
            }
        }
        System.out.println(maxSum);
        br.close();
    }
}

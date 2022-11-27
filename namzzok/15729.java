package notComplete;

import java.util.*;
import java.io.*;

public class boj15729 {
    /**
     * s2 방탈출
     * 처음 접근은 나온 결과에서 all 0을 만드려고 접근했는데, 좌->우 순서없이 버튼을 누른다면 성립이 안될까봐 그런 접근을 했었음.
     * 근데 그냥 순서없이 변형시켜보고 좌에서 우로 변형시켜봐도 cnt가 똑같은 것 같아서 그대로 구현함.
     * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean[] arr = new boolean[n+2];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; ++i){
            if(Integer.parseInt(st.nextToken())==1){
                arr[i]=true;
            }else{
                arr[i]=false;
            }
        }

        int cnt = 0;
        for(int i=0; i<n; ++i){
            if(arr[i]) {
                ++cnt;
                arr[i] = !arr[i];
                arr[i+1] = !arr[i+1];
                arr[i+2] = !arr[i+2];
            }
        }
        System.out.println(cnt);
        br.close();
    }
}

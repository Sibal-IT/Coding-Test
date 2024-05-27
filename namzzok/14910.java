package complete;

import java.util.*;
import java.io.*;

public class boj14910 {
    /**
     * b2 오르막
     * 단순히 주어진 문장을 완전탐색으로 훑으면서, 이전수보다 작은 경우만 체크.
     * st.hasMoreTokens() 메소드 암기
     * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        float num = Float.parseFloat(st.nextToken());
        String answer = "Good";
        while(st.hasMoreTokens()){
            float next = Float.parseFloat(st.nextToken());
            if(num>next){
                answer = "Bad";
                break;
            }
            num = next;
        }
        System.out.println(answer);
        br.close();

    }
}

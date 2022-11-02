package notComplete;

import java.util.*;
import java.io.*;

public class boj_repeat {
    /**
     * s5 수들의 합
     * 자연수의 합을 이용, 자연수의 합을 더해가며 커지는 순간 수 하나를 뺌으로서 동률을 만들 수 있음.
     * 200의 경우, 1부터 20까지의 합이 210이므로 -10을 해주면 200을 맞출 수 있다.
     * 20개에서 10 한개를 빼주면 19개
     *
     * 그리디보다는 완전탐색풀이?
    * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Long S = Long.parseLong(br.readLine());
        Long N = 0L;
        Long sum = 0L;
        while(true){
            ++N;
            sum+=N;
            if(sum>S){
                break;
            }
        }
        System.out.println(N-1);
        br.close();
    }
}

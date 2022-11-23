package complete;

import java.util.*;
import java.io.*;

public class boj1946 {
    /**
     * s1 신입 사원
     *
     * 정렬 comparable, comparator 부분은 구글링의 도움을 받았습니다.
     * 추후 정렬 따로 정리하면서 숙달하도록 하겟삼,,
     *
     * 모두 비교를 하는 방법으론 시간 초과날 것 같아서, 서류를 정렬해놓고 면접만 비교하는 방식으로
     * 합격자의 수를 카운팅 -> 면접을 정렬하고 서류로 카운팅해도 좋을듯?
     *
     * 운이 좋았던 문제.
     * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for(int i=0; i<tc; ++i){
            int cnt = 0;
            int n = Integer.parseInt(br.readLine());
            int[][] arr = new int[n][2];

            //초기화
            for(int j=0; j<n; ++j){
                StringTokenizer st = new StringTokenizer(br.readLine());
                arr[j][0] = Integer.parseInt(st.nextToken());
                arr[j][1] = Integer.parseInt(st.nextToken());
            }

            //정렬
            Arrays.sort(arr, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return Integer.compare(o1[0], o2[0]);
                }
            });


            //돌면서 크기 비교, 나머지 크기비교를 하면서 서류 점수가 낮을 수록, 면접 점수가 높아야하니까 가장 최근에 뽑힌 면접 점수를 기준으로 계속 비교를 진행.
            int tmp = arr[0][1];
            for(int j=1; j<n; ++j){
                if(tmp>arr[j][1]){
                    tmp = arr[j][1];
                    ++cnt;
                }
            }
            //0번째 인덱스는 1등한게 있으므로 무조건 선발되니까 +1 해줘야함.
            System.out.println(cnt+1);
        }
        br.close();
    }
}

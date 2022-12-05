import java.io.*;
import java.util.*;

/* 방탈출 -- 참조함 */
public class b15729 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N+2];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int result = 0;
        for(int i = 0; i < N; i++) {
            if(arr[i] == 1) {
                arr[i+1] = arr[i+1] == 1 ? 0 : 1;
                arr[i+2] = arr[i+2] == 1 ? 0 : 1;
                result++;
            }
        }

        System.out.println(result);
        br.close();
    }
}

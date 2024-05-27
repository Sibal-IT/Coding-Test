package complete;

import java.util.*;
import java.io.*;

public class boj11328 {
    /**
     * b2  Strfry
     * 다른 이들의 정석적인 풀이는 알파벳 배열을 만들어서 카운팅하는 것이고,
     * 내 풀이는 문자배열로 바꿔서 전부 비교해주었음. 비효율적인 풀이인듯.
     * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for(int i = 0; i<tc; ++i) {
            StringTokenizer sb = new StringTokenizer(br.readLine());
            String firstString = sb.nextToken();
            String secondString = sb.nextToken();
            String answer = "Possible";
            if (firstString.length() != secondString.length()) {
                System.out.println("Impossible");
            } else {
                char[] first = firstString.toCharArray();
                char[] second = secondString.toCharArray();
                for (int j = 0; j < secondString.length(); ++j) {
                    for (int k = 0; k < firstString.length(); ++k) {
                        if (first[k] == second[j]) {
                            first[k] = ' ';
                            second[j] = ' '; // 반례 aaa abb 일경우 aaa가 모두 a에 걸려서 공백을 저장하게 되므로, 문자열을  공백으로 바꿔줘서 회피.
                        }
                    }
                }

                for (int j = 0; j < first.length; ++j) {
                    if (first[j] != ' ') {
                        answer = "Impossible";
                        break;
                    }
                }
                System.out.println(answer);

            }
        }
        br.close();
    }
}

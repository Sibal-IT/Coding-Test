package complete;

import java.util.*;
import java.io.*;
import java.lang.*;

public class boj1919 {
    /**
     * b2 애너그램 만들기
     * */
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] first = new int[26];
        int[] second = new int[26];
        int result = 0;

        char[] one = br.readLine().toCharArray();
        char[] two = br.readLine().toCharArray();

        for (char c : one) {
            ++first[c - 'a'];
        }

        for (char c : two) {
            ++second[c - 'a'];
        }

        for(int i=0; i<first.length; ++i){
            result+=Math.abs(first[i]-second[i]);
        }

        System.out.println(result);
        br.close();
    }
}


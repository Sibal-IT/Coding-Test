package inflearn;

import java.util.Scanner;

public class I0201 {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int N = in.nextInt();
        int[] arr = new int[N];
        
        for(int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
            //System.out.print(arr[i] + " ");
        }
        
        for(int i = 0; i < N; i++) {
            if(i == 0) {
                System.out.print(arr[i] + " ");
                continue;
            }
            
            if (arr[i-1] < arr[i]) {
                System.out.print(arr[i] + " ");
            }
        }
        
        in.close();
        return ;
    }
}

package complete;

import java.util.*;
import java.io.*;

public class boj1244 {
    /**
     * s4 스위치 켜고 끄기
     * */
    public static void  main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int btnNum = Integer.parseInt(br.readLine());
        int[] switches = new int[btnNum];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<btnNum; ++i) {
            switches[i] = Integer.parseInt(st.nextToken());
        }

        int Studnum = Integer.parseInt(br.readLine());
        for(int i=0; i<Studnum; ++i){
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int sex = Integer.parseInt(st2.nextToken());
            int btnIdx = Integer.parseInt(st2.nextToken());

            if(sex==1){
                for(int j=btnIdx-1; j<switches.length; ++j){
                    if((j+1)%btnIdx==0){
                        if(switches[j]==0){
                            switches[j]=1;
                        }else{
                            switches[j]=0;
                        }
                    }
                }
            }else if(sex==2){
                if(switches[btnIdx-1]==0){
                    switches[btnIdx-1]=1;
                }else{
                    switches[btnIdx-1]=0;
                }
                if(btnIdx<=btnNum-btnIdx){
                    // 인덱스를 찾아서 한번에 전부 바꾸는 방법이 있고, 하나씩 바꾸는 방법도 있을듯.
                    // 1. 하나씩 바꾸기
                    for(int j=btnIdx-2; j>=0; --j){
                        if(switches[j]==switches[2*(btnIdx-1)-j]){
                            if(switches[j]==0){
                                switches[j]=1;
                                switches[2*(btnIdx-1)-j]=1;
                            }else{
                                switches[j]=0;
                                switches[2*(btnIdx-1)-j]=0;
                            }
                        }else{
                            break;
                        }
                    }
                }else{
                    for(int j=btnIdx; j<switches.length; ++j){ //위에서 핸들링을 하고 내려왔기 때문에, 다음열에부터 실행하면 된다. 다행히 계산식에는 문제없었음.
                        if(switches[j]==switches[2*(btnIdx-1)-j]){
                            if(switches[j]==0){
                                switches[j]=1;
                                switches[2*(btnIdx-1)-j]=1;
                            }else{
                                switches[j]=0;
                                switches[2*(btnIdx-1)-j]=0;
                            }
                        }else{
                            break;
                        }
                    }
                }
            }
        }

        for(int i=0; i<switches.length; ++i){
            System.out.print(switches[i]);
            if((i+1)%20==0){
                if((i+1)!=btnNum){ // 버튼이 20개만 주어질 경우, 개행없이 끝내야함.
                    System.out.println();
                }
            }else{
                System.out.print(" ");
            }
        }
        br.close();
    }
}

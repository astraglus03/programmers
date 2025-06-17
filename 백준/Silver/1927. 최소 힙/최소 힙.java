import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());


        Queue<Integer> pq = new PriorityQueue<>();

        StringBuilder sb = new StringBuilder();

        for(int i=0; i<n;i++){
            int num = Integer.parseInt(br.readLine());
            if(num==0){
                if(pq.isEmpty()){
                    sb.append(0).append("\n");
                }
                else{
                    sb.append(pq.poll()).append("\n");
                }
            }
            else{
                pq.add(num);
            }
        }
        br.close();
        sb.setLength(sb.length()-1);
        System.out.println(sb);
    }
}
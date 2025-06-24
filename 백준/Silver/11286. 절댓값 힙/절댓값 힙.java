import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        Queue<Integer> queue = new PriorityQueue<>((i1,i2) -> {
            return Math.abs(i1) == Math.abs(i2) ? i1 - i2 : Math.abs(i1) - Math.abs(i2);
        });
        for(int i=0; i<n; i++){
            int num = Integer.parseInt(br.readLine());
            if(num ==0){
                if(queue.isEmpty()){
                    sb.append("0\n");
                } else {;
                    sb.append(queue.poll()).append("\n");
                }
            }
            else{
                queue.offer(num);
            }
        }

        br.close();
        System.out.println(sb);
    }
}
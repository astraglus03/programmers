import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        br.close();

        Queue<Integer> queue = new LinkedList<>();
        for(int i=1; i<=Integer.parseInt(input[0]); i++){
            queue.add(i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");

        int cnt = 0;
        while(!queue.isEmpty()){
            int current = queue.poll();
            cnt++;
            if(cnt == Integer.parseInt(input[1])){
                cnt = 0;
                sb.append(current).append(", ");
            } else {
                queue.add(current);
            }
        }
        sb.setLength(sb.length()-2);
        sb.append(">");
        System.out.println(sb);

    }
}
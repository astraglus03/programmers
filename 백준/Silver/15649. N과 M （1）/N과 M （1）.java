// 백준 15649 N과 M (1) 

import java.util.*;
import java.io.*;

public class Main {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        boolean[] visited = new boolean[a+1];
        backtracking(a, b, new ArrayList<>(), visited);

        br.close();
        System.out.println(sb.toString().trim());

    }

    public static void backtracking(int n, int m, List<Integer> tmpList, boolean[] visited) {
        if(tmpList.size() == m){
            for(int i=0; i<m; i++){
                sb.append(tmpList.get(i)).append(" ");
            }
            sb.append("\n");
            return;
        }

        for(int i=1;i<=n;i++){
            if(visited[i]) continue;
            visited[i] = true;
            tmpList.add(i);
            backtracking(n,m, tmpList, visited);
            tmpList.remove(tmpList.size() - 1);
            visited[i] = false;
        }
    }
}

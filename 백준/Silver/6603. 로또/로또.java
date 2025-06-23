// 백준 6603 - 로또
import java.util.*;
import java.io.*;
import java.util.stream.*;

public class Main {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            List<Integer> myList = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
            if(myList.get(0) == 0 && myList.size() ==1) break;
            boolean[] visited = new boolean[myList.size()-1];
            backtracking(1, myList, new ArrayList<>(), visited);
            System.out.println(sb.toString());
            sb.setLength(0);
        }
    }

    public static void backtracking(int start, List<Integer> myList ,List<Integer> tmpList, boolean[] visited){
        if(tmpList.size() == 6){
            for (Integer integer : tmpList) {
                sb.append(integer).append(" ");
            }
            sb.append("\n");
            return;
        }
        for(int i=start; i<myList.size(); i++){
            if(visited[i-1]) continue;
            visited[i-1] = true;
            tmpList.add(myList.get(i));
            backtracking(i+1, myList, tmpList, visited);
            tmpList.remove(tmpList.size() - 1);
            visited[i-1] = false;
        }
    }
}

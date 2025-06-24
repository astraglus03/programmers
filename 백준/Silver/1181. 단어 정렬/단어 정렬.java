import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<String> list = new ArrayList<>();
        Set<String> set = new HashSet<>();
        for(int i=0; i<n; i++){
            String input = br.readLine();
            if(!set.contains(input)){
                set.add(input);
                list.add(input);
            }
        }
        Collections.sort(list, (s1, s2) -> {
            if(s1.length() != s2.length()){
                return s1.length() - s2.length();
            }
            return s1.compareTo(s2);
        });

        br.close();
        StringBuilder sb = new StringBuilder();
        for(String s : list){
            sb.append(s).append("\n");
        }
        System.out.print(sb.toString());
    }
}
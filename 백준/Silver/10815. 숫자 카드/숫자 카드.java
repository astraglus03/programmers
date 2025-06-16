import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] input1 = br.readLine().split(" ");
        int[] arr1 =  new int[n];
        for(int i=0; i<n; i++){
            arr1[i] = Integer.parseInt(input1[i]);
        }

        int m = Integer.parseInt(br.readLine());
        String[] input2 = br.readLine().split(" ");
        int[] arr2 =  new int[m];

        for(int j=0; j<m; j++){
            arr2[j] = Integer.parseInt(input2[j]);
        }

        br.close();

        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<n; i++){
            map.put(arr1[i], map.getOrDefault(arr1[i], 0) + 1);
        }
        StringBuilder sb = new StringBuilder();
        for(int j=0; j<m; j++){
            sb.append(map.getOrDefault(arr2[j], 0)).append(" ");
        }
        System.out.println(sb);
    }
}

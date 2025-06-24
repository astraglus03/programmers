import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];

        for(int i=0; i<n; i++){
            int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            arr[i][0] = input[0];
            arr[i][1] = input[1];
        }
        Arrays.sort(arr, (a,b) -> {
            if(a[0] == b[0]){
                return a[1]- b[1];
            }
            else{
                return a[0] - b[0];
            }
        });
        int res =0;
        int start = arr[0][0];
        int end = arr[0][1];

        for(int i=1; i<n ; i++){
            int tryStart = arr[i][0];
            int tryEnd = arr[i][1];
            if(tryStart <= end){
                end = Math.max(end, tryEnd);
            }
            else{
                res += end - start;
                start = tryStart;
                end = tryEnd;
            }
        }
        res += end- start;
        sb.append(res);
        br.close();
        System.out.println(sb);
    }
}
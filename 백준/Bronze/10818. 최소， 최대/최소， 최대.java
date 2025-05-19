import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] input = new int[n];

        String[] inputString = br.readLine().split(" ");
        for(int i=0; i<n; i++){
            input[i] = Integer.parseInt(inputString[i]);
        }
        Arrays.sort(input);
        System.out.println(input[0]+" "+input[n-1]);
    }
}

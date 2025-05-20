import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int[] arr = new int[Integer.parseInt(input[0])];
        int a = Integer.parseInt(input[1]);
        for(int i = 0; i < a; i++){
            String[] input2 = br.readLine().split(" ");
            int b = Integer.parseInt(input2[0]);
            int c = Integer.parseInt(input2[1]);
            int d = Integer.parseInt(input2[2]);

            for(int j=b;j<=c; j++){
                arr[j-1] = d;
            }
        }
        for (int j=0; j<arr.length; j++){
            System.out.print(arr[j] + " ");
        }
    }
}

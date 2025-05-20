import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int[][] arr1 = new int[a][b];
        int[][] arr2 = new int[a][b];

        for(int i=0; i<a; i++){
            String[] input2 = br.readLine().split(" ");
            for(int j=0; j<b; j++){
                arr1[i][j] = Integer.parseInt(input2[j]);
            }
        }

        for(int i=0; i<a; i++){
            String[] input3 = br.readLine().split(" ");
            for(int j=0; j<b; j++){
                arr2[i][j] = Integer.parseInt(input3[j]);
            }
        }
        for(int i=0; i<a; i++){
            for(int j=0; j<b; j++){
                System.out.print(arr1[i][j] + arr2[i][j] + " ");
            }
            System.out.println();
        }
    }
}

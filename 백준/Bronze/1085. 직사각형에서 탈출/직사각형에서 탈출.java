import java.io.BufferedReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int c = Integer.parseInt(input[2]);
        int d = Integer.parseInt(input[3]);

        int xMin = Math.min(a, c);
        int yMin = Math.min(b, d);

        if(xMin > c-a){
            xMin = c-a;
        }

        if(yMin > d-b){
            yMin = d-b;
        }

        System.out.println(Math.min(xMin, yMin));

    }
}

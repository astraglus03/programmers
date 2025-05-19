import java.io.BufferedReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int c = Integer.parseInt(input[2]);

        int result = (a+b)%c;
        int result2 = ((a%c)+(b%c))%c;
        int result3 = (a*b)%c;
        int result4 = ((a%c)*(b%c))%c;

        System.out.println(result+"\n"+result2+"\n"+result3+"\n"+result4);
    }
}

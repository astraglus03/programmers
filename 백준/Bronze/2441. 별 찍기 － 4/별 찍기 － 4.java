import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int i=n; i>0; i--){
            String star = "*".repeat(i);
            String blank = " ".repeat(n-i);
            System.out.println(blank + star);
        }
    }
}

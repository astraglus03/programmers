import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        String input = br.readLine();
        String backward="";

        for(int i=input.length(); i>0; i--){
            backward += input.charAt(i-1);
        }
        System.out.println(input.equals(backward) ? 1 : 0);
    }
}

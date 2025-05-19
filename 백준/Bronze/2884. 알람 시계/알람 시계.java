import java.io.BufferedReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        String[] time = br.readLine().split(" ");
        int hour = Integer.parseInt(time[0]);
        int minute = Integer.parseInt(time[1]);

        if(minute < 45){
            if(hour == 0){
                hour = 23;
            }else{
                hour--;
            }
            minute += 15;
        }
        else{
            minute -= 45;
        }

        System.out.println(hour + " " + minute);
    }
}

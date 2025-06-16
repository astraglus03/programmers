import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> bestSeller = new HashMap<>();

        for(int i=0;i<n;i++){
            String input = br.readLine();
            if(bestSeller.containsKey(input)){
                bestSeller.put(input, bestSeller.get(input) + 1);
            } else {
                bestSeller.put(input, 1);
            }
        }
        int maxCount = Integer.MIN_VALUE;
        String bestBook = "";

        for(String book: bestSeller.keySet()){
            if(bestSeller.get(book) > maxCount){
                maxCount = bestSeller.get(book);
                bestBook = book;
            } else if(bestSeller.get(book) == maxCount && book.compareTo(bestBook) < 0){
                bestBook = book;
            }
        }

        System.out.println(bestBook);
    }
}
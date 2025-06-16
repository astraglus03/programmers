import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String,Integer> hmap = new HashMap<>();
        for(String par: participant) hmap.put(par,hmap.getOrDefault(par,0)+1);
        for(String com: completion) hmap.put(com,hmap.get(com)-1);
        
        for(String key: hmap.keySet()){
            if(hmap.get(key) !=0){
                answer = key;
            }
        }
        
        return answer;
    }
}
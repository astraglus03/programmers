import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String,Integer> hmap = new HashMap<>();
        
        for(String[] lst: clothes){
            if(hmap.containsKey(lst[1])){
                hmap.put(lst[1],hmap.getOrDefault(lst[1],0)+1);
            }
            else{
                hmap.put(lst[1],1);
            }
        }
        
        for(String a: hmap.keySet()){
            answer*=((hmap.get(a))+1);
        }
        
        return answer-1;
    }
}
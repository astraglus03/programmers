import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Deque<Character> dq = new ArrayDeque<>();
        for(char c: s.toCharArray()){
            if(c == '('){
              dq.addLast(c);
            }
            else{
                if(dq.isEmpty()){
                    answer = false;
                    break;
                }
                dq.removeLast();
            }
        }
        if(!dq.isEmpty()){
            answer = false;
        }

        return answer;
    }
}
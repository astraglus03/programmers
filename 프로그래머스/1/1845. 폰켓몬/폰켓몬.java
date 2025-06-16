import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();
        for(int num : nums) {
            set.add(num);
        }

        int maxSelect = nums.length /2;

        if(set.size() <= maxSelect) {
            answer = set.size();
        } else {
            answer = maxSelect;
        }
        return answer;
    }
}
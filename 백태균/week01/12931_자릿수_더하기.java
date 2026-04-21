import java.util.*;

public class Solution {
    public int solution(int n) {
        String sn = String.valueOf(n);
        int answer = 0;

        for (int i=0; i<sn.length(); i++) {
            answer += sn.charAt(i) - '0';
        }

        return answer;

//         int answer = 0;

//         while (n > 0) {
//             answer += n % 10;
//             n /= 10;
//         }

//        return answer;
    }
}
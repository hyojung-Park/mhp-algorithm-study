class Solution {
    public int solution(int[] numbers) {
        int answer = 0;

        for (int i=0; i<=9; i++) {
            boolean found = false;

            for (int num : numbers) {
                if (i == num) {
                    found = true;
                    break;
                }
            }

            if (!found) {
                answer += i;
            }
        }

        return answer;
    }
}
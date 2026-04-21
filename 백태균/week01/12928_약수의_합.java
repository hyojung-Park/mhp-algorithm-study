class Solution {
    public int solution(int n) {
        int answer = 0;

        for (int i=1; i*i<=n; i++) {
            if (n % i == 0) {
                answer += i;  // 작은 약수

                if (i != n / i) {
                    answer += n / i;  // 쌍이 되는 큰 약수 (중복 방지)
                }
            }
        }

        return answer;
    }
}
class Solution {
    public long solution(long n) {

        long sqr = (int) Math.sqrt(n);
        if (sqr * sqr == n) {
            return (sqr + 1) * (sqr + 1);
        } else {
            return -1;
        }
    }
}
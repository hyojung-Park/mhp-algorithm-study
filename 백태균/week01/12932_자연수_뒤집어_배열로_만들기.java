class Solution {
    public int[] solution(long n) {
        StringBuilder sb = new StringBuilder();
        String sn = String.valueOf(n);

        for (int i=sn.length()-1; i>=0; i--) {
            sb.append(sn.charAt(i));
        }

        int[] arr = new int[sn.length()];
        for (int i=0; i<sn.length(); i++) {
            arr[i] = sb.charAt(i) - '0';
        }

        return arr;
    }
}
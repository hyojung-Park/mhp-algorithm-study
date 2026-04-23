class Solution {
    public String solution(String s) {

        StringBuilder sb = new StringBuilder();

        int len = s.length();
        int mid = len / 2;

        System.out.println(mid);

        if (s.length() % 2 == 0) {
            sb.append(s.charAt(mid-1));
            sb.append(s.charAt(mid));
        } else {
            sb.append(s.charAt(mid));
        }

        return sb.toString();
    }
}
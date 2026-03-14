class Solution {
    public String getHappyString(int n, int k) {
        List<String> result = new ArrayList<>();
        backtrack("", n, result);

        if (k > result.size()) return "";
        return result.get(k - 1);
    }

    private void backtrack(String current, int n, List<String> result) {
        if (current.length() == n) {
            result.add(current);
            return;
        }

        char[] chars = {'a', 'b', 'c'};

        for (char c : chars) {
            if (current.length() > 0 && current.charAt(current.length() - 1) == c)
                continue;

            backtrack(current + c, n, result);
        }
    }
}
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {

        List<List<Integer>> new_list = new ArrayList<>();

        Arrays.sort(arr);

        int minAbsDiff = Integer.MAX_VALUE;
        for (int i = 1; i <= arr.length-1; i++) {
            minAbsDiff = Math.min(minAbsDiff, arr[i] - arr[i - 1]);
        }

        for (int i = 1; i <= arr.length-1; i++) {
            if (arr[i] - arr[i - 1] == minAbsDiff) {
                new_list.add(Arrays.asList(arr[i - 1], arr[i]));
            }
        }

        return new_list;
    }
}

class Solution {
    class Pair implements Comparable<Pair> {
        long sum;
        int index;

        Pair(long sum, int index) {
            this.sum = sum;
            this.index = index;
        }

        public int compareTo(Pair other) {
            if (this.sum != other.sum) {
                return Long.compare(this.sum, other.sum);
            }
            return Integer.compare(this.index, other.index);
        }
    }

    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;

        long[] val = new long[n];
        int[] prev = new int[n];
        int[] next = new int[n];
        boolean[] removed = new boolean[n];

        for (int i = 0; i < n; i++) {
            val[i] = nums[i];
            prev[i] = i - 1;
            next[i] = i + 1;
        }
        next[n - 1] = -1;

        PriorityQueue<Pair> pq = new PriorityQueue<>();
        int inversions = 0;

        for (int i = 0; i < n - 1; i++) {
            pq.add(new Pair(val[i] + val[i + 1], i));
            if (val[i] > val[i + 1]) inversions++;
        }

        int operations = 0;
        while (inversions > 0 && !pq.isEmpty()) {
            Pair top = pq.poll();
            int i = top.index;

            if (removed[i] || next[i] == -1 || val[i] + val[next[i]] != top.sum) {
                continue;
            }

            int j = next[i];
            int p = prev[i];
            int nn = next[j];

            if (p != -1 && val[p] > val[i]) inversions--;
            if (val[i] > val[j]) inversions--;
            if (nn != -1 && val[j] > val[nn]) inversions--;

            val[i] = top.sum;
            removed[j] = true;
            next[i] = nn;
            if (nn != -1) prev[nn] = i;

            if (p != -1 && val[p] > val[i]) inversions++;
            if (nn != -1 && val[i] > val[nn]) inversions++;

            if (p != -1) pq.add(new Pair(val[p] + val[i], p));
            if (nn != -1) pq.add(new Pair(val[i] + val[nn], i));

            operations++;
        }

        return operations;
    }
}
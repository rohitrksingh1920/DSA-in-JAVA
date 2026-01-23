class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        vector<long long> val(n);
        for (int i = 0; i < n; i++) val[i] = nums[i];

        vector<int> left(n), right(n);
        for (int i = 0; i < n; i++) {
            left[i] = i - 1;
            right[i] = i + 1;
        }
        right[n - 1] = -1;

        using Pair = pair<long long, int>;
        priority_queue<Pair, vector<Pair>, greater<Pair>> pq;
        
        int inversions = 0;
        for (int i = 0; i < n - 1; i++) {
            pq.push({val[i] + val[i + 1], i});
            if (val[i] > val[i + 1]) inversions++;
        }

        int operations = 0;
        vector<bool> removed(n, false);

        while (inversions > 0) {
            auto [current_sum, i] = pq.top();
            pq.pop();

            if (removed[i] || right[i] == -1 || val[i] + val[right[i]] != current_sum) {
                continue;
            }

            int j = right[i];
            int prev = left[i];
            int next = right[j];

            if (prev != -1 && val[prev] > val[i]) inversions--;
            if (val[i] > val[j]) inversions--;
            if (next != -1 && val[j] > val[next]) inversions--;

            val[i] = current_sum;
            removed[j] = true;
            right[i] = next;
            if (next != -1) left[next] = i;

            if (prev != -1 && val[prev] > val[i]) inversions++;
            if (next != -1 && val[i] > val[next]) inversions++;

            if (prev != -1) pq.push({val[prev] + val[i], prev});
            if (next != -1) pq.push({val[i] + val[next], i});

            operations++;
        }

        return operations;
    }
};
class Solution {
    class TrieNode {
        TrieNode[] next = new TrieNode[26];
        int id = -1;
    }

    public void insert(TrieNode root, String s, int id) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            int idx = c - 'a';
            if (node.next[idx] == null) {
                node.next[idx] = new TrieNode();
            }
            node = node.next[idx];
        }
        node.id = id;
    }

    public long minimumCost(String source, String target, String[] original, String[] changed, int[] cost) {
        int n = source.length();
        Map<String, Integer> strToId = new HashMap<>();
        TrieNode root = new TrieNode();
        int idCounter = 0;

        for (String s : original) {
            if (!strToId.containsKey(s)) {
                strToId.put(s, idCounter);
                insert(root, s, idCounter);
                idCounter++;
            }
        }
        for (String s : changed) {
            if (!strToId.containsKey(s)) {
                strToId.put(s, idCounter);
                insert(root, s, idCounter);
                idCounter++;
            }
        }

        long[][] dist = new long[idCounter][idCounter];
        long INF = Long.MAX_VALUE;
        for (long[] row : dist) Arrays.fill(row, INF);
        for (int i = 0; i < idCounter; i++) dist[i][i] = 0;

        for (int i = 0; i < original.length; i++) {
            int u = strToId.get(original[i]);
            int v = strToId.get(changed[i]);
            dist[u][v] = Math.min(dist[u][v], cost[i]);
        }

        for (int k = 0; k < idCounter; k++) {
            for (int i = 0; i < idCounter; i++) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < idCounter; j++) {
                    if (dist[k][j] == INF) continue;
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        long[] dp = new long[n + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        char[] s = source.toCharArray();
        char[] t = target.toCharArray();

        for (int i = 0; i < n; i++) {
            if (dp[i] == INF) continue;

            if (s[i] == t[i]) {
                dp[i + 1] = Math.min(dp[i + 1], dp[i]);
            }

            TrieNode tNode = root;
            Map<Integer, Integer> lenToTargetId = new HashMap<>();
            
            for (int j = i; j < n; j++) {
                int idx = t[j] - 'a';
                if (tNode.next[idx] == null) break;
                tNode = tNode.next[idx];
                if (tNode.id != -1) {
                    lenToTargetId.put(j - i + 1, tNode.id);
                }
            }

            TrieNode sNode = root;
            for (int j = i; j < n; j++) {
                int idx = s[j] - 'a';
                if (sNode.next[idx] == null) break;
                sNode = sNode.next[idx];
                if (sNode.id != -1) {
                    int len = j - i + 1;
                    if (lenToTargetId.containsKey(len)) {
                        int sId = sNode.id;
                        int tId = lenToTargetId.get(len);
                        if (dist[sId][tId] != INF) {
                            dp[i + len] = Math.min(dp[i + len], dp[i] + dist[sId][tId]);
                        }
                    }
                }
            }
        }
        return (dp[n] == INF) ? -1 : dp[n];
    }
}
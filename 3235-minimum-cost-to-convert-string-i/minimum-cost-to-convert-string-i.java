class Solution {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        List<List<int[]>> graph = new ArrayList<>();
        for(int i=0; i<26; i++){
            graph.add(new ArrayList<>());
        }
        for(int i=0; i<cost.length; i++){
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            int c = cost[i];
            graph.get(u).add(new int[]{v, c});
        }

        long d[][] = floyd(graph);
        long total = 0;
        for(int i=0; i<target.length(); i++){
            int src = source.charAt(i) - 'a';
            int dest = target.charAt(i) - 'a';
            if(source.charAt(i) != target.charAt(i)){
                if(d[src][dest] == Long.MAX_VALUE){
                    return -1;
                }
                total += d[src][dest];
            }
        }
        return total;
    }
    public long[][] floyd(List<List<int[]>> graph){
        long d[][] = new long[26][26];
        for(int i=0; i<26; i++){
            Arrays.fill(d[i], Long.MAX_VALUE);
        }

        for(int i=0; i<26; i++){
            for(int neighbour[]: graph.get(i)){
                d[i][neighbour[0]] = Math.min(d[i][neighbour[0]], neighbour[1]);
            }
        }

        
        for(int i=0; i<5; i++){
            for(int j=0; j<5; j++){
                System.out.print(d[i][j] + " ");
            }
            System.out.println();
        }
        
        for(int k=0; k<26; k++){
            for(int i=0; i<26; i++){
                for(int j=0; j<26; j++){
                    if(d[i][k] != Long.MAX_VALUE && d[k][j] != Long.MAX_VALUE){
                        d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
                    }
                }
            }
        }
        for(int i=0; i<5; i++){
            for(int j=0; j<5; j++){
                System.out.print(d[i][j] + " ");
            }
            System.out.println();
        }
        return d;
    }
}
class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        Map<Integer, List<int[]>> timeMap = new TreeMap<>();
        
        for (int[] m : meetings) {
            timeMap.computeIfAbsent(m[2], k -> new ArrayList<>()).add(m);
        }

        Set<Integer> knowSecret = new HashSet<>();
        knowSecret.add(0);
        knowSecret.add(firstPerson);

        for (int time : timeMap.keySet()) {
            Map<Integer, List<Integer>> graph = new HashMap<>();
            Set<Integer> visited = new HashSet<>();

            for (int[] m : timeMap.get(time)) {
                graph.computeIfAbsent(m[0], k -> new ArrayList<>()).add(m[1]);
                graph.computeIfAbsent(m[1], k -> new ArrayList<>()).add(m[0]);
            }

            Queue<Integer> queue = new LinkedList<>();

            for (int person : graph.keySet()) {
                if (knowSecret.contains(person)) {
                    queue.offer(person);
                    visited.add(person);
                }
            }

            while (!queue.isEmpty()) {
                int curr = queue.poll();
                for (int next : graph.getOrDefault(curr, new ArrayList<>())) {
                    if (!visited.contains(next)) {
                        visited.add(next);
                        queue.offer(next);
                        knowSecret.add(next);
                    }
                }
            }
        }

        return new ArrayList<>(knowSecret);
    }
}

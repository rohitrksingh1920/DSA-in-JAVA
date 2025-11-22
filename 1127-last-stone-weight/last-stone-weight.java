class Solution {
    public int lastStoneWeight(int[] stones) {
        //max priority queue
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for(int ele : stones) {    //adding element of array to priority queue
            pq.add(ele);
        }

        while(pq.size() > 1) {
            int max = pq.remove();
            int smax = pq.remove();

            int new_stone = max - smax;

            if(new_stone != 0) {
                pq.add(new_stone);
            }
        }
        if(pq.size() == 0) {
            return 0;
        }
        else{
            return pq.remove();
        }
    }
}
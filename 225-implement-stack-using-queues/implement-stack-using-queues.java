class MyStack {
    private Queue<Integer> main;
    private Queue<Integer> helper;

    public MyStack() {
        main = new LinkedList<>();
        helper = new LinkedList<>();
    }

    public void push(int x) {
        // Move all elements from main to helper
        while (main.size() > 0) {
            helper.add(main.remove());
        }

        // Add the new element to main
        main.add(x);

        // Move everything back to main
        while (helper.size() > 0) {
            main.add(helper.remove());
        }
    }
    public int pop() {
        return main.remove();
    }
    public int top() {
        return main.peek();
    }

    public boolean empty() {
        return main.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
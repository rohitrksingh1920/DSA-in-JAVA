class Solution {

    static class Event {
        double y;
        int l, r;
        int type;
        Event(double y, int l, int r, int type) {
            this.y = y;
            this.l = l;
            this.r = r;
            this.type = type;
        }
    }

    static class SegTree {
        int n;
        int[] cnt;
        double[] len;
        double[] xs;

        SegTree(double[] xs) {
            this.xs = xs;
            n = xs.length - 1;
            cnt = new int[4 * n];
            len = new double[4 * n];
        }

        void update(int idx, int l, int r, int ql, int qr, int val) {
            if (qr <= l || r <= ql) return;
            if (ql <= l && r <= qr) {
                cnt[idx] += val;
            } else {
                int mid = (l + r) / 2;
                update(idx * 2, l, mid, ql, qr, val);
                update(idx * 2 + 1, mid, r, ql, qr, val);
            }

            if (cnt[idx] > 0) {
                len[idx] = xs[r] - xs[l];
            } else if (l + 1 == r) {
                len[idx] = 0;
            } else {
                len[idx] = len[idx * 2] + len[idx * 2 + 1];
            }
        }
    }

    public double separateSquares(int[][] squares) {
        int n = squares.length;

        // collect x-coordinates
        double[] xs = new double[2 * n];
        for (int i = 0; i < n; i++) {
            xs[2 * i] = squares[i][0];
            xs[2 * i + 1] = squares[i][0] + squares[i][2];
        }
        Arrays.sort(xs);

        Map<Double, Integer> comp = new HashMap<>();
        int id = 0;
        for (double x : xs) {
            if (!comp.containsKey(x)) comp.put(x, id++);
        }

        List<Event> events = new ArrayList<>();
        for (int[] s : squares) {
            double x = s[0], y = s[1], d = s[2];
            int l = comp.get(x);
            int r = comp.get(x + d);
            events.add(new Event(y, l, r, +1));
            events.add(new Event(y + d, l, r, -1));
        }

        events.sort(Comparator.comparingDouble(e -> e.y));
        SegTree st = new SegTree(Arrays.stream(xs).distinct().toArray());

        double total = 0;
        double prevY = events.get(0).y;

        for (Event e : events) {
            double dy = e.y - prevY;
            total += st.len[1] * dy;
            st.update(1, 0, st.n, e.l, e.r, e.type);
            prevY = e.y;
        }

        double half = total / 2.0;

        // second sweep
        st = new SegTree(Arrays.stream(xs).distinct().toArray());
        double acc = 0;
        prevY = events.get(0).y;

        for (Event e : events) {
            double dy = e.y - prevY;
            if (st.len[1] > 0 && acc + st.len[1] * dy >= half) {
                return prevY + (half - acc) / st.len[1];
            }
            acc += st.len[1] * dy;
            st.update(1, 0, st.n, e.l, e.r, e.type);
            prevY = e.y;
        }
        return prevY;
    }
}

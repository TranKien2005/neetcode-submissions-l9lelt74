class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int r = Arrays.stream(piles).max().getAsInt();
        int l = 1;
        int res = r;

        while (l <= r) {
            int m = (l + r) / 2;
            int counter = 0;
            System.out.print(l);
            System.out.print(m);
            System.out.print(r);
            System.out.println(res);
            for (int pile: piles) {
                counter += Math.ceil((double) pile / m);
            }

            if (counter <= h) {
                res = m;
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }

        return res;
    }
}

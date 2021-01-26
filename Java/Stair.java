class Stair
{
    public static int totalWays(int n)
    {
        if (n < 0) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }
        return totalWays(n - 1) + totalWays(n - 2);
    }

    public static void main(String[] args)
    {
        int n = 5;
        System.out.println(totalWays(n));
    }
}
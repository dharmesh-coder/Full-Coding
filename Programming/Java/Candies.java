import java.util.Scanner;
public class Candies {
    public static void main(String args[])
    {
        int T,x,i,s=0,min=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no. of test case");
        T=sc.nextInt();
        if (T>=1 && T<10)
        {
            for (x=0;x<T;x++)
            {
                System.out.println("Enter the details of test case no "+x);
                int N;
                System.out.println("Enter the number of boxes");
                N=sc.nextInt();
                int[] C = new int[N];
                if (N>1 && N<10000) {
                    for (i = 0; i < N; i++) {
                        C[i] = sc.nextInt();
                    }
                }
                int[] sum=new int[N];
                s=s+C[0]+C[1];
                sum[0]=s;
                for (i=2;i<N;i++)
                {
                    s=s+C[i];
                    sum[i]=s;
                }
                for (i=0;i<N;i++)
                {
                    min=min+sum[i];
                }
                System.out.println("The minimum time is " +min);
                s=0;
                min=0;
            }
        }
    }
}
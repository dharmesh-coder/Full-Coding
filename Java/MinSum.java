import java.io.*;
import java.util.*;
import java.util.Arrays;

public class MinSum {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int N,k,i,j,c=0;
        N=sc.nextInt();
        k=sc.nextInt();
        int[] arr = new int[N];
        if (1 <= N && k <= 100000) {
            for (i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);
            while (true)
            {
                arr[N-1]=arr[N-1]/2;
                Arrays.sort(arr);
                c++;
                if (c==k)
                {
                    break;
                }
            }
        }
        int sum=0;
        for (i=0;i<N;i++)
        {
            sum=sum+arr[i];
        }
        System.out.println(sum);
    }
}

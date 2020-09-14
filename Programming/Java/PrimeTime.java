import java.io.*;
import java.util.*;

public class PrimeTime{
    public static boolean isPrime(int n) {
        if (n<=1)
        {
            return false;
        }
        if (n<=3)
        {
            return true;
        }
        else {
            for (int i = 2; i < Math.sqrt(n); i++) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }
    }


    public static void main(String args[])
    {
        int D,P,i,j,k=1;
        Scanner sc= new Scanner(System.in);
        D= sc.nextInt();
        P= sc.nextInt();
        int count=0;
        int H=D/P;
        int c=0;
        int[][] array= new int[H][P];
        for (i=0;i<H;i++)
        {
            for (j=0;j<P;j++)
            {
                array[i][j]=j*H+k;
            }
            k=k+1;
        }
        for (i=0;i<H;i++)
        {
            for (j=0;j<P;j++)
            {
                if (isPrime(array[i][j]))
                {
                    count=count+1;
                }
                if (count==P)
                {
                    c=c+1;
                }
            }
            count=0;
        }
        System.out.println(c);
    }
}

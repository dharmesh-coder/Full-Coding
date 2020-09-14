import java.util.*;
import java.util.Scanner;




public class Pair
{
    public static void main(String args[])
    {
        int n,i,j,d;
        int a=0,b=0,r;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        int[] N=new int[n];
        int[] Bit=new int[n];
        int[] even=new int[n];
        int[] odd =new int[n];
        int[] countsig1=new int[10];
        int[] countsig2=new int[10];
        int largest = 0;
        int smallest = 9;
        if (n<=500)
        {
            for (i=0;i<n;i++)
            {
                N[i]=sc.nextInt();


                while(N[i]!= 0)
                {
                    r = N[i] % 10;
                    largest = Math.max(r, largest);
                    smallest = Math.min(r, smallest);
                    N[i] = N[i] / 10;
                }
                Bit[i]=largest*11+smallest*7;
                Bit[i]=Bit[i]%100;
                largest=0;
                smallest=9;
            }

                for (i = 0; i < n; i++)
                {
                    if ((i + 1) % 2 == 0) {
                        even[a] = Bit[i];
                        a = a + 1;
                    } else {
                        odd[b] = Bit[i];
                        b = b + 1;
                    }
                }
            }

            if (n%2==0) {
                for (i = 0; i < (n / 2); i++) {
                    for (d = 0; d < 10; d++) {

                        if (even[i] / 10 == d) {
                            countsig1[d] = countsig1[d] + 1;
                        } else {
                            countsig1[d] = countsig1[d];
                        }
                        if (odd[i] / 10 == d) {
                            countsig2[d] = countsig2[d] + 1;
                        } else countsig2[d] = countsig2[d];
                    }

                }
            }

            else {
                for (i = 0; i < (n / 2); i++)
                {
                    for (d = 0; d < 10; d++)
                    {
                        if (even[i] / 10 == d) {
                            countsig1[d] = countsig1[d] + 1;
                        } else {
                            countsig1[d] = countsig1[d];
                        }
                    }
                }

                for (i = 0; i < (n / 2+1); i++) {
                    for (d = 0; d < 10; d++) {
                        if (odd[i] / 10 == d) {
                            countsig2[d] = countsig2[d] + 1;
                        } else countsig2[d] = countsig2[d];
                    }

                }
            }


            for (i=0;i<10;i++)
            {
                if (countsig1[i]==0 || countsig1[i]==1)
                    countsig1[i]=0;
                else if (countsig1[i]==2)
                    countsig1[i]=1;
                else
                    countsig1[i]=2;


                if (countsig2[i]==0 || countsig2[i]==1)
                    countsig2[i]=0;
                else if (countsig2[i]==2)
                    countsig2[i]=1;
                else
                    countsig2[i]=2;

            }

            int asd=0;

            for (i=0;i<10;i++)
            {
                asd=countsig1[i]+countsig2[i]+asd;
            }

            System.out.println(asd);



    }
}
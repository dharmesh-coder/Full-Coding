/* Target Set */

import java.util.Scanner;

public class Solution {
    public static void main(String[] args)
    {
        int i,n,m,j;
        int s=0;
        Scanner sc= new Scanner(System.in);
        n= sc.nextInt();
        int[] arr1=new int[n];
        int[] sum=new int[n];
        if(n>=1 && n<=100000){
            for (i=0;i<n;i++)
            {
                arr1[i]=sc.nextInt();
                if(arr1[i]>=1 && arr1[i]<=1000){
                    s=s+arr1[i];
                    sum[i]=s;
                }
                
            }
        }
        
        m=sc.nextInt();

        int[] arr2=new int[m];
        int[] arrdemo=new int[m];
        if(m>=1 && m<=1000000){
            for (j=0;j<m;j++)
            {
                arrdemo[j]=sc.nextInt();
                if(arrdemo[j]>=1 && arrdemo[j]<=1000000000){
                    arr2[j]=arrdemo[j];
                }

            }
        }

        int a=0;
        int b=0;
        while (b<=m-1)
        {
            if (sum[a]>=arr2[b])
            {
                System.out.println(a+1);
                if (b<=(m-1))
                {
                    b=b+1;
                }
                a=0;
            }
            else
            {
                if (a<(n-1))
                {
                    a=a+1;
                }
                else
                {
                    System.out.println(-1);
                    if (b<=(m-1))
                    {
                        b=b+1;
                    }
                    a=0;
                }
            }


        }
    }
}

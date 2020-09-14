import java.io.*;
import java.util.*;

public class Mangoes
{

    public static void main(String[] args)
    {

        int i,n,j;
        int s=0;
        int a=0;
        int b=0;
        int z=0;
        Scanner sc= new Scanner(System.in);
        n= sc.nextInt();
        int[] array=new int[n];
        int[] arr2=new int[1000];
        int[] arr1=new int[n];
        if (n>=1 && n<=1000)
        {
            for (i=0;i<n;i++)
            {
                array[i]=sc.nextInt();
                s=s+array[i];
            }
            if (s%3==0)
            {
                System.out.println(s);
            }
            else
            {
                for (i=0;i<n;i++)
                {
                    a=s-array[i];
                    if (a%3==0)
                    {
                        arr1[i]=a;
                    }
                }
                for (i=0;i<n;i++)
                {
                    for (j=i+1;j<n;j++)
                    {
                        b=s-array[i]-array[j];
                        if (b%3==0)
                        {
                            arr2[z]=b;
                            z++;
                        }


                    }



                }

                int max1=0;
                for(i=0;i<n;i++)
                {
                    if(arr1[i] > max1)
                    {
                        max1 = arr1[i];
                    }
                }


                int max2=0;
                for(i=0;i<n;i++)
                {
                    if(arr2[i] > max2)
                    {
                        max2 = arr2[i];
                    }
                }


                if (max1>max2)
                {
                    System.out.println(max1);
                }
                else System.out.println(max2);
            }

        }

    }
}
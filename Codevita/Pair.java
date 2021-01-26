import java.util.*;
import java.util.Scanner;




public class Pair
{
  public static void main(String args[])
  {
    int n,i,j,d=0;
    int a,b,r;
    Scanner sc=new Scanner(System.in);
    n=sc.nextInt();
    int[] N=new int[n];
    int[] Bit=new int[n];
    int[] even=new int[n];
    int[] odd =new int[n];
    int[] countsig1=new int[n];
    int[] countsig2=new int[n];
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
    
    for (i=0;i<n;i++)
    {
      a=0;
      b=0;
     if ((i+1)%2==0)
     {
       even[a]=Bit[i];
       a=a+1;
     }
     else
     {
     odd[b]=Bit[i];
     b=b+1;
     }
     }
     for (i=0;i<n;i++)
     {
      for (j=i+1;j<n;j++)
      {
        if (even[i]/10==d )
        {
            countsig1[d]=countsig1[d]+1;
        }
         else 
         {
           countsig1[d]=countsig1[d];
         }
        if (odd[i]/10==d )
        {
            countsig2[d]=countsig2[d]+1;
        }
          else countsig2[d]=countsig2[d];
      } 
      d=d+1;
    }
  

       
       for (i=0;i<n;i++)
       {
          if (countsig1[i]==0 || countsig1[i]==1)
            countsig1[i]=0;
         else
           countsig1[i]=2;
       
         
          if (countsig2[i]==0 || countsig2[i]==1)
            countsig2[i]=0;
         else
           countsig2[i]=2;

       }
       
      int asd=0;
       
       for (i=0;i<n;i++)
       {
         asd=countsig1[i]+countsig2[i]+asd;
       }
      
     System.out.println(asd);
      
      
    }
  }
}
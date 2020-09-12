/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Arrays;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	      
			//Your Solve
	
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		if (n>=1 && n<=100)
		{
		String[] path = new String[100];
                String[] path1=new String[100];
		int[] point=new int[20];
		int i,j;
		int[] max1=new int[20];
		for (i=0; i<n; i++)
		{
		      path1 [i] = sc.next();
                      path[i]=path1[i].toLowerCase();
		}
            char choice=sc.next().charAt(0);
            
		switch(choice)
		{
		case 'n' :
                case 'N':
		{
		      for (i=0;i<n;i++)
		      {
		            for (j=0;j<path[i].length();j++)
		            {
		              if (path[i].charAt(j)=='r')
		              {
		                  point[i]=point[i]+3;
		              }
		              else if (path[i].charAt(j)=='o')
		              {
		                    point[i]=point[i]+2;
		              }
		              else point[i]=point[i]+1;
		            } 
		             
		      }
		      break;
		}
		case 'i' :
                case 'I':
		{
		   for (i=0;i<n;i++)
		      {
		            for (j=0;j<path[i].length();j++)
		            {
		              if (path[i].charAt(j)=='r' || path[i].charAt(j)=='o')
		              {
		                  point[i]=point[i]+1;
		              }
		              else point[i]=point[i];
		            } 
		           
		             
		      }  
		      break;
		}
		}
		int min=point[0];
		for( i=0;i <n;i++)
		{
		      if(point[i] < min)
		      { 
                    min = point[i]; 
		      }
		      
            }
            System.out.println(min);
	
		      
		}	      
	      
	      
		      
	}
}

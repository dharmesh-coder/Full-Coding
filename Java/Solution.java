import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        int N,i,M;
        int sum=0;
        int count=0;
        Scanner sc= new Scanner(System.in);
        N= sc.nextInt();
        int[] D = new int[N];
        if (N>=1) {
            for (i = 0; i < N; i++) {
                D[i] = i + 1;
            }
        }
        M=sc.nextInt();
        if (M<=10000)
        {
            for (i=N-1;i>=0;i--)
            {
               if (M<=i)
               {
                   count=count+1;
                   M=M-i;
               }
            }
        }
    }
}
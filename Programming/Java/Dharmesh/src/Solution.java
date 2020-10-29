
// A Java program to find a  
// maximum product of a 
// quadruple in array of integers 
import java.io.*; 
import java.util.Arrays; 
  
class Solution  
{ 
  
/* Function to find a  
maximum product of a quadruple 
in array of integers of size n */
static int maxProduct(int arr[],  
                      int n) 
{ 
    // if size is less than 4,  
    // no quadruple exists 
    if (n < 4) 
        return -1; 
  
    // Sort the array  
    // in ascending order 
    Arrays.sort(arr); 
  
    int x = arr[n - 1] * arr[n - 2] *  
            arr[n - 3] * arr[n - 4]; 
    int y = arr[0] * arr[1] * 
            arr[2] * arr[3]; 
    int z = arr[0] * arr[1] *  
            arr[n - 1] * arr[n - 2]; 
  
    // Return the maximum 
    // of x, y and z 
    return Math.max(x, Math.max(y, z)); 
} 
  
// Driver Code 
public static void main (String[] args)  
{ 
    int arr[] = {-10, -3, 5, 6, -20}; 
    int n = arr.length; 
    int max = maxProduct(arr, n); 
    if (max == -1) 
        System.out.println("No Quadruple Exists"); 
    else
        System.out.println("Maximum product is " + 
                                             max); 
} 
} 
  
// This code is contributed 
// by anuj_67 
import java.io.*;
import java.util.*;

public class Constellation {
    public static void main(String args[])
    {
        int N;
        int i,j;
        Scanner sc= new Scanner(System.in);
        N= sc.nextInt();
        char[][] arr = new char[3][N];
            for (i = 0; i < 3; i++) {
                for (j = 0; j <= N - 1; j++) {
                    arr[i][j] = sc.next().charAt(0);
                }
            }
            i=0;
            for (i=0;i<N;i++) {
                if (arr[0][i] == '#' && arr[1][i] == '#' && arr[2][i]=='#')
                {
                        System.out.print("#");
                }
                else if (arr[1][i+1]=='.')
                {
                    if (arr[0][i+1]=='.')
                    {
                        System.out.print("U");
                    }
                    else System.out.print("O");
                    i=i+2;
                }

                else if (arr[1][i]=='.' && arr[1][i+2]=='.')
                {
                    System.out.print("I");
                    i=i+2;
                }
                else if (arr[0][i]=='.' && arr[0][i+2]=='.' && arr[2][i+1]=='.')
                {
                    System.out.print("A");
                    i=i+2;
                }
                else {
                    System.out.print("E");
                    i = i + 2;
                }
                    if (i==N)
                {
                    break;
                }
            }

    }
}

import java.util.Scanner;
public class Matrix {
	public static void main(String args[]) {
		int row,col,i,j;
		Scanner sc=new Scanner(System.in);
		row=sc.nextInt();
		col=sc.nextInt();
		int m1[][]=new int[row][col];
		int m2[][]=new int[row][col];
		int res[][]=new int[row][col];
		for(i=0;i<row;i++) {
			for(j=0;j<col;j++) {
				m1[i][j]=sc.nextInt();
			}
		}
		for(i=0;i<row;i++) {
			for(j=0;j<col;j++) {
				m2[i][j]=sc.nextInt();
			}
		}
		for(i=0;i<row;i++) {
			for(j=0;j<col;j++) {
				res[i][j]=m1[i][j]-m2[i][j];
			}
		}
		for(i=0;i<row;i++) {
			for(j=0;j<col;j++) {
				System.out.print(res[i][j]);
			}
			System.out.println();
		}
	}
	
}

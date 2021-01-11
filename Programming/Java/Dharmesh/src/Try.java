import java.util.*;
public class Try {
	int one,two;
	Try(int a,int b) {
		one=a;
		two=b;
	}
	void add(){
		System.out.println(one+two);
	}
	public static void main(String args[]) {
		int x,y;
		Scanner sc =new Scanner(System.in);
		x=sc.nextInt();
		y=sc.nextInt();
		Try obje=new Try(x,y);
		obje.add();
	}
}

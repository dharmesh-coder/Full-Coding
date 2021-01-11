import java.util.Scanner;
public class Add {
	int one,two;
	Add(int a,int b) {
		one=a;
		two=b;
	}
	void Addi(){
		System.out.println(one+two);
	}
	public static void main(String args[]) {
		int x,y;
		Scanner sc =new Scanner(System.in);
		x=sc.nextInt();
		y=sc.nextInt();
		Add obje=new Add(x,y);
		obje.Addi();
	}
}

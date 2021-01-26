
public class Trick {

	public static void main(String[] args) {
		int c=34;
		int d=12;
		
		swap(c,d);
		System.out.println(c+" "+d);

	}
	
	static int swap(int a,int b) {
		int temp=a;
		a=b;
		b=temp;
		return a;
	}

}

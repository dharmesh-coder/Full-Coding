import java.util.Queue;
import java.util.LinkedList;
public class QueueEx {
	public static void main(String args[]) {
		Queue<Integer> q=new LinkedList<Integer>();
		q.add(10);
		System.out.println(q);
		q.add(5);
		System.out.println(q);
		q.add(12);
		System.out.println(q.peek());
		System.out.println(q);
		q.remove();
		System.out.println(q);
		System.out.println(q.size());
		
	}
}
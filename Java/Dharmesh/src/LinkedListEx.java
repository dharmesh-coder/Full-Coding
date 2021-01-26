import java.util.LinkedList;
public class LinkedListEx {
	public static void main(String args[]) {
		LinkedList L=new LinkedList();
		L.add(10);
		L.add(85);
		L.add(45);
		L.add(9);
		L.add(12);
		System.out.println(L);
		L.remove();
		L.removeLast();
		System.out.println(L);
		System.out.println(L.getFirst());
		L.addFirst(2);
		System.out.println(L);
		L.add(3,18);
		System.out.println(L);
		System.out.println(L.contains(100));
		System.out.println(L.element());
		System.out.println(L.getLast());
	}
}

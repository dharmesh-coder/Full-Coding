import java.util.Stack;
public class StackEx {
	public static void main(String args[]) {
		Stack<Character> stk=new Stack<>();
		stk.push('a');
		stk.push('b');
		stk.push('c');
		stk.pop();
		System.out.println(stk.peek());
		System.out.println(stk.empty());
		System.out.print(stk);
	}
}
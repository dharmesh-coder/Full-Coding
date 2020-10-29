import java.util.Stack;
import java.util.*;
 
public class Parenthesis {
 
    public static void main(String[] args) {
    	 Scanner sc=new Scanner(System.in);
         String str = new String();
         str=sc.nextLine();

         Stack<Character> st = new Stack<Character>();
         int count=0;
 
         for(int i = 0; i < str.length(); i++) {
 
            if(str.charAt(i) == '{' || str.charAt(i) == '[' || str.charAt(i) == '(') {
                   st.push(str.charAt(i));
                   count++;
 
            } else if ( !st.empty() && ((str.charAt(i) == ']' && (st.peek()).equals('[')) || 
                        (str.charAt(i) == '}' && (st.peek()).equals('{')) ||
                        (str.charAt(i) == ')' && (st.peek()).equals('(')))) {
 
                   st.pop();
                   count++;
 
             } else if (str.charAt(i) == '}' || str.charAt(i) == ']' || str.charAt(i) == ')')  {
                  st.push(str.charAt(i));
                  count++;
                  break;
             }
             else {
            	 continue;
             }
         }
 
         if(st.empty()) {
              System.out.println("Success");
         } else {
              System.out.println(count);
         }
  }
}
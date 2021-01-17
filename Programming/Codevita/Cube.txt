import java.util.*;

class Cube{
    public void rotateMatrix( int N, int mat[][]) 
    { 
        for (int x = 0; x < N / 2; x++) { 
            for (int y = x; y < N - x - 1; y++) { 
                int temp = mat[x][y]; 
                mat[x][y] = mat[y][N - 1 - x]; 
                mat[y][N - 1 - x] 
                    = mat[N - 1 - x][N - 1 - y]; 
                mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]; 
                mat[N - 1 - y][x] = temp; 
            } 
        }
    } 

    public void melting(int N, int mat[][]) {
    
    	for(int i=0;i<N;i++) {
    		int top=0;
    	    int down=N-1;
    	  for(int loop=0;loop<N;loop++) {
    		  if(top>down) {
    			  break;
    		  }
    		for(;top<N;top++) {
    			if(mat[top][i]==0) {
    				mat[top][i]=-1;
    			}
    			else if(mat[top][i]==1) {
    			   break;
    			}
    		}
    		for(;down>0;down--) {
    			if(mat[down][i]==0) {
    				mat[down][i]=1;
    				mat[top][i]=-1;
    				top++;
    				down--;
    				break;
    			}
    		}
    	  }
    	}

    }

    public int wall_size(int N,int mat[][]){
    	
    	   int[] arr = new int[N];
    	    for(int i=0;i<N;i++) {
    	    	arr[i]=(i+1);
    	    }
    	    
    	    for(int i=0;i<arr.length;i++) {
    	    	int loop=0;
  
    	    	for(int col=0;col<N;col++) {
    	  	    	int count =0;
    	    		for(int row=0;row<N;row++ ) {
    	    			if(count==arr[i]) {
    	    				break;
    	    			}
    	    			if(mat[row][col]==-1) {
    	    			    count++;
    	    			}
    	    			else  if(mat[row][col]==1)
    	    			{
    	    				break;
    	    			}
    	    		}
    	    	    if(count<arr[i]) {
    	    	    	loop=0;
    	    	    }
    	    		if(count==arr[i]) {
    	    			loop++;
    	    			if(loop==arr[i]) {
    	    				arr[i]=-1;
    	    				break;
    	    			
    	    			}
    	    		}
    	    		
    	    	
    	    	}
    	    }
    	    
    	    
    	    for(int i=(arr.length)-1;i>=0;i--) {
    	    	if(arr[i]==-1) {
    	    		return (i+1);
    	    	}
    	    }
    	    return 0;
    }
    
    public void print(int size,int[][] mat) {
    	System.out.println();
    	for(int i =0;i<size;i++	) {
    		for ( int j=0;j<size;j++) {
    			System.out.print("  "+mat[i][j]+"  ");
    		}
    		System.out.println();
    	}
    }
  
}


//Main class
public class Cube_Fill {
 public static void main(String[] args) {
	 Scanner input = new Scanner(System.in);
	 int wall_size = input.nextInt();
	 input.nextLine();
	 String[] bricks = new String[wall_size];
	 int[][] bmatrix = new int[wall_size][wall_size];
	 int[][] bmatrix1 = new int[wall_size][wall_size];

	 
	 for(int i=0;i<bricks.length;i++) {
		 bricks[i] = input.nextLine();
		for(int j=0;j<bricks.length;j++) {
			if(bricks[i].charAt(j)=='C') {
						bmatrix[i][j] = 1;
}
			else
				bmatrix[i][j]=0;
		}
	 }
	 
	 Cube cubObj = new Cube();
	 
	 int[][] k = new int[2][2];
	 k[0][1]=1;
	 int[][] j = new int[2][2];
	 
	 for(int i=0;i<k.length;i++) {
	 System.arraycopy(k[i]	, 0, j[i], 0, k[0].length);
	 }
	 j[0][1] = 0;
	 System.out.println(k[0][1]);

	for(int i=0;i<bmatrix.length;i++) {
	 System.arraycopy(bmatrix[i], 0, bmatrix1[i], 0, bmatrix[0].length);
	}
     cubObj.rotateMatrix(wall_size, bmatrix1); 
	 cubObj.melting(wall_size, bmatrix);
	 cubObj.melting(wall_size,bmatrix1);
		
	 int notRotated =  cubObj.wall_size(wall_size, bmatrix); 
	 int rotated = cubObj.wall_size(wall_size, bmatrix1);  
	 if(notRotated>=rotated) {
		 System.out.println(notRotated);
	 }
	 else {
		 System.out.println(rotated);
	 }
   }

}
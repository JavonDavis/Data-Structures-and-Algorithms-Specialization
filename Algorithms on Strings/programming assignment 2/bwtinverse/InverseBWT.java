import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class InverseBWT {
    class FastScanner {
        StringTokenizer tok = new StringTokenizer("");
        BufferedReader in;

        FastScanner() {
            in = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() throws IOException {
            while (!tok.hasMoreElements())
                tok = new StringTokenizer(in.readLine());
            return tok.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    String inverseBWT(String bwt) {
        StringBuilder result = new StringBuilder();
		
		char[] alphabet = new char[]{'A','C','G','T', '$'};

        // write your code here
		char[] tmpArray = bwt.toCharArray();
		Arrays.sort(tmpArray);
		String firstColumn = new String(tmpArray);
		
		Map<Character, List<Integer>> letterPositionMap = new HashMap<>();
		
		// Populate position map for first column
		for(int i = 0; i < bwt.length(); i ++) {
			List<Integer> mList = letterPositionMap.get(firstColumn.charAt(i));
			char c = firstColumn.charAt(i);
			if(mList == null) {
				mList = new ArrayList<>();
				letterPositionMap.put(c, mList);
			}
			mList.add(i); // Add position to the arrayList
		}
				//
		// for(Map.Entry<Character, List<Integer>> entry: letterPositionMap.entrySet()) {
		// 	System.out.println(entry.getKey() +" - " +entry.getValue());
		// }

		Map<Character, Integer> alphabetCount = new HashMap<>();
		
		for(char c: alphabet) {
			alphabetCount.put(c, 0);
		}
		
		List<Integer> positionCount = new ArrayList<>();
		
		for(char c: bwt.toCharArray()) {
			int count = alphabetCount.get(c);
			positionCount.add(count);
			alphabetCount.put(c, count+1);
		}
		
		
		int row = 0; 
		char c = bwt.charAt(row);
		result.append("$");
		
		while(c != '$') {
			result.append(c);
			
			int count = positionCount.get(row);
			
			int firstColumnPosition = letterPositionMap.get(c).get(row);
			row = positionCount.get(firstColumnPosition);
			
			c = bwt.charAt(firstColumnPosition);
		}
		result.reverse();
        return result.toString();
    }

    static public void main(String[] args) throws IOException {
        new InverseBWT().run();
    }

    public void run() throws IOException {
        FastScanner scanner = new FastScanner();
        String bwt = scanner.next();
        System.out.println(inverseBWT(bwt));
    }
}

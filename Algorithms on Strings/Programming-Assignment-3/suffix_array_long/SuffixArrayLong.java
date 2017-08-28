import java.util.*;
import java.io.*;
import java.util.zip.CheckedInputStream;

public class SuffixArrayLong {
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

    public class Suffix implements Comparable {
        String suffix;
        int start;

        Suffix(String suffix, int start) {
            this.suffix = suffix;
            this.start = start;
        }

        @Override
        public int compareTo(Object o) {
            Suffix other = (Suffix) o;
            return suffix.compareTo(other.suffix);
        }
    }
	
	int[] sortCharacters(String s) {
		int alphabetLength = 5;
		int[] order = new int[s.length()];
		char[] alphabet = new char[]{'$', 'A','C','G','T'};
		Map<Character, Integer> count = new HashMap<>();
		count.put('$', 0);
		count.put('A', 0);
		count.put('C', 0);
		count.put('G', 0);
		count.put('T', 0);
		for(int i = 0; i < s.length(); ++i) {
			char c = s.charAt(i);
			count.put(c, count.get(c) + 1);
		}
		
		for(int j = 1; j < alphabetLength; ++j) {
			count.put(alphabet[j],count.get(alphabet[j]) + count.get(alphabet[j - 1]));
		}
		
		for(int i = s.length() - 1; i >= 0; --i) {
			char c = s.charAt(i);
			count.put(c,count.get(c) - 1);
			order[count.get(c)] = i;
		}
		return order;
	}
	
	int[] computeCharClasses(String s, int[] order) { 
		int[] mClass = new int[s.length()];
		mClass[order[0]] = 0; // Set the smallest position to the first equivalence class 
		for(int i = 1; i < s.length(); ++i) {
			if(s.charAt(order[i]) != s.charAt(order[i - 1])) {
				mClass[order[i]] = mClass[order[i-1]] + 1;
			} else {
				mClass[order[i]] = mClass[order[i-1]];
			}
		}
		return mClass;
	}
	
	int[] sortDoubled(String s, int L, int[] order, int[] mClass) {
		int[] count = new int[s.length()];
		int[] newOrder = new int[s.length()];
		
		for(int i = 0; i < s.length(); ++i) {
			++count[mClass[i]];
		}
		
		for(int j = 1; j < s.length(); ++j) {
			count[j] += count[j-1];
		}
		
		for(int i = s.length() - 1; i >= 0; --i) {
			int start = (order[i] - L + s.length()) % s.length();
			int cl = mClass[start];
			--count[cl];
			newOrder[count[cl]] = start;
		}
		return newOrder;
	}
	
	int[] updateClasses(int[] newOrder, int[] mClass, int L) {
		int n = newOrder.length;
		int[] newClass = new int[n];
		newClass[newOrder[0]] = 0;
		for(int i = 1; i < n; ++i) {
			int cur = newOrder[i];
			int prev = newOrder[i - 1];
			int mid = (cur + L) % n;
			int midPrev = (prev + L) % n;
			
			if(mClass[cur] != mClass[prev] || mClass[mid] != mClass[midPrev]) {
				newClass[cur] = newClass[prev] + 1;
			} else {
				newClass[cur] = newClass[prev];
			}
		}
		return newClass;
	}

    // Build suffix array of the string text and
    // return an int[] result of the same length as the text
    // such that the value result[i] is the index (0-based)
    // in text where the i-th lexicographically smallest
    // suffix of text starts.
    public int[] computeSuffixArray(String s) {
        int[] order = sortCharacters(s);
		int[] mClass = computeCharClasses(s, order);
		
		int L = 1;
		
		while(L < s.length()) {
			order = sortDoubled(s, L, order, mClass);
			mClass = updateClasses(order, mClass, L);
			L = 2*L;
		}
		return order;
    }


    static public void main(String[] args) throws IOException {
        new SuffixArrayLong().run();
    }

    public void print(int[] x) {
        for (int a : x) {
            System.out.print(a + " ");
        }
        System.out.println();
    }

    public void run() throws IOException {
        FastScanner scanner = new FastScanner();
        String text = scanner.next();
        int[] suffix_array = computeSuffixArray(text);
        print(suffix_array);
    }
}

public class WeekFour {
	
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
	
	int lcpOfSuffixes(String s, int i, int j, int equal) {
		int lcp = Math.max(0, equal);
		while(i + lcp < s.length() && j + lcp < s.length()) {
			if(s.charAt(i + lcp) == s.charAt(j + lcp)) {
				++lcp;
			} else {
				break;
			}
		}
		return lcp;
	}
	
	int[] invertSuffixArray(int[] order) {
		int[] pos = new int[order.length];
		for(int i = 0; i< pos.length - 1; ++i) {
			pos[order[i]] = i;
		}
		return pos;
	}
	
	int[] computeLCPArray(String s, int[] order) {
		int[] lcpArray = new int[s.lenght() - 1];
		int lcp = 0;
		int[] posInOrder = invertSuffixArray(order);
		int suffix = order[0];
		for(int i = 0; i < s.length(); ++i) {
			int orderIndex = posInOrder[suffix];
			if(orderIndex == s.length() - 1) {
				lcp = 0;
				suffix = (suffix + 1) % s.length();
				continue;
			}
			int nextSuffix = order[orderIndex + 1];
			lcp = lcpOfSuffixes(s, suffix, nextSuffix, lcp - 1);
			lcpArray[orderIndex] = lcp;
			suffix = (suffix + 1) % s.length();
		}
		return lcpArray;
	}
	
	SuffixTreeNode createNewLeaf(SuffixTreeNode node, Strings s, int suffix) {
		SuffixTreeNode leaf = new SuffixTreeNode(new HashMap<>(), node, s.length() - suffix, suffix + node.stringDepth, s.length() - 1);
			node.children.put(s.charAt(leaf.edgeStart), leaf);
			return leaf;
	}
	
	SuffixTreeNode breakEdge(SuffixTreeNode node, String s, int start, int offset) {
		char startChar = s.charAt(start);
		char midChar = s.charAt(start + offset);
		SuffixTreeNode midNode = new SuffixTreeNode(new HashMap<>(), node, node.stringDepth + offset, start, start + offset - 1);
		midNode.children.put(midChar, node.children.get(startChar));
		node.children.get(startChar).parent = midNode;
		node.children.get(startChar).edgeStart = start + offset;
		node.children.put(startChar, midNode);
		return midNode;
	}
	
	SuffixTreeNode stFromSA(String s, int[] order, int[] lcpArray) {
		SuffixTreeNode root;
		int lcpPrev = 0;
		SuffixTreeNode currNode = root;
		for(int i = 0; i < s.length() - 1; ++i) {
			int suffix = order[i];
			while(currNode.stringDepth > lcpPrev) {
				currNode = currNode.parent;
			}
			if(currNode.stringDepth == lcpPrev) {
				currnode = createNewLeaf(currNode, s, suffix);
			} else {
				int edgeStart = order[i - 1] + currNode.stringDepth;
				int offset = lcpPrev - currNode.stringDepth;
				SuffixTreeNode midNode = brakeEdge(currNode, s, edgeStart, offset);
				currNode = createNewLeaf(midNode, s, suffix);
			}
			if(i < s.length() - 1) {
				lcpPrev = lcpArray[i];
			}
		}
		return root;
	}
	
	private static class SuffixTreeNode {
		SuffixTreeNode parent;
		Map<Character, SuffixTreeNode> children;
		int stringDepth;
		int edgeStart;
		int edgeEnd;
		
		SuffixTreeNode() {
			this.children = new HashMap<>();
			this.parent = null;
			this.stringDepth = 0;
			this.edgeStart = -1;
			this.edgeEnd = -1;
		}
		
		SuffixTreeNode(Map<Character, SuffixTreeNode> children, SuffixTreeNode parent, int stringDepth, int edgeStart, int edgeEnd) {
			this.children = children;
			this.parent = parent;
			this.stringDepth = stringDepth;
			this.edgeStart = edgeStart;
			this.edgeEnd = edgeEnd;
		}
	}
}
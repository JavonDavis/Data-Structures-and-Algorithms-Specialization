import java.util.*;
import java.io.*;
import java.util.zip.CheckedInputStream;

public class SuffixTree {
	
	private Node root;

	    SuffixTree() {
	        setRoot(new Node());
	    }

	    Node getRoot() {
	        return root;
	    }

	    void setRoot(Node root) {
	        this.root = root;
	    }

	    static SuffixTree build(String text) {
	        SuffixTree suffixTree = new SuffixTree();
	        suffixTree.addSuffix(text, 0);

	        return suffixTree;
	    }

	    void addSuffix(String text, int startIndex) { // Recursively add a suffix and all it's suffixes
			int index = startIndex;
	        String suffix = text.substring(startIndex);
	        if(suffix.length() == 0) {
	            return;
	        }

	        Node curr = root;
	        Node next = curr.getChildNodePartialMatchingString(text, suffix);

	        while(true) {

	            if(next == null) {
	                Node branch = new Node(startIndex, suffix.length());
	                curr.addChild(branch);
	                break;
	            }

	            int j = 0;
	            for(int i = next.getStartIndex(); i < next.getStartIndex() + next.getLength(); i++) {
	                if(text.charAt(i) != suffix.charAt(j)) {
	                    break;
	                }
	                j++;
	            }

	            if(j == next.getLength()) {
	                if(j == suffix.length()) {
	                    break;
	                }
	                curr = next;
	                startIndex += j;
	                suffix = suffix.substring(j);
	                next = curr.getChildNodePartialMatchingString(text, suffix);
	            } else {
	                Node branch1 = new Node(text.length() - suffix.length() + j, suffix.length()-j);
	                Node branch2 = new Node(next.getStartIndex() + j, next.getLength() - j);
					branch2.setChildren(next.getChildren());
					next.setChildren(new HashSet<>());
	                next.setLength(j);
	                next.addChild(branch1);
	                next.addChild(branch2);
	                break;
	            }

	        }

	        addSuffix(text, index + 1);

	    }

	    static class Node {
	        int startIndex;
	        int length;

	        Set<Node> children;

	        Node() { // Used when creating the root
	            setStartIndex(-1);
	            setLength(-1);
	            setChildren(new HashSet<>());
	        }

	        Node(int startIndex, int length) {
	            setStartIndex(startIndex);
	            setLength(length);
	            setChildren(new HashSet<>());
	        }

	        int getStartIndex() {
	            return startIndex;
	        }

	        void setStartIndex(int startIndex) {
	            this.startIndex = startIndex;
	        }

	        int getLength() {
	            return length;
	        }

	        void setLength(int length) {
	            this.length = length;
	        }

	        Set<Node> getChildren() {
	            return children;
	        }

	        void setChildren(Set<Node> children) {
	            this.children = children;
	        }

	        Node getChildNodePartialMatchingString(String text, String entry) {

	            for(Node n: children) {
	                if(text.charAt(n.getStartIndex()) == entry.charAt(0)) {
	                    return n;
	                }
	            }
	            return null;
	        }

	        void addChild(Node n) {
	            this.children.add(n);
	        }

	        void printChildren(String text) {
	            for(Node child: getChildren()) {
	                System.out.println(text.substring(child.getStartIndex(), child.getStartIndex() + child.getLength()));
	            }
	        }

	        static void printPath(String text, Node curr) {
	            if(curr != null) {
	                if (curr.hasChildren()) {
	                    curr.printChildren(text);
	                    for (Node child : curr.getChildren()) {
	                        printPath(text, child);
	                    }
	                }
	            }
	        }

	        private boolean hasChildren() {
	            return children.size()>0;
	        }
	    }

	    // public static void main(String[] args) {
 // 	        String[] patterns = new String[]{"banana", "anas", "bandana", "apple", "app", "bar", "bank"};
 //
 // 	        String text = "BOBBY#BOSTON";
 // 	        SuffixTree tree = SuffixTree.build(text);
 // 	//        tree.getRoot().printChildren(text);
 // 	        Node.printPath(text,tree.getRoot());
 // 	    }
 //
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

    static public void main(String[] args) throws IOException {
        new SuffixTree().run();
    }


    public void run() throws IOException {
        FastScanner scanner = new FastScanner();
        String text = scanner.next();
        SuffixTree tree = SuffixTree.build(text);
		Node.printPath(text,tree.getRoot());
    }
}

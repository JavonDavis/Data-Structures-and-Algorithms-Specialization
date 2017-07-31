import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Created by Javon Davis on 7/30/17.
 */
public class Trie {
    int count = 1;

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

    private Node root;

    Trie() {
        setRoot(new Node());
    }

    Node getRoot() {
        return root;
    }

    private void setRoot(Node root) {
        this.root = root;
    }

    static Trie build(String[] patterns) {
        Trie trie = new Trie();
        for(String pattern: patterns) {
            trie.addPattern(pattern);
        }
        return trie;
    }

    void addPattern(String pattern) {
        Node curr = root;
        for(int i = 0; i < pattern.length(); i ++) {
            String currentSymbol = String.valueOf(pattern.charAt(i));
            Node tmp = curr.getChild(currentSymbol);
            if (tmp != null) {
                curr = tmp;
            } else {
                curr.addChild(currentSymbol, count);
                count += 1;
                curr = curr.getChild(currentSymbol);
            }
        }
        curr.setLeaf(true);
    }

    static void prefixTrieMatching(String text, int startIndex, Trie trie) {
        String symbol = String.valueOf(text.charAt(startIndex));
        Node v = trie.getRoot();
        int currIndex = startIndex;
        while(true) {
            Node w = v.getChild(symbol);
            if(v.isLeaf()) {
//                System.out.println("Matched: " +text.substring(startIndex, currIndex));
                System.out.print(startIndex + " ");
//                if(w != null) {
//                    currIndex += 1;
//                    symbol = String.valueOf(text.charAt(currIndex));
//                    v = w;
//                    continue;
//                }
                return;
            } else if(w != null) {
                v = w;
                currIndex += 1;
                if(currIndex >= text.length())
                    if(v.isLeaf())
                        continue;
                    else
                        return;
                symbol = String.valueOf(text.charAt(currIndex));

            } else {
//                System.out.println("No matches found");
                return;
            }
        }
    }

    static void trieMatching(String text, Trie trie) {
        int start = 0;
        int end = text.length();

        while(start < end) {
            prefixTrieMatching(text, start, trie);
            start += 1;
        }
    }

    static class Node {
        private String symbol;
        private int key;
        private Set<Node> children;
        private boolean isLeaf;

        Node() { // Used when creating the root node
            setKey(0);
            setSymbol(null);
            setChildren(new HashSet<>());
        }

        Node(String symbol, int key) {
            setKey(key);
            setSymbol(symbol);
            setChildren(new HashSet<>());
        }

        String getSymbol() {
            return symbol;
        }

        void setSymbol(String symbol) {
            this.symbol = symbol;
        }

        Set<Node> getChildren() {
            return children;
        }

        void setChildren(Set<Node> children) {
            this.children = children;
        }

        boolean hasChildren() {
            return getChildren().size() > 0;
        }

        void setLeaf(boolean leaf) {
            isLeaf = leaf;
        }

        boolean isLeaf() {
            return this.isLeaf;
        }

        int getKey() {
            return key;
        }

        void setKey(int key) {
            this.key = key;
        }

        void addChild(String symbol, int i) {
            this.children.add(new Node(symbol, i));
        }

        Node getChild(String symbol) { // O(|alphabet of trie|)
            for(Node child : getChildren()) {
                if(child.getSymbol().equals(symbol)) {
                    return child;
                }
            }
            return null;
        }

        void printChildren() {
            for(Node child: getChildren()) {
                System.out.println(getKey() + "->" + child.getKey() + ":" + child.getSymbol());
            }
            // System.out.println();
        }

        static void printPath(Node curr) {
            if(curr != null) {
                if (curr.hasChildren()) {
                    curr.printChildren();
                    for (Node child : curr.getChildren()) {
                        printPath(child);
                    }
                }
            }
        }

    }

    public static void main(String[] args) {
        try {
            new Trie().run();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void run() throws IOException {
        FastScanner scanner = new FastScanner();
        String text = scanner.next();
        int patternsCount = scanner.nextInt();
        String[] patterns = new String[patternsCount];
        for (int i = 0; i < patternsCount; ++i) {
            patterns[i] = scanner.next();
        }
        Trie trie = Trie.build(patterns);
        trieMatching(text, trie);
//        Node.printPath(trie.root);
    }
}

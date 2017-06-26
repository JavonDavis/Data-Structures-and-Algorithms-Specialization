import java.util.*;
import java.io.*;

public class tree_height {
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

    public class Node {
        int parent;
        List<Node> children = new ArrayList<Node>();
        int height;

        public Node(int parent) {
            this.parent = parent;
        }
    }

	public class TreeHeight {
		int n;
		int parent[];

		void read() throws IOException {
			FastScanner in = new FastScanner();
			n = in.nextInt();
			parent = new int[n];
			for (int i = 0; i < n; i++) {
				parent[i] = in.nextInt();
			}
		}

        int height(Node root, Node[] nodes) {
            int max = 1;
            Queue<Node> q = new LinkedList<Node>();
            root.height = 1;
            Iterator<Node> iterator = root.children.iterator();
            while(iterator.hasNext()) {
                q.add(iterator.next());
            }

            while(!q.isEmpty()) {
                Node node = q.remove();
                node.height = nodes[node.parent].height + 1;
                if(node.height > max) {
                    max = node.height;
                }

                iterator = node.children.iterator();
                while(iterator.hasNext()) {
                    q.add(iterator.next());
                }
            }

            return max;
        }

		int computeHeight() {
            Node root = new Node(-2);
            Node[] nodes = new Node[n];
            for(int i = 0; i < n; i ++) {
                nodes[i] = new Node(parent[i]);
            }

            Node node;
            for(int i = 0; i < n; i ++) {
                node = nodes[i];
                if (node.parent == -1) {
                    root = node;
                } else {
                    nodes[node.parent].children.add(node);
                }
            }
            if(root.parent != -2)
			    return height(root, nodes);
            else
                return 0;
		}
	}

	static public void main(String[] args) throws IOException {
            new Thread(null, new Runnable() {
                    public void run() {
                        try {
                            new tree_height().run();
                        } catch (IOException e) {
                        }
                    }
                }, "1", 1 << 26).start();
	}
	public void run() throws IOException {
		TreeHeight tree = new TreeHeight();
		tree.read();
		System.out.println(tree.computeHeight());
	}
}

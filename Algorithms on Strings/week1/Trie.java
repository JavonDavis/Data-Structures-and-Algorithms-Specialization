import java.util.*;

public class Trie {
	
	
	static class Node {
		String symbol;
		Set<Node> children;
		
		Node() {
			setSymbol(null);
			setChildren(null);
		}

		Node(String symbol) {
			setSymbol(symbol);
			setChildren();
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
	}

	public static void main(String[] args) {

	}
}
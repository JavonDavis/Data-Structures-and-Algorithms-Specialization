public class KnuthMorrisPratt {
	
	int[] computePrefixFunction(String pattern) {
		int[] result = new int[pattern.length()];
		result[0] = 0;
		int border = 0;
		for(int i = 1; i < pattern.length(); ++i) {
			while(border > 0 && pattern.charAt(i) != pattern.charAt(border)) {
				border = result[border - 1];
			}
			
			if(pattern.charAt(i) == pattern.charAt(border)) {
				++border;
			} else {
				border = 0;
			}
			result[i] = border;
		}
		return result;
	}
	
	List<Integer> findAllOccurrences(String pattern, String text) {
		String s = pattern + "$"+text;
		int[] prefixFunction = computePrefixFunction(s);
		List<Integer> result = new ArrayList<>();
		for(int i = pattern.length() + 1; i < s.length(); ++i) {
			if(prefixFunction[i] == pattern.length()) {
				result.add(i - 2*pattern.length());
			}
		}
		return result;
	}
}
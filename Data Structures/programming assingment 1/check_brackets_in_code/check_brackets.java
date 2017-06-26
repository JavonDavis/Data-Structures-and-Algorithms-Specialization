import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

class Bracket {
    Bracket(char type, int position) {
        this.type = type;
        this.position = position;
    }

    boolean Match(char c) {
        if (this.type == '[' && c == ']')
            return true;
        if (this.type == '{' && c == '}')
            return true;
        if (this.type == '(' && c == ')')
            return true;
        return false;
    }

    boolean closing() {
        return this.type == ']' || this.type == '}' || this.type == ')';
    }
    char type;
    int position;
}

class check_brackets {
    public static void main(String[] args) throws IOException {
        InputStreamReader input_stream = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input_stream);
        String text = reader.readLine();

        Stack<Bracket> opening_brackets_stack = new Stack<Bracket>();
        for (int position = 0; position < text.length(); ++position) {
            char next = text.charAt(position);

            if (next == '(' || next == '[' || next == '{') {
                opening_brackets_stack.push(new Bracket(next, position + 1));
            }

            if (next == ')' || next == ']' || next == '}') {
                if(opening_brackets_stack.empty()) {
                    opening_brackets_stack.push(new Bracket(next, position + 1));
                    break;
                }
                Bracket bracket = opening_brackets_stack.peek();
                if(bracket.Match(next)) {
                    opening_brackets_stack.pop();
                } else {
                    opening_brackets_stack.push(new Bracket(next, position + 1));
                }
            }
        }

        if(opening_brackets_stack.empty()) {
            System.out.println("Success");
        } else {
            Integer last_closing = null;
            Integer last_opening = null;
            while(!opening_brackets_stack.empty()) {
                Bracket el = opening_brackets_stack.pop();

                if(el.closing()) {
                    if (last_closing == null) {
                        last_closing = el.position;
                    } else {
                        if(el.position < last_closing) {
                            last_closing = el.position;
                        }
                    }

                } else {
                    if (last_opening == null) {
                        last_opening = el.position;
                    } else {
                        if(el.position < last_opening) {
                            last_opening = el.position;
                        }
                    }
                }

            }
            if(last_closing != null) {
                System.out.println(last_closing);
            } else {
                System.out.println(last_opening);
            }
        }

    }
}

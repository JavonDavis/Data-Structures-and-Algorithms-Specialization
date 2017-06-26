import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

class Request {
    public Request(int arrival_time, int process_time) {
        this.arrival_time = arrival_time;
        this.process_time = process_time;
    }

    public int arrival_time;
    public int process_time;
}

class Response {
    public Response(boolean dropped, int start_time) {
        this.dropped = dropped;
        this.start_time = start_time;
    }

    public boolean dropped;
    public int start_time;
}

class Buffer {
    public Buffer(int size) {
        this.size_ = size;
        this.finish_time_ = new ArrayList<Integer>();
    }

    public Response Process(Request request) {
        // write your code here
        Response response;
        int last;
        if(finish_time_.size() > 0) {
            int current = finish_time_.get(0);
            if(request.arrival_time < current) {
                if(finish_time_.size() == size_) {
                    response = new Response(true, -1);
                } else {
                    last = finish_time_.get(finish_time_.size() - 1);
                    response = new Response(false, last);
                    current_time = last + request.process_time;
                    finish_time_.add(current_time);
                }
            } else {
                last = finish_time_.get(finish_time_.size() - 1);
                finish_time_.remove(0); // Order n - If too slow switch out with LinkedList
                if(last < request.arrival_time) {
                    last = request.arrival_time;
                }
                response = new Response(false, last);
                current_time = last + request.process_time;
                finish_time_.add(current_time);
            }
        } else {
            if(current_time < request.arrival_time) {
                current_time = request.arrival_time;
            }
            response = new Response(false, current_time);
            finish_time_.add(current_time + request.process_time);
        }
        return response;
    }

    private int size_;
    private ArrayList<Integer> finish_time_;
    private int current_time = 0;
    private int current_size = 0;
}

class process_packages {
    private static ArrayList<Request> ReadQueries(Scanner scanner) throws IOException {
        int requests_count = scanner.nextInt();
        ArrayList<Request> requests = new ArrayList<Request>();
        for (int i = 0; i < requests_count; ++i) {
            int arrival_time = scanner.nextInt();
            int process_time = scanner.nextInt();
            requests.add(new Request(arrival_time, process_time));
        }
        return requests;
    }

    private static ArrayList<Response> ProcessRequests(ArrayList<Request> requests, Buffer buffer) {
        ArrayList<Response> responses = new ArrayList<Response>();
        for (int i = 0; i < requests.size(); ++i) {
            responses.add(buffer.Process(requests.get(i)));
        }
        return responses;
    }

    private static void PrintResponses(ArrayList<Response> responses) {
        for (int i = 0; i < responses.size(); ++i) {
            Response response = responses.get(i);
            if (response.dropped) {
                System.out.println(-1);
            } else {
                System.out.println(response.start_time);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        int buffer_max_size = scanner.nextInt();
        Buffer buffer = new Buffer(buffer_max_size);

        ArrayList<Request> requests = ReadQueries(scanner);
        ArrayList<Response> responses = ProcessRequests(requests, buffer);
        PrintResponses(responses);
    }
}

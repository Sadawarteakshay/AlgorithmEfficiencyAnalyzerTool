import http.server
import socketserver
import urllib.parse
import time

class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = urllib.parse.parse_qs(post_data)

        numbers = parsed_data.get('numbers', [''])[0].split(',')
        numbers = [int(num.strip()) for num in numbers if num.strip()]

        selected_algorithms = []
        sorting_algorithms = {
            'bubble_sort': self.bubble_sort,
            'merge_sort': self.merge_sort,
            'insertion_sort': self.insertion_sort
        }

        for algorithm in sorting_algorithms.keys():
            if algorithm in parsed_data:
                selected_algorithms.append(algorithm)

        analysis_results = []
        for algorithm in selected_algorithms:
            start_time = time.time()
            sorted_numbers = sorting_algorithms[algorithm](numbers.copy())
            end_time = time.time()
            time_complexity = end_time - start_time
            analysis_results.append((algorithm.capitalize(), sorted_numbers, time_complexity))

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        title = "Algorithm Efficiency Analyzer Tool"
        message = f"<h1>{title}</h1>"
        message += f"<p>Input Numbers: {numbers}</p>"

        if analysis_results:
            message += "<h2>Analysis Results:</h2>"
            for result in analysis_results:
                algo_name, sorted_numbers, time_complexity = result
                message += f"<h3>{algo_name}:</h3>"
                message += f"<p>Sorted Numbers: {sorted_numbers}</p>"
                message += f"<p>Time Complexity: {time_complexity} seconds</p>"

        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, 'Page Not Found')

    def bubble_sort(self, arr):
        # Bubble Sort implementation
        return arr

    def merge_sort(self, arr):
        # Merge Sort implementation
        return arr

    def insertion_sort(self, arr):
        # Insertion Sort implementation
        return arr

PORT = 8000
Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

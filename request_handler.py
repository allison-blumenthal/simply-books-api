from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_authors, get_single_author, get_all_books, get_single_book
import json

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/authors/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /authors
        except ValueError:
            pass  # Request had trailing slash: /authors/

        return (resource, id)  # This is a tuple
    

    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


    def do_GET(self):
        """Handles GET requests to the server
        """
        self._set_headers(200)
        response = {} # Default response
        
         # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "authors":
          if id is not None:
            response = get_single_author(id)
            
          else:
            response = get_all_authors()

        self.wfile.write(json.dumps(response).encode())
        
        if resource == "books":
          if id is not None:
            response = get_single_book(id)
            
          else:
            response = get_all_books()
            
        self.wfile.write(json.dumps(response).encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server
        """
        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = f"received post request:<br>{post_body}"
        self.wfile.write(response.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self.do_POST()


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()

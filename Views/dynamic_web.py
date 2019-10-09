from http.server import HTTPServer, BaseHTTPRequestHandler
from connect_to_db import *
def render_people():
    people_html = ""
    peopleFromDB = getAllDataFromDbTable("person")
    for person in peopleFromDB:
        people_html += f'<tr><td>{person["person_id"]}</td><td>{person["first_name"]}</td><td>{person["last_name"]}</td><td>{person["email"]}</td></tr>'
    return people_html

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Tell the client we're about to send HTML content in our HTTP payload
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # Produce the HTML

        html_document = f"""
<!doctype html>
<html>
 <head>
    <title>Flask app</title>
  </head>
    <body>
        <p>Available drinks:</p>
        <table >
          <tr>
            <th>ID</th>
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Email</th>
          </tr>
          {render_people()}
        </table>
    </body>
</html>
"""
        # Render and send response
        self.wfile.write(html_document.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', 8088)
    httpd = HTTPServer(server_address, Handler)
    print("Starting server")
    httpd.serve_forever()
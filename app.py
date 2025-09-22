from http.server import BaseHTTPRequestHandler, HTTPServer
import os


# Путь к HTML-файлу
HTML_FILE = "contacts.html"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Игнорирование favicon.ico
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        # Проверка, существует ли HTML-файл
        if not os.path.exists(HTML_FILE):
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1>Файл не найден</h1>".encode("utf-8"))
            return

        # Чтение содержимого HTML-файла
        with open(HTML_FILE, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Отправка ответа
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()

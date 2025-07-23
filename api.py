import socketserver
import datetime

class GPSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        timestamp = datetime.datetime.now().isoformat()
        print(f"[{timestamp}] Pacote recebido de {self.client_address[0]}: {data.decode()}")

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 5000
    with socketserver.TCPServer((HOST, PORT), GPSHandler) as server:
        print(f"Servidor TCP rodando em {HOST}:{PORT}")
        server.serve_forever()

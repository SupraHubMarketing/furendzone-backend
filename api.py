import socketserver
import datetime
import os

# Usa a porta fornecida pelo Railway ou 5000 como fallback local
PORT = int(os.environ.get("PORT", 5000))
HOST = "0.0.0.0"

class GPSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        timestamp = datetime.datetime.now().isoformat()
        print(f"[{timestamp}] Pacote recebido de {self.client_address[0]}: {data.decode(errors='ignore')}")

if __name__ == "__main__":
    try:
        with socketserver.TCPServer((HOST, PORT), GPSHandler) as server:
            print(f"Servidor TCP rodando em {HOST}:{PORT}")
            server.serve_forever()
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")

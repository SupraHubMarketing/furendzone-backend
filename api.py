
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'GPS Server Running'

@app.route('/api/gps', methods=['POST'])
def receive_gps_data():
    try:
        data = request.get_json()
        device_id = data.get('device_id')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        timestamp = data.get('timestamp', datetime.datetime.now().isoformat())
        # Aqui você poderia salvar no banco de dados se quiser
        print(f"[{timestamp}] Device {device_id} - Lat: {latitude}, Lon: {longitude}")
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

@app.route('/predict', methods=['POST','GET'])
def predict():
    # Dummy model: echoes input or returns fixed prediction
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        return jsonify({'prediction': 'dummy', 'input': data})
    return jsonify({'prediction': 'dummy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

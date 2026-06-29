from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Sample data to return
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(data)
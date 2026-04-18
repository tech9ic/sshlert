import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify
from flask_cors import CORS
from backend.output.generator import process_pipeline

app = Flask(__name__)
# Enable CORS for local testing with generic HTML
CORS(app)

@app.route('/process-alerts', methods=['GET'])
def get_alerts():
    try:
        data = process_pipeline()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)

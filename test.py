from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():

    response = requests.get("https://sheetdb.io/api/v1/cwho1fbb3bjzn")
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to retrieve data"}), 500

if __name__ == '__main__':
    app.run(debug=True)

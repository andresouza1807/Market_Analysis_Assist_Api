from data_exchange import get_data_collect, prepare_data
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Forex API</h1>'''

@app.route('/data', methods=['GET'])
def get_data():
    try:
        data = get_data_collect()
        prepraed_data = prepare_data(data)
        return jsonify(prepraed_data)
    except ValueError as e:
        return jsonify({'error': str(e)}), 500
    
    
if __name__ == '__main__':
    app.run(debug=True)
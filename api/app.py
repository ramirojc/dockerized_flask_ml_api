from flask import Flask, jsonify, request
import json
import pickle
from pathlib import Path

app = Flask(__name__)

model_path = Path('./api/models/model.pkl')

with model_path.open('rb') as f:
    model = pickle.load(f)

@app.route('/')
def check():
    return jsonify(f'Server Alive, Model Info: {str(model)}')

@app.route('/loaneval')
def loaneval():
    input = json.loads(request.data)["data"]
    print(input)
    return jsonify(str(model.predict(input)))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
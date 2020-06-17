from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/')
def index(methods=['GET']):
    return jsonify({'data':'hha'})

if __name__ == '__main__':
    app.run(debug=True)

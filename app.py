from flask import Flask, jsonify
import pickle as pk

app = Flask(__name__)

with open('data.pkl','rb') as load:
	arts = pk.load(load)

@app.route('/api/')
def index(methods=['GET']):
    return jsonify({'arts':arts})

@app.route('/api/user')
def user(methods=['GET']):
	return jsonify({'data':'user'})


if __name__ == '__main__':
    app.run(debug=True)

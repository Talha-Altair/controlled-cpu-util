from flask import *
from cpu_stress import stress

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():

    return jsonify({"ping":"pong"})

if __name__ == '__main__':

	app.run(host='0.0.0.0', port=8080, debug=True)

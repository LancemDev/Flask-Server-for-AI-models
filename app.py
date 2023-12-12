from flask import Flask, request, jsonify
import model

app = Flask(__name__)

@app.route('/api/prediction', methods=['POST'])
def get_prediction():
    data = request.get_json()
    prediction = model.predict(data)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
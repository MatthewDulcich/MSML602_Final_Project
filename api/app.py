from flask import Flask, jsonify, request, render_template, redirect
from modules_scripts.preprocessing import predict_pipeline
from flask_cors import CORS

app = Flask(__name__, template_folder='./webpage', static_folder='./webpage')
CORS(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text sent'})
    
    #sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions) #predictions[0]
    except TypeError as e:
        return jsonify({'error': str(e)})
    return result


if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False, port=5001)
    app.run()

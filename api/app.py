from flask import Flask, jsonify, request, render_template, redirect
from modules_scripts.preprocessing import predict_pipeline
from modules_scripts.graphs import plot_histogram
from flask_cors import CORS
import pandas as pd

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

@app.route('/display')
def display_table():
    # Assuming the CSV file is in the 'data' folder relative to the script
    file_path = 'data/google_play_apps.csv'

    # Read the CSV file using pandas
    df = pd.read_csv(file_path)
    # print(df).head()

    # Convert DataFrame to an HTML table
    html_table = df.to_html(classes="table table-striped", index=False)

    # Render the HTML table within a template
    return render_template('table_display.html', table=html_table)

@app.route('/graphing')
def graph():
    
    # html_graph = plot_histogram()

    # Render the HTML table within a template
    return render_template('interactive_plot.html')


if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False, port=5001)
    app.run()

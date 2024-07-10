from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the data
data = pd.read_csv(r'C:\Users\VENKATA SURYA\OneDrive\Documents\SOCR-HeightWeight.csv')

# Function to convert height in feet to cm and find weight in kg
def get_weight(height_ft):
    height_cm = height_ft * 30.48
    closest_match = data.iloc[(data['Height(Inches)']*2.54 - height_cm).abs().argmin()]
    weight_kg = closest_match['Weight(Pounds)'] * 0.453592
    return weight_kg

@app.route('/', methods=['GET', 'POST'])
def index():
    weight = None
    if request.method == 'POST':
        height_ft = float(request.form['height'])
        weight = get_weight(height_ft)
    return render_template('index.html', weight=weight)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('./constituents-financials_csv.csv')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/Sector')
def list_unique_sectors():
    unique_sectors = df['Sector'].unique().tolist()
    return jsonify(unique_sectors)

@app.route('/EBITDA')
def get_ebitda_by_sector():
    sector = request.args.get('Sector')
    if not sector:
        return "There is no query string provided", 400
    ebitda_values = df[df['Sector'] == sector]['EBITDA'].dropna().tolist()
    return jsonify(ebitda_values)

if __name__ == '__main__':
    app.run(port=5000)

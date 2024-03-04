from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", matches=None)

@app.route('/result', methods=['POST'])
def result():
    regex_exp = request.form['regex_exp']
    text_data = request.form['text_data']
    
    matches = re.findall(regex_exp, text_data)
    num_matches = len(matches)
    
    return render_template('index.html', matches=matches,num_matches=num_matches)

if __name__ == '__main__':
    app.run(debug=True)

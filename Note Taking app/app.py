# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        note = request.form.get('note')
        if note:
            notes.append(note)
    return render_template("home.html", notes_with_index=enumerate(notes))

@app.route('/clear')
def clear():
    notes.clear()
    return render_template('home.html', notes_with_index=enumerate(notes))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(notes):
        del notes[index]
    return render_template('home.html', notes_with_index=enumerate(notes))

if __name__ == "__main__":
    app.run(debug=True)

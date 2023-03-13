from flask import Flask
from flask import request
from flask import render_template
from functions import *

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        length = request.form['length']

        try:
            uppercase = request.form['uppercase']
        except:
            uppercase = False

        try:
            lowercase = request.form['lowercase']
        except:
            lowercase = False

        try:
            numbers = request.form['numbers']
        except:
            numbers = False

        try:
            special = request.form['special']
        except:
            special = False

        password = generate_password(int(length), bool(uppercase), bool(lowercase), bool(numbers), bool(special))
        return render_template('result.html', password=password)

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
    
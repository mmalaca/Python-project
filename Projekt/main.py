from flask import Flask, render_template


app= Flask(__name__,template_folder='strona',static_folder='css')

@app.route('/')
def index():
    return render_template('strona.html')

@app.route('/samochody.html')
def samochody():
    return render_template('samochody.html')

@app.route('/czesci.html')
def czesci():
    return render_template('czesci.html')

@app.route('/motocykle.html')
def motocykle():
    return render_template('motocykle.html')
@app.route('/strona.html')
def strona():
    return render_template('strona.html')
if __name__ =='__main__':
    app.run(debug=True)

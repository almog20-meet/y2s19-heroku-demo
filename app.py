from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home2.html')

@app.route('/dad')
def dad():
    return render_template('dad.html')

@app.route('/mom')
def mom():
    return render_template('mom.html')

@app.route('/dog')
def dog():
    return render_template('dog.html')

@app.route('/brother')
def brother():
    return render_template('brother.html')

@app.route('/sister')
def sister():
    return render_template('sister.html')


if __name__ == '__main__':
    app.run(debug=True)


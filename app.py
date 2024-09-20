from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cv')
def cv():
    return render_template('CV.html')

@app.route('/research')
def research():
    return render_template('research.html')

if __name__ == '__main__':
    app.run(debug=True)
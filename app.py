from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Here, you could perform any backend tasks, like saving to a database
    return f'Thank you, {name}! Your email ({email}) has been submitted.'

if __name__ == '__main__':
    app.run(debug=True)

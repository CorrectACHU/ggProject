from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('start.html')


@app.route('/authorization/')
def enter_the_matrix():
    return render_template('enter_form.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

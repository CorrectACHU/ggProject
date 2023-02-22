import os
from full_of_bot.selenium_scripts.main import get_filters, get_driver
from flask import Flask, render_template, request, flash, session, redirect, url_for

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'FuturamaNaDyatlahprikinxDDD:s'


@app.route('/')
def hello_world():
    return render_template('start.html', title='START PAGE')


@app.route('/login/', methods=['POST', 'GET'])
def enter_the_matrix():
    session['customer'] = {}
    session['filters'] = {}
    if request.method == 'POST':
        if request.form['email'] and request.form['password']:
            flash('Data was send', category='success')
            e, p = request.form['email'], request.form['password']
            session['customer'] = {'email': e, 'pass': p}
            return redirect(url_for('wait_page'))
        else:
            flash('Data was not send', category='error')

    return render_template('login.html', title='LOGIN MY FRIEND')


@app.route('/wait_page/')
def wait_page():
    if not session['filters']:
        driver = get_driver(session['customer']['email'], session['customer']['pass'])
        filters = get_filters(driver)
        session['filters'] = {fltr: filters[fltr] for fltr in filters}
    else:
        pass
    print(session['filters'])
    return render_template('wait_page.html', title='Wait pls',
                           filters=session['filters'])


@app.errorhandler(404)
def pageNotFount(error):
    if session['customer']:
        print(session['customer'])
    return render_template('page404.html', title="Ну что , попался?"), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

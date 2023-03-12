import json
import os
from flask_restful import Api, Resource
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
from full_of_bot.selenium_scripts.main import get_filters, get_driver
from flask import Flask, request, flash, session, redirect, url_for, Response,jsonify

load_dotenv()

# app = Flask(__name__, static_folder='static')
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


class MyProject(Resource):
    def get(self):
        return {'hello': 'fucking_madness'}

    def post(self):
        d = request.get_json()
        # d = json.loads(d)
        # driver = get_driver(d['email'], d['password'])
        filters = {'Connections': ['1st', '2nd', '3rd+'],
                   'Locations': ['Poland', 'United States', 'India', 'Wielkopolskie, Poland',
                                 'Poznan Metropolitan Area'],
                   'Talks about': ['#leadership', '#marketing', '#startups', '#hiring', '#recruitment'],
                   'Current company': ['Google', 'Microsoft', 'Amazon', 'YouTube', 'LinkedIn'],
                   'Past company': ['Microsoft', 'Google', 'IBM', 'Amazon', 'Accenture'],
                   'School': ['Uniwersytet im. Adama Mickiewicza w Poznaniu',
                              'Poznan University of Economics And Business', 'Poznan University of Technology',
                              'University of Warsaw', 'SGH Warsaw School of Economics'],
                   'Industry': ['Computer Software', 'Information Technology & Services', 'Human Resources',
                                'Staffing & Recruiting', 'Internet'],
                   'Profile language': ['English', 'Polish', 'Russian', 'French', 'Spanish'],
                   'Open to': ['Pro bono consulting and volunteering', 'Joining a nonprofit board'],
                   'Service categories': ['Consulting', 'Coaching & Mentoring', 'Marketing', 'Operations',
                                          'Software Development']}
        # filters = get_filters(driver)
        # return jsonify(filters)
        return json.dumps(filters)


# @app.route('/')
# def hello_world():
#     return render_template('start.html', title='START PAGE')
#
#
# @app.route('/login/', methods=['POST', 'GET'])
# @cross_origin()
# def enter_the_matrix():
#     # session['customer'] = {}
#     # session['filters'] = {}
#     if request.method == 'POST':
#         print("hello putin")
#     #     if request.form['email'] and request.form['password']:
#     #         flash('Data was send', category='success')
#     #         e, p = request.form['email'], request.form['password']
#     #         session['customer'] = {'email': e, 'pass': p}
#     #         return redirect(url_for('wait_page'))
#     #     else:
#     #         flash('Data was not send', category='error')
#     return render_template('login.html', title='LOGIN MY FRIEND')
#
#
# @app.route('/wait_page/')
# def wait_page():
#     if not session['filters']:
#         driver = get_driver(session['customer']['email'], session['customer']['pass'])
#         filters = get_filters(driver)
#         session['filters'] = {fltr: filters[fltr] for fltr in filters}
#     else:
#         pass
#     print(session['filters'])
#     return render_template('wait_page.html', title='Wait pls',
#                            filters=session['filters'])
#
#
# @app.errorhandler(404)
# def pageNotFount(error):
#     return render_template('page404.html', title="Ну что , попался?"), 404


api.add_resource(MyProject, '/')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

dashboard = Flask(__name__)


@dashboard.route('/', methods = ['GET'])
def page():

    return render_template('page.html')


if __name__ == '__main__':

    dashboard.run(host='0.0.0.0', port=8080, debug=False)

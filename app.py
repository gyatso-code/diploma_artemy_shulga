""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    """ Эта функция  """
    return render_template('index.html')

@app.route('/ui_tests')
def ui_tests():
    """ Эта функция """
    return render_template('index.html')

@app.route('/ui_tests_header')
def ui_tests_header():
    """ Эта функция """
    return render_template('index.html')

@app.route('/ui_tests_footer')
def ui_tests_footer():
    """ Эта функция  """
    return render_template('index.html')

@app.route('/ui_tests_main_page')
def welcome():
    """ Эта функция """
    return render_template('index.html')

@app.route('/ui_tests_list_of_cars')
def ui_tests_list_of_cars():
    """ Эта функция  """
    return render_template('index.html')

@app.route('/ui_tests_registration')
def ui_tests_registration():
    """ Эта функция """
    return render_template('index.html')


@app.route('/api_tests')
def api_tests():
    """ Эта функция """
    return render_template('index.html')

@app.route('/api_tests_status_code_get')
def api_tests_status_code_get():
    """ Эта функция """
    return render_template('index.html')


@app.route('/api_tests_status_code_post')
def api_tests_status_code_post():
    """ Эта функция """
    return render_template('index.html')



@app.route('/allure_all')
def allure():
    """ Эта функция  """
    return render_template('index.html')



@app.route('/locust')
def locust():
    """ Эта функция  """
    return render_template('index.html')

@app.route('/locust_report')
def locust_report():
    """ Эта функция """
    return render_template('index.html')


# @app.route("/error")
# def error():
#     """Эта функция запуская и отвечает за процесс возврата результата test_error.html."""
#     return render_template('test_error.html')


# @app.route("/runallure")
# def run_allure():
#     """ Эта функция запуская и отвечает за генерацию отчета allure. """
#
#     cmd = ["./scriptsh/runallure.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
#
# @app.route("/run_ui")
# def run_ui():
#     """ Эта функция запуская и отвечает за тесты страницы /example. """
#
#     cmd = ["./scriptsh/run_aut_lk.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

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
    cmd = ["bash", "C:/Users/user/PycharmProjects/diploma_artemy_shulga/scripts/ui_tests.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

# @app.route('/ui_tests_header')
# def ui_tests_header():
#     """ Эта функция """
#     cmd = ["./scripts/ui_tests_header.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
# @app.route('/ui_tests_footer')
# def ui_tests_footer():
#     """ Эта функция  """
#     cmd = ["./scripts/ui_tests_footer.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
# @app.route('/ui_tests_main_page')
# def ui_tests_main_page():
#     """ Эта функция """
#     cmd = ["./scripts/ui_tests_main_page.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
# @app.route('/ui_tests_list_of_cars')
# def ui_tests_list_of_cars():
#     """ Эта функция  """
#     cmd = ["./scripts/ui_tests_list_of_cars.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
# @app.route('/ui_tests_registration')
# def ui_tests_registration():
#     """ Эта функция """
#     cmd = ["./scripts/ui_tests_registration.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
#
# @app.route('/api_tests')
# def api_tests():
#     """ Эта функция """
#     cmd = ["./scripts/api_tests.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
# @app.route('/api_tests_status_code_get')
# def api_tests_status_code_get():
#     """ Эта функция """
#     cmd = ["./scripts/api_tests_status_code_get.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
#
# @app.route('/api_tests_status_code_post')
# def api_tests_status_code_post():
#     """ Эта функция """
#     cmd = ["./scripts/api_tests_status_code_post.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
#
#
# @app.route('/allure_all')
# def allure_all():
#     """ Эта функция  """
#     cmd = ["./scripts/allure_allsh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
#
# @app.route('/locust')
# def locust():
#     """ Эта функция  """
#     cmd = ["./scripts/locust.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
# @app.route('/locust_report')
# def locust_report():
#     """ Эта функция """
#     cmd = ["./scripts/locust_report.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)


# @app.route("/error")
# def error():
#     """Эта функция запуская и отвечает за процесс возврата результата test_error.html."""
#     return render_template('test_error.html')


# @app.route("/runallure")
# def run_allure():
#     """ Эта функция запуская и отвечает за генерацию отчета allure. """
#
    # cmd = ["./scripts/runallure.sh"]
    # with subprocess.Popen(cmd, stdout=subprocess.PIPE,
    #                       stderr=subprocess.PIPE,
    #                       stdin=subprocess.PIPE,
    #                       universal_newlines=True) as result:
    #     out = result.communicate()
    # return render_template('welcome.html', text=out, json=out)
#
#
# @app.route("/run_ui")
# def run_ui():
#     """ Эта функция запуская и отвечает за тесты страницы /example. """
#
#     cmd = ["./scripts/run_aut_lk.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('welcome.html', text=out, json=out)
#
#
if __name__ == "__main__":
    app.run(debug=True)

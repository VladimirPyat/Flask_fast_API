from flask import Flask
from flask import render_template

app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'Hello world'
#
# @app.route('/about/')
# def about():
#     return 'Тут должна быть инфо обо мне'
#
# @app.route('/contact/')
# def contact():
#     return 'Тут должны быть контакты'
#
# @app.route('/summ/<int:num1>/<int:num2>')
# def summ(num1, num2):
#     result = num1+num2
#     return str(result)

# @app.route('/str_len/<some_text>')
# def summ(some_text):
#
#     return str(len(some_text))
#
# @app.route('/hello_html')
# def hello_html():
#     html_string = """
#
#     <h1> Моя первая страница HTML</h1>
#     <p> Привет привет </p>
#
#     """
#     return html_string

_users = [{'name': 'Ivan',
               'Last_name': 'Ivanov',
               'age': '44',
               'average_mark': '4.8',
               },
              {'name': 'dsfds',
               'Last_name': 'sdfg',
               'age': '44',
               'average_mark': '4.8',
               }]

_news = [{'title': 'MAIN_news',
          'content': 'sdsdfsdgsdgsgsfgsfgsfg',
          'date': '2024-02-04',
          },
         {'title': 'other_news',
          'content':'fgsfg',
          'date': '2024-02-05',
          },]

@app.route('/table/')
def table():
    return render_template('table.html', users =_users)


@app.route('/news/')
def news():
    return render_template('news.html', news =_news)




if __name__ == '__main__':
    app.run()

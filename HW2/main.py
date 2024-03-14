
from flask import Flask, render_template, request, flash, redirect, url_for, session


app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

LOGIN = 'admin'
PASSWD = '1234'


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    get_login = request.form.get('login')
    get_passwd = request.form.get('passwd')

    if get_login == LOGIN and get_passwd == PASSWD:
        return redirect(url_for('index'))
    flash('Неверный логин и/или пароль', 'warning')
    return render_template('login.html')


@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/result/')
def result(message=None):
    return render_template('result.html', message=message)

@app.route('/error/')
def error(message=None):
    return render_template('error.html', message=message)


@app.route('/task4/', methods=['POST', 'GET'])
def task4():
    if request.method == 'GET':
        return render_template('task4.html')

    get_text = request.form.get('text')
    words_count = len(get_text.split())
    message = f'Количество слов в тексте: {words_count}'

    return result(message)



@app.route('/task6/', methods=['POST', 'GET'])
def task6():
    if request.method == 'GET':
        return render_template('task6.html')
    get_name = request.form.get('name')
    get_age = request.form.get('age')

    if int(get_age) < 0 :
        return render_template('error.html', message='Возраст не может быть отрицательным')

    return result('Данные введены корректно')


@app.route('/task9/', methods=['POST', 'GET'])
def task9():
    if request.method == 'GET':
        return render_template('task9.html')
    get_name = request.form.get('username')
    get_email = request.form.get('email')

    session['username'] = get_name
    session['email'] = get_email


    return redirect(url_for('task9_result'))


@app.route('/task9_result', methods=['POST', 'GET'])
def task9_result():
    if request.method == 'GET':
        name = session.get('username')

        return render_template('task9_result.html', name=name)
    session.pop('username', None)
    session.pop('email', None)

    return redirect(url_for('task9'))



if __name__ == '__main__':
    app.run()

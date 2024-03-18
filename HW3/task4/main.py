from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import CSRFProtect

from models import *

from forms import RegistrationForm, EnterIdForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kJkUOJIUZRAYkEgFR6X52w'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_01.db'
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/add/', methods=['GET', 'POST'])
def add_db():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        db_user = UsersDB(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                          password=form.password.data)
        if is_uniq_mail(form.email.data):
            db.session.add(db_user)
            db.session.commit()
            return render_template('result.html', message='Данные введены корректно')
        return render_template('register.html', form=form, message='Пользователь с таким email уже существует')

    return render_template('register.html', form=form)


@app.route('/list/')
def list_db():
    users = UsersDB.query.all()
    return render_template('list.html', users=users)


@app.route('/del/', methods=['GET', 'POST'])
def del_db():
    form = EnterIdForm()
    if request.method == 'GET':
        return render_template('delete.html', form=form)
    get_id = request.form.get('user_id')
    user = UsersDB.query.filter_by(user_id=get_id).first()
    if user:
        return redirect(url_for('del_confirm', user_id=get_id))
    return render_template('delete.html', form=form, message='Пользователь с таким ID не найден')

@app.route('/del/confirm/', methods=['GET', 'POST'])
@csrf.exempt
def del_confirm():
    user_id = request.args.get('user_id')
    user = UsersDB.query.filter_by(user_id=user_id).first()
    message = f'Удалить пользователя? ID: {user.user_id}, Имя: {user.first_name}, Фамилия: {user.last_name}'
    if request.method == 'GET':
        return render_template('delete_conf.html', message=message, user_id=user_id)
    db.session.delete(user)
    db.session.commit()
    return render_template('result.html', message='Пользователь удален')



# flask --app  main:app init-db - запуск из командной строки
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


def is_uniq_mail(email):
    # проверка если база не заполнена
    same_mail_user = UsersDB.query.filter_by(email=email).first()
    return False if same_mail_user else True




if __name__ == '__main__':
    app.run()

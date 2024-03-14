from flask import Flask, render_template
from models import db, Students, Fags, Gender
from random import choice, randint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_01.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-user")
def add_user():
    for _ in range(1, 11):
        fag = Fags(fag_name=choice(['math', 'hist', 'lang']))
        db.session.add(fag)
    db.session.commit()

    for i in range(1, 11):
        student = Students(name=f'name{i}', last_name=f'last_name{i}', age=i+15, gender=choice([Gender.male, Gender.female]), group=choice([1, 2, 3]), fags_id=randint(1, 10))
        db.session.add(student)
    db.session.commit()


# @app.cli.command("del-user")
# def del_user():
#     user = User.query.filter_by(username='Alex').first()
#     db.session.delete(user)
#     db.session.commit()


@app.route('/')
def index():
    #print('*'*50)
    student = Students.query.all()

    return render_template('index.html', student=student)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from MyForms import PreTourForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = PreTourForm(5)
    if request.method == 'POST' and form.validate():
        data = {}
        for i in range(form.n):
            name = request.form.get(f'name_{i}')
            grade = request.form.get(f'grade_{i}')
            data[name] = grade
        pass
    return render_template('fill_form.html', form=form)


if __name__ == '__main__':
    app.run()

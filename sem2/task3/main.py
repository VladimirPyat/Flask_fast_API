from flask import Flask, render_template, request

app = Flask(__name__)

LOGIN = 'admin'
PASSWD = '1234'

@app.route ('/', methods=['POST', 'GET'])
def login ():
    if request.method=='GET':
        return render_template('login.html')
    get_login=request.form.get('login')
    get_passwd=request.form.get('passwd')

    if get_login==LOGIN and get_passwd==PASSWD:
        return render_template('index.html')
    return render_template('error.html')


if __name__ == '__main__':
    app.run()
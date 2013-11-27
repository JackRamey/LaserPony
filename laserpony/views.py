from flask import redirect, render_template, request, url_for
from flask.views import View
from laserpony import app
from util import db
#Models
from user import User

from flask_login import current_user, login_user, logout_user


#Views
class IndexView(View):
    methods = ['GET']

    def dispatch_request(self):
        if current_user.is_anonymous():
            return redirect(url_for('login'))
        else:
            return render_template('index.html')


class LoginView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            return render_template('login.html')
        elif request.method == 'GET':
            return render_template('login.html')


class LogoutView(View):
    methods = ['GET']

    def dispatch_request(self):
        logout_user()
        return redirect(url_for('login'))


class SignUpView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        #Handle POST
        if request.method == 'POST':
            name = request.form['name']
            if name == '':
                error = 'Name is required!'
                return render_template('signup.html', error=error)
            email = request.form['email']
            if email == '':
                error = 'Email is required!'
                return render_template('signup.html', error=error)
            password1 = request.form['password1']
            password2 = request.form['password2']
            if password1 == '':
                error = 'You must provide a password!'
                return render_template('signup.html', error=error)
            if password1 != password2:
                error = 'Passwords do not match!'
                return render_template('signup.html', error=error)
            user = User(name, email, password1)
            user.save()
            login_user(user)
            return redirect(url_for('index)'))
        #Handle GET
        elif request.method == 'GET':
            return render_template('signup.html')

#Page View Rules
app.add_url_rule('/',
                view_func=IndexView.as_view('index'))
app.add_url_rule('/login',
                view_func=LoginView.as_view('login'))
app.add_url_rule('/logout',
                view_func=LogoutView.as_view('logout'))
app.add_url_rule('/signup',
                view_func=SignUpView.as_view('signup'))


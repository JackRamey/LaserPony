from flask import redirect, render_template, request, url_for
from flask.views import View
from flask_login import login_user, logout_user
from laserpony import app
from laserpony.models import Post, User

#Views
class IndexView(View):
    methods = ['GET']

    def dispatch_request(self):
        posts = Post.objects.order_by('created_at').limit(app.config['NUM_POSTS_HOMEPAGE'])
        return render_template('index.html', posts=posts)

#Login
class LogInView(View):
    methods = ['GET','POST']

    def dispatch_request(self):
        if request.method == 'POST':
            user = User.objects(email=request.form['email']).first()
            if user is None:
                error = "That user does not exist."
                return render_template('login.html', error=error)
            else:
                if user.password_hash == request.form['password']:
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    error = "Username and Password combination are incorrect."
                    return render_template('login.html', error=error)

        else:
            return render_template('login.html')

#Logout
class LogOutView(View):
    methods = ['GET']

    def dispatch_request(self):
        logout_user()
        return redirect(url_for('index'))

#Sign Up
class SignUpView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        return render_template('disabled.html')
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            pass1 = request.form['password1']
            pass2 = request.form['password2']
            args = {'name':name,'email':email}
            user = User.objects(email=email).first()
            if user is not None:
                error = "Email provided is already in use!"
                return render_template('signup.html', error=error, args=args)
            if pass1 == '' or pass1 is None:
                error = "You must provide a valid password!"
                return render_template('signup.html', error=error, args=args)
            if pass1 != pass2:
                error = "Passwords do not match!"
                return render_template('signup.html', error=error, args=args)
            #All checks passed, create user
            newUser = User(name, email, pass1, active=True, admin=False, authenticated=True)
            newUser.save()
            login_user(newUser)
            return redirect(url_for('index'))
        else:
            args = {}
            return render_template('signup.html', args=args)

#Page View Rules
app.add_url_rule('/',
                view_func=IndexView.as_view('index'))
app.add_url_rule('/login',
                view_func=LogInView.as_view('login'))
app.add_url_rule('/logout',
                view_func=LogOutView.as_view('logout'))
app.add_url_rule('/signup',
                view_func=SignUpView.as_view('signup'))


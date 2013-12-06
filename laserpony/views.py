from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from flask.views import View
from laserpony import app
from laserpony.models import Post, User


#Views
class IndexView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('index.html')

#Login
class LogInView(View):
    methods = ['GET','POST']

    def dispatch_request(self):
        if request.method == 'POST':
            user = User.objects.get(name=request.form['username'])
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


#Posts
class PostsView(View):
    methods = ['GET']

    def dispatch_request(self):
        posts = Post.objects.all()
        return render_template('posts.html', posts=posts)


#Post
class PostView(View):
    methods = ['GET']

    def dispatch_request(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        return render_template('post.html', post=post)

#Page View Rules
app.add_url_rule('/',
                view_func=IndexView.as_view('index'))
app.add_url_rule('/login',
                view_func=LogInView.as_view('login'))
app.add_url_rule('/logout',
                view_func=LogOutView.as_view('logout'))
app.add_url_rule('/posts/',
                view_func=PostsView.as_view('posts'))
app.add_url_rule('/posts/<slug>',
                view_func=PostView.as_view('post'))


from flask import redirect, render_template, request, url_for
from flask.views import View
from laserpony import app
from laserpony.models import Post


#Views
class IndexView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('index.html')


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
app.add_url_rule('/posts/',
                view_func=PostsView.as_view('posts'))
app.add_url_rule('/posts/<slug>',
                view_func=PostView.as_view('post'))


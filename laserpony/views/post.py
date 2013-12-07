from flask import render_template
from flask.views import View
from laserpony import app
from laserpony.models import Post

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
app.add_url_rule('/posts/',
                view_func=PostsView.as_view('posts'))
app.add_url_rule('/posts/<slug>',
                view_func=PostView.as_view('post'))


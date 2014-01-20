from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from bson.objectid import ObjectId
from laserpony import app
from laserpony.views.scaffold import BaseView
from laserpony.models.post import Post


#Posts
class PostsView(BaseView):
    methods = ['GET']

    def handle_request(self):
        posts = Post.objects.all()
        return render_template('posts.html', posts=posts)


#Post CRUD
class PostView(BaseView):
    methods = ['GET']

    def handle_request(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        return render_template('post.html', post=post)


class PostCreate(BaseView):
    methods = ['GET', 'POST']

    @login_required
    def handle_request(self):
        if not current_user.is_author():
            return redirect(url_for('index'))
        if request.method == 'POST':
            title = request.form['title']
            slug = request.form['slug']
            body = request.form['body']
            newPost = Post(title=title,slug=slug,body=body)
            if current_user.is_author():
                newPost.save()
            return redirect(url_for('posts'))
        else:
            return render_template('post_create_edit.html', post=None)


class PostEdit(BaseView):
    methods = ['GET', 'POST']

    @login_required
    def handle_request(self, post_id):
        if not current_user.is_author():
            return redirect(url_for('index'))
        post = Post.objects(id=ObjectId(post_id)).first()
        if request.method == 'POST':
            post.title = request.form['title']
            post.slug = request.form['slug']
            post.body = request.form['body']
            post.save()
            return redirect(url_for('post', slug=post.slug))
        else:
            return render_template('post_create_edit.html', post=post)


class PostDelete(BaseView):
    methods = ['GET', 'POST']

    @login_required
    def handle_request(self, post_id):
        post = Post.objects(id=ObjectId(post_id)).first()
        if current_user.is_admin():
            if request.method == 'POST':
                delete_text = request.form['delete-text']
                print(delete_text)
                if delete_text == 'DELETE':
                    post.delete()
                    return redirect(url_for('posts'))
                else:
                    error = "Confirmation text was not correct."
                    return render_template('post_delete.html', post=post, error=error)
            else:
                return render_template('post_delete.html', post=post)
        else:
            return redirect(url_for('posts'))

#Page View Rules
app.add_url_rule('/posts/',
                view_func=PostsView.as_view('posts'))
app.add_url_rule('/posts/<slug>',
                view_func=PostView.as_view('post'))
app.add_url_rule('/posts/create/',
                view_func=PostCreate.as_view('post_create'))
app.add_url_rule('/posts/edit/<post_id>',
                view_func=PostEdit.as_view('post_edit'))
app.add_url_rule('/posts/delete/<post_id>',
                view_func=PostDelete.as_view('post_delete'))


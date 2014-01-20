from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from bson.objectid import ObjectId
from laserpony import app
from laserpony.views.scaffold import BaseView
from laserpony.models.user import User


#User
class UsersView(BaseView):
    methods = ['GET']

    @login_required
    def handle_request(self):
        users = User.objects.all()
        if current_user.is_admin():
            return render_template('users.html', users=users, **self.context)
        else:
            redirect(url_for('index'))


#User CRUD
class UserView(BaseView):
    methods = ['GET']

    @login_required
    def handle_request(self, user_id):
        user = User.objects.get_or_404(id=ObjectId(user_id))
        return render_template('user.html', user=user, **self.context)


class UserEdit(BaseView):
    methods = ['GET', 'POST']

    @login_required
    def handle_request(self, user_id):
        if not current_user.is_admin() and current_user.id != ObjectId(user_id):
            return redirect(url_for('index'))
        user = User.objects(id=ObjectId(user_id)).first()
        if request.method == 'POST':
            user.name = request.form['name']
            user.email = request.form['email']
            user.active = False
            if 'active' in request.form:
                user.active = True
            user.admin = False
            if 'admin' in request.form:
                user.admin = True
            user.authenticated = False
            if 'authenticated' in request.form:
                user.authenticated = True
            user.author = False
            if 'author' in request.form:
                user.author = True
            user.save()
            return redirect(url_for('user', user_id=user.id))
        else:
            return render_template('user_edit.html', user=user, **self.context)

#Page View Rules
app.add_url_rule('/users/',
                view_func=UsersView.as_view('users'))
app.add_url_rule('/users/<user_id>',
                view_func=UserView.as_view('user'))
app.add_url_rule('/users/edit/<user_id>',
                view_func=UserEdit.as_view('user_edit'))


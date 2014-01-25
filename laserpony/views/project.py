from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required
from laserpony import app
from laserpony.views.scaffold import BaseView
from laserpony.models.project import Project
from laserpony.models.post import Post
from laserpony.forms.project import ProjectForm


#Project View
class ProjectView(BaseView):
    methods = ['GET']

    def handle_request(self, slug):
        project = Project.objects.get_or_404(slug=slug)
        posts = Post.objects(project=project).order_by('-created_at').all()
        return render_template('project.html',project=project,posts=posts, **self.context)


class ProjectCreate(BaseView):
    methods = ['GET', 'POST']

    @login_required
    def handle_request(self):
        if not current_user.is_admin():
            return redirect(url_for('index'))
        form = ProjectForm()
        if form.validate_on_submit():
            name = form.name.data
            slug = form.slug.data
            project = Project(name,slug)
            project.save()
            return redirect(url_for('project', slug=project.slug))
        else:
            return render_template('project_create_edit.html', form=form, **self.context)


class ProjectEdit(BaseView):
    methods = ['GET', 'POST']

    @login_required
    def handle_request(self, slug):
        if not current_user.is_admin():
            return redirect(url_for('index'))
        form = ProjectForm()
        project = Project.objects(slug=slug).first()
        if form.validate_on_submit():
            project.name = form.name.data
            project.slug = form.slug.data
            project.save()
            return redirect(url_for('project', slug=project.slug))
        else:
            form.name.data = project.name
            form.slug.data = project.slug
            return render_template('project_create_edit.html', form=form, **self.context)

app.add_url_rule('/project/<slug>/',
                view_func=ProjectView.as_view('project'))
app.add_url_rule('/projects/create/',
                view_func=ProjectCreate.as_view('project_create'))
app.add_url_rule('/projects/edit/<slug>/',
                view_func=ProjectEdit.as_view('project_edit'))


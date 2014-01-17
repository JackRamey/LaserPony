from flask import render_template, request
from flask.views import View
from laserpony import app
from laserpony.models.project import Project
from laserpony.models.post import Post

#Project View
class ProjectView(View):
    methods = ['GET']

    def dispatch_request(self, project_slug):
        project = Project.objects.get_or_404(slug=project_slug)
        posts = Post.objects(project=project).all()
        return render_template('project.html',project=project,posts=posts)

app.add_url_rule('/<project_slug>/',
                view_func=ProjectView.as_view('project'))

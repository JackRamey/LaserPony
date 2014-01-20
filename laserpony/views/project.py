from flask import render_template, request
from laserpony import app
from laserpony.views.scaffold import BaseView
from laserpony.models.project import Project
from laserpony.models.post import Post

#Project View
class ProjectView(BaseView):
    methods = ['GET']

    def handle_request(self, project_slug):
        project = Project.objects.get_or_404(slug=project_slug)
        posts = Post.objects(project=project).all()
        return render_template('project.html',project=project,posts=posts, **self.context)

app.add_url_rule('/project/<project_slug>/',
                view_func=ProjectView.as_view('project'))

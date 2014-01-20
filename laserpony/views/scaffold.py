from flask.views import View
from laserpony.models.project import Project


class BaseView(View):
    context = {}

    def prepare(self, *args, **kwargs):
        #Any processing that needs to happen before each request is handled
        #gets taken care of here
        projects = Project.objects
        self.context['navigation'] = projects

    def handle_request(self):
        """Subclasses have to override this method to implement the
        actual view function code.  This method is called with all
        the arguments from the URL rule.
        """
        raise NotImplementedError()

    def dispatch_request(self, *args, **kwargs):
        self.context = dict()
        self.prepare(self, *args, **kwargs)
        return self.handle_request(*args, **kwargs)



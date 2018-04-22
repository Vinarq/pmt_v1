import cherrypy, logging
from controllers.base import BaseController

class HomeController(BaseController):
    @cherrypy.expose
    def tt(self, **kwargs):
        from processes import test
        response_ = test.red()
        response_ = response_._get_red(logging)
        logging.info(str(response_))
        return str(response_)

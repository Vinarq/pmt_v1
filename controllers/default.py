import hashlib
import cherrypy, logging
from controllers.base import BaseController
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class DashboardController(BaseController):
    @cherrypy.expose
    def dashboard(self):
        return self.render_template()

class LoginController(BaseController):
	"""docstring for LoginController"""
	@cherrypy.expose
	def login(self):
		return self.render_template()

class ForgotPController(BaseController):
	"""docstring for LoginController"""
	@cherrypy.expose
	def forgot_password(self):
		return self.render_template()

class RegisterController(BaseController):
	"""docstring for LoginController"""
	@cherrypy.expose
	def register(self):
		return self.render_template()
		
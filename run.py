from controllers.tester import HomeController
from controllers.default import DashboardController, LoginController, RegisterController, ForgotPController
import cherrypy, logging
from cherrypy import tools
from settings.base import settings

def error_page_404(status, message, traceback, version):
    logging.warn(str(status))
    logging.warn(str(message))
    logging.warn(str(traceback))
    logging.warn(str(version))
    return file("templates/404.html")


def start_server():
    site_config_path = 'site.conf'
    cherrypy.config.update({'log.screen': True,'log.access_file': "",'log.error_file': ""})
    cherrypy.engine.unsubscribe('graceful', cherrypy.log.reopen_files)
    logging.config.dictConfig(settings.LOG_CONF)
    cherrypy.tree.mount(HomeController(), '/', site_config_path)
    cherrypy.tree.mount(DashboardController(), '/dashboard', site_config_path)
    cherrypy.tree.mount(LoginController(), '/login', site_config_path)
    cherrypy.tree.mount(RegisterController(), '/register', site_config_path)
    cherrypy.tree.mount(ForgotPController(), '/forgot_password', site_config_path)
    cherrypy.config.update({'error_page.404': error_page_404})
    cherrypy.config.update('server.conf')
    # settings.ssl_module
    # settings.certificate_
    # settings.private_key
    # settings.logger
    cherrypy.engine.start()

if __name__ == '__main__':
    start_server()
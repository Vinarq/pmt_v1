import inspect,logging
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from site_conf import site_config
class BaseController:


    def get_template(self, caller_name):
        template = None
        try:
            logging.info(str(caller_name))
            class_name = self.__class__.__name__.replace('Controller', '')
            logging.info(str(class_name))
            view_base = '{0}/templates'.format(site_config.home)
            logging.info(str(view_base))
            view_path = '{0}'.format(view_base)
            logging.info(str(view_path))
            env = Environment(loader=FileSystemLoader([view_base, view_path]))
            template = env.get_template(caller_name+ '.html')
            logging.info(str(template))
        except TemplateNotFound as template_ex:
            logging.exception(template_ex)
        except Exception as e:
            logging.exception(e)
        return template

    def render_template(self, template_vars={}):
        try:
            caller_name = inspect.stack()[1][3]
            return self.get_template(caller_name).render(template_vars)
        except Exception as ex:
            logging.exception(ex)
            return None
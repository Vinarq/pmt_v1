import logging, cherrypy,os, sys
import logging.config
from os.path import abspath
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))


#Email Settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER =''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

#SSL
certificate_= os.path.join(BASE_DIR, 'website')
private_key= os.path.join(BASE_DIR, 'website')


ssl_module=cherrypy.server.ssl_module = 'builtin'
certificate_=cherrypy.server.ssl_certificate = certificate_+"/certs/certificate.crt"
private_key=cherrypy.server.ssl_private_key = private_key+"/certs/private.key"
server_ip=cherrypy.request.remote.ip

#AUTH

ALLOWED_HOST=[
    server_ip
]


logger=cherrypy._cpconfig.environments['production']['log.screen'] = False


LOG_CONF = {
    'version': 1,

    'formatters': {
        'void': {
            'format': ''
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'WARN',
            'class':'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'cherrypy_console': {
            'level':'WARN',
            'class':'logging.StreamHandler',
            'formatter': 'void',
            'stream': 'ext://sys.stdout'
        },
        'cherrypy_access': {
            'level':'WARN',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'void',
            'filename': 'access.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        },
        'cherrypy_error': {
            'level':'WARN',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'void',
            'filename': 'errors.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'WARN'
        },
        'db': {
            'handlers': ['default'],
            'level': 'WARN' ,
            'propagate': False
        },
        'cherrypy.access': {
            'handlers': ['cherrypy_access'],
            'level': 'WARN',
            'propagate': False
        },
        'cherrypy.error': {
            'handlers': ['cherrypy_console', 'cherrypy_error'],
            'level': 'WARN',
            'propagate': False
        },
    }
}

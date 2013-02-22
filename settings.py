from os import path as op
import logging

SERVER_ROOT = op.normpath(op.dirname(__file__))
STATIC_DIR = op.join(SERVER_ROOT, 'static')
TEMPLATES_DIR = op.join(SERVER_ROOT, 'templates')

COOKIE_SECRET = '61oETzKXQAGaYdkL5gEmGe61oETzKXQAGaYdkL5gEmGe'

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

DEBUG = True



from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler  

import settings
import handlers


routes = [
  (r'/', handlers.MainHandler),
  (r'/(login|logout|profile|signup)', handlers.ProfileHandler)
]


application = Application(
    routes + [
        (r'/static/(.*)', StaticFileHandler, {'path': settings.STATIC_DIR })
    ],
    template_path=settings.TEMPLATES_DIR,
    cookie_secret=settings.COOKIE_SECRET,
    debug=settings.DEBUG
)

if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    application.listen(8000)
    IOLoop.instance().start()




from tornado.web import RequestHandler



class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class ProfileHandler(RequestHandler):
    def get(self, action):
        action = getattr(self, 'get_' + action, None)
        if action:
            return action()
        else:
            raise Exception("Not found")

    def post(self, action):
        action = getattr(self, 'post_' + action, None)
        if action:
            return action()
        else:
            raise Exception("Not found")

    def get_login(self):
        self.render("login.html")



routes = [
  (r'/', MainHandler),
  (r'/(login|logout|profile|signup)', ProfileHandler)
]


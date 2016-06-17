from tornado.web import RequestHandler as r
import random
import logging


class Home(r):
    def get(self):
        context = {}
        self.render("index.html", **context)

class Style(r):
    def get(self):
        context = {}
        self.render("style/app.css", **context)

class PageNotFound(r):
    def get(self):
        context = {}
        self.render("basic/404_not_found.html", **context)

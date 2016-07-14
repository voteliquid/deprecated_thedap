import tornado
from base import RequestHandler as R
import random
import logging


class Home(R):
    def get(self):
        context = {}
        self.render("index.html", **context)

class Style(R):
    def get(self):
        context = {}
        self.render("style/app.css", **context)

class PageNotFound(R):
    def get(self):
        context = {}
        self.render("basic/404_not_found.html", **context)

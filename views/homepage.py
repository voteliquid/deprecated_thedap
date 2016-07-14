import tornado
from base import RequestHandler as R
import random
import logging


class Home(R):
    def get(self):
        context = {}
        self.render("index.html", **context)


class Login(R):
    def get(self):
        context = {}
        self.render("login.html", **context)
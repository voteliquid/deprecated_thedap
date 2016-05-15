# from libraries.requests import requests
from tornado.web import RequestHandler as r
import random
import logging

#todo resize all post images in GIMP to same size.
#Use a sprite to cut up all the images. 
#Later: do something fun with the images. Like a rubic's cube or something. 



class Test(r):
	def get(self):
		context = {}
		self.render("basic/test.html", **context)


class Home(r):
	def get(self):
		context = {}
		self.render("index.html", **context)



class SchizoRobot(r):
	def get(self):
		context = {}
		self.render("basic/schizo_robot.html", **context)


class PageNotFound(r):
	def get(self):
		context = {}
		self.render("basic/404_not_found.html", **context)

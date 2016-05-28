#!/usr/bin/env python
import os
import os.path
import logging
import tornado.web
import tornado.wsgi
import wsgiref.handlers

from views import homepage, voting

                   
settings = {
    # Application Settings
    "title": u"rd108",
    "cookie_secret": "12093b258de35ad7dcq5b96a3bdbe9401c3b71c81fa8f0baa442d5f3",
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    # Configuration
    "debug": os.environ['SERVER_SOFTWARE'].startswith('Development'),
    #"xsrf_cookies": True,
}        

application = tornado.wsgi.WSGIApplication([   

    (r"/voting", voting.VotingModule),
    (r'.*', homepage.Home)

], **settings)


def main():
    wsgiref.handlers.CGIHandler().run(application)


if __name__ == "__main__":
    main()

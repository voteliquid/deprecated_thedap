import tornado
from google.appengine.ext.db import GqlQuery #for BaseHandler.get_user on Google App Engine.
from google.appengine.ext import db
from models.user import User




class RequestHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        """overriding the built-in Tornado function for @tornado.web.authenticated"""
        return self.get_secure_cookie("user")

    def update_model(self, model, values):
        for k, v in values.iteritems():
            setattr(model, k, v)
        return model

    def gen_query(self, model_name, params):
        """takes a model_name (e.g. "User" as a string) and dictionary of params 
        and returns a GQLQuery object"""
        query_text = "SELECT * from " + model_name + " WHERE "
        first_and = True
        for key in params_dict.keys():
            if first_and:
                query_text+=" " + key + " = :" + key
                first_and = False
            else:
                query_text+=" AND " + key + " = :" + key
        query = db.GqlQuery(query_text, **params_dict)
        return query

    def from_email(self, email):
        """convenience wrapper around gen_query, input email string,
        return first User object found in DB with that email."""
        q = self.gen_query("User", {"email":email} )
        user = q.get()
        return user
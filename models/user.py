from google.appengine.ext import db
import models.util.properties


class User(db.Expando):
	#signup
    email = db.EmailProperty(required=True)
    signup_message = db.StringProperty()
    signup_code = db.StringProperty()
    #app data
    activated = db.BooleanProperty()
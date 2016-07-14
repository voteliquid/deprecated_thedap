from google.appengine.ext import db
from Crypto.Hash import SHA256



class BaseModel(db.Expando):
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)



class DAP(BaseModel):
    name = db.StringProperty()


class User(BaseModel):
    email = db.EmailProperty(required=True)    
    password = db.StringProperty() #hashed with make_hash
    #collected properties
    dap = db.ReferenceProperty(DAP, collection_name='users')

    def check_password(self, plaintext_password):
        """Check a password against an existing hash."""
        return self.password == SHA256.new(plaintext_password).hexdigest()

    def set_password(self, plaintext_password):
        self.password = SHA256.new(plaintext_password).hexdigest()


class Proposal(BaseModel):
    proposal_text = db.StringProperty()
    cost = db.FloatProperty()
    client_timestamp = db.DateTimeProperty()
    #collected properties
    user = db.ReferenceProperty(User, collection_name='proposals')
    dap = db.ReferenceProperty(DAP, collection_name='proposals')



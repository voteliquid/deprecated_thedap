from google.appengine.ext import db
from Crypto.Hash import SHA256



class BaseModel(db.Expando):
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)


class User(BaseModel):
    email = db.EmailProperty(required=True)    
    password = db.StringProperty() #hashed with make_hash

    def check_password(self, plaintext_password):
        return check_hash(plaintext_password, self.password)

    def set_password(self, plaintext_password):
        self.password = make_hash(plaintext_password)



def make_hash(password):
    """Generate a new hash for the password."""
    return SHA256.new(password).hexdigest()

def check_hash(password, password_hash):
    """Check a password against an existing hash."""
    return SHA256.new(password).hexdigest() == password_hash
import tornado
from base import RequestHandler as R
import random
import logging
import json


class Authenticate(R):
   def post(self):
        packet = json.loads(self.request.body)
        logging.info(packet)

        user = self.from_email(packet["email"])

        if user.check_password(packet["password"]):
            self.set_status(200)
            resp = {"success":True, "error":""}
        else:
            self.set_status(400)
            resp = {"success":False, "error":str(sys.exc_info())}            
        
        self.write(json.dumps(resp))
        return 


class ListProposals(R):
    @tornado.web.authenticated
    def post(self):
        packet = json.loads(self.request.body)
        logging.info(packet)

        user = self.from_email(packet["email"])

        if user.check_password(packet["password"]):
            self.set_status(200)
            resp = {"success":True, "error":""}
        else:
            self.set_status(400)
            resp = {"success":False, "error":str(sys.exc_info())}            
        
        self.write(json.dumps(resp))
        return 


class CreateProposal(R):
    @tornado.web.authenticated
    def post(self):
        packet = json.loads(self.request.body)
        logging.info(packet)

        user = self.from_email(packet["email"])

        if user.check_password(packet["password"]):
            self.set_status(200)
            resp = {"success":True, "error":""}
        else:
            self.set_status(400)
            resp = {"success":False, "error":str(sys.exc_info())}            
        
        self.write(json.dumps(resp))
        return 



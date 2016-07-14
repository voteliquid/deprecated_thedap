import tornado
from base import RequestHandler as R
from google.appengine.ext import db
import json
import logging

from models.user import DAP, User, Proposal





class ListProposals(R):
    @tornado.web.authenticated
    def get(self):
        dap_key_str = self.get_argument("dap")
        dap = db.get(dap_key_str)

        proposals = []
        for p in dap.proposals:
            proposals.append({"proposal_title":p.proposal_title,
                             "proposal_text":p.proposal_text,
                             "cost":p.cost,
                             "timestamp":.p.created.strftime("%d/%m/%Y %H:%M:%S"),
                             "user":p.user.key(),
                             "dap":p.dap.key()
                             })
        self.set_status(200)
        self.write(json.dumps(proposals))


class CreateProposal(R):
    @tornado.web.authenticated
    def post(self):
        data = json.loads(self.request.body)
        logging.info(data)  

        p = Proposal(
                     proposal_title=data["proposal_title"],
                     proposal_text=data["proposal_text"],
                     cost=float(data["cost"]),
                     dap=db.get(data["dap"]),
                     user=str(self.get_current_user().key())
                    )
        p.put()

        r = {"proposal_title":p.proposal_title,
             "proposal_text":p.proposal_text,
             "cost":p.cost,
             "timestamp":.p.created.strftime("%d/%m/%Y %H:%M:%S"),
             "user":p.user.key(),
             "dap":p.dap.key()
             })
        self.set_status(200)
        self.write(json.dumps(r))


class Authenticate(R):
    """TODO: this needs to be refactored to be more secure, e.g. stopping multiple password check attempts"""
    def get(self):
        data = json.loads(self.get_arguments)
        logging.info(data)

        user = self.from_email(data["email"])

        if user.check_password(data["password"]):
            #set secure cookie
            self.set_secure_cookie("user", str(user.key()))
            self.set_status(200)
            resp = {"success":True, "error":""}
        else:
            self.set_status(400)
            resp = {"success":False, "error":"Could not authenticate user"}            

        self.write(json.dumps(resp))

        
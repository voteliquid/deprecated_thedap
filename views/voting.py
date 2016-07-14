import tornado
from base import RequestHandler as R
import random
import logging

from pyvotecore.schulze_pr import SchulzePR


class VotingModule(R):
    def get(self):
        ballots = [
            {"count": 6, "ballot": [["a"], ["d"], ["b"], ["c"], ["e"]]},
            {"count": 12, "ballot": [["a"], ["d"], ["e"], ["c"], ["b"]]},
            {"count": 72, "ballot": [["a"], ["d"], ["e"], ["b"], ["c"]]},
            {"count": 6, "ballot": [["a"], ["e"], ["b"], ["d"], ["c"]]},
            {"count": 30, "ballot": [["b"], ["d"], ["c"], ["e"], ["a"]]},
            {"count": 48, "ballot": [["b"], ["e"], ["a"], ["d"], ["c"]]},
            {"count": 24, "ballot": [["b"], ["e"], ["d"], ["c"], ["a"]]},
            {"count": 168, "ballot": [["c"], ["a"], ["e"], ["b"], ["d"]]},
            {"count": 108, "ballot": [["d"], ["b"], ["e"], ["c"], ["a"]]},
            {"count": 30, "ballot": [["e"], ["a"], ["b"], ["d"], ["c"]]},
        ]

        output = SchulzePR(ballots, ballot_notation=SchulzePR.BALLOT_NOTATION_GROUPING).as_dict()

        #test assumptions: budget = 1000 bucks, each proposal is $300 bucks
        budget = 1000.00 
        approved_proposals = []
        for proposal in output["order"]:
            #subtract proposal budget from total
            proposal_budget = 300
            if budget - proposal_budget>0:
                approved_proposals.append(proposal)
                budget = budget - proposal_budget
            else:
                break



        context = {
            "results": output,
            "approved_proposals": approved_proposals,
            "remaining_budget": budget
        }
        self.render("voting_module.html", **context)


    def post(self):
        """use the schultz proportional method to rank the proposals until the budget is done."""
        context = {}
        self.render("voting_module.html", **context)



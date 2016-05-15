from google.appengine.ext import db
import models.util.properties


class Record(db.Expando):
	"""Gooroo user"""

	created = db.DateTimeProperty(auto_now_add=True)
	# email = db.EmailProperty(required=False)
	# password = models.util.properties.PickledProperty(required=False)
	program = db.StringProperty(required=False)
	jobcard = db.StringProperty(required=False)
	surname = db.StringProperty(required=False)
	name = db.StringProperty(required=False)
	caste = db.StringProperty(required=False)
	age = db.IntegerProperty(required=False)
	sex = db.StringProperty(required=False)
	work_id = db.IntegerProperty(required=False)
	pay_order_id = db.IntegerProperty(required=False)
	from_data = db.StringProperty(required=False)
	to_date = db.StringProperty(required=False)
	pay_order = db.StringProperty(required=False)
	gen_date = db.StringProperty(required=False)
	days = db.FloatProperty(required=False)
	payment_per_day = db.FloatProperty(required=False)
	amount = db.FloatProperty(required=False)
	account_no = db.IntegerProperty(required=False)
	advance_paid = db.FloatProperty(required=False)
	vo_sangam = db.StringProperty(required=False)

	#headers = db.StringListProperty(required=True, default=['Welcome to gooroo.me'])


#[u'Program', u'Jobcard ID', u'SurName', u'Name', u'Caste', u'Age', u'Sex', u'WorkID', u'Pay Order Id', u'Work Name', u'From Date', u'To Date', u'PayOrder Gen Date', u'Days', u'Payment Per Day(Rs)', u'Amount (Rs)', u'Account No.', u'Bank/PostOffice Name', u'Advance Paid', u'VO/Labour Sangam']
	
# PayOrder 
# Gen Date	
# Days	
# Payment Per Day(Rs)	
# Amount (Rs)	
# Account No.	Bank/PostOffice Name	
# Advance Paid	
# VO/Labour Sangam


# State Name: 
# District Name: 
# Mandal Name: 
# Panchayat Name: 
# Village Name: 
# Hab Name: 

    

    



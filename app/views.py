from flask import render_template, flash, redirect, request
from app import db
from app import app
from models import Applicant, Event
import constants
import json
from datetime import datetime,timedelta
from utils import *


def get_applicant_by_email(email_id):
	""" Returns the applicant object that matches the unique emailId given. Retuns None when no match found """
	return Applicant.query.filter_by(email=email_id).first()

def event_counts(date_start,date_end):
	""" Returns the counts of event entries grouped by the event type, between the date range provided """
	res={}
	events=db.session.query(Event,db.func.count(Event.event_type)).filter(Event.created_time >= date_start,Event.created_time < date_end).group_by(Event.event_type).all()
	for event,count in events:
		res[event.event_type]=count
	return res

@app.route('/')
@app.route('/index')
def landing_page():
	""" Records a visit event and retuns the landing page HTML """
	Event(None,constants.EVENT_VISITED).commit()
	return render_template('landing_page.html')


@app.route('/new_applicant',methods=['POST'])
def new_applicant():
	""" Attempts to create an applicant object, persist it, commit an application event and return the questionnare HTML. 
	Returns appropriate error msg if unable to do so. """
	form=request.form
	try:
		applicant = Applicant(form['email'],form['firstname'],form['lastname'],form['phone'],form['zipcode'])
		applicant.commit()
		Event(applicant.id,constants.EVENT_APPLIED).commit()
	except ValueError as error:
		return constants.ERROR_INVALID_VALUES
	except:
		return constants.ERROR_USER_EXISTS
	return render_template('questionnaire_page.html')

@app.route('/questionnare')
def questionnare():
	return render_template('questionnaire_page.html')	

@app.route('/update_answers/<email>',methods=['POST'])
def update_answers(email):
	""" Updates the answers for the current applicant and commits it to DB """
	applicant = get_applicant_by_email(email)
	applicant.answers=json.dumps(form_entries(request.form))
	applicant.commit()
	Event(applicant.id,constants.EVENT_COMPLETED_QUESTIONNARE).commit()
	return render_template('bgcheck_page.html')


@app.route('/submit_bgcheck/<email>',methods=['POST'])
def submit_bgcheck(email):
	""" Registers a background check event for the current applicant """
	applicant = get_applicant_by_email(email)
	Event(applicant.id,constants.EVENT_ACCEPTED_BG_CHECK).commit()
	return render_template('confirmation_page.html', applicant=applicant)

@app.route('/funnels.json')
def event_funnels():
	""" Returns the event counts for every week (Mon-Sun) between the date range specified in request.args """
	try:
		start_date=string_to_date(request.args[constants.FUNNELS_START_DATE],constants.FUNNELS_DATE_PATTERN)
		end_date=string_to_date(request.args[constants.FUNNELS_END_DATE],constants.FUNNELS_DATE_PATTERN)
		
		date_ranges=week_ranges(start_date,end_date)
		res={}
		for d_start,d_end in date_ranges:
			res[date_range_key(d_start,d_end)]=event_counts(d_start,d_end)
		return json.dumps(res)	
	except:
		return json.dumps({})   # TODO: failure



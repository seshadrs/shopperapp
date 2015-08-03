# shopperapp
Personal Shopper Application

IINSTALLING DEPENDENCIES:
pip install -r requirements.txt

DB SETUP:
python db_create.py

RUN APP:
- To run on default port (5000) :  "python run.py"
- To run on a chosen port :  "python run.py [PORT]"

TEST FUNNEL STATISTICS:
- "http://127.0.0.1:5000/funnels.json?start_date=2015-7-05&end_date=2015-8-09"


IMPLEMENTATION:
- Single page app that uses Python Flask as server
- REST HTTP APIs exposed
- Server is stateless/session-unaware. EmailId used as session/user identifier
- Sqlite DB used to store Applicant, Event (defined in models.py)
- Parsley.js used for form validation

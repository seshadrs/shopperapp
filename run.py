import sys
from app import app

if len(sys.argv)>1 and type(sys.argv[1]==int):
	app.run(debug=True,port=int(sys.argv[1]))
else:
	app.run(debug=True)

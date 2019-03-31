#!/usr/bin/env python3

import cgi, cgitb
import worker

# Enable CGI Traceback
# Disable it in production
cgitb.enable()

# Save data from POST (if any) into form variable
form = cgi.FieldStorage()

""" Check if the form is empty """
""" Only possible if someone deliberately modifies the webpage """
if form is not None:
	if form.getvalue('prog'):
		worker.showResult(form.getvalue('prog'))
	elif form.getvalue('qGroup'):
		worker.putQues(form.getvalue('qGroup'))
	else:
		worker.badRequest()
else:
	worker.badRequest()
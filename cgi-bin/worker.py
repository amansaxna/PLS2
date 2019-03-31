#!/usr/bin/env python3

import templateEngine
import xml.etree.ElementTree as ET

""" This function is executed when "worker" module is imported into "enginePLS2".
    Data file (PLS2_data.xml) is parsed and root element is extracted from it.
    CGI content type line is printed to interpret output as HTML.
"""

tree = ET.parse('data/PLS2_data.xml')
root = tree.getroot()
print(templateEngine.content_type())

# Function to handle bad requests
def badRequest():
	print(templateEngine.HackingAttempt())

# Function to handle the final response
def showResult(nameOfLanguage):

	""" If the language is present, it will be assigned to tmp otherwise None will be assigned """
	tmp = root.find(nameOfLanguage)

	""" Make sure that the element exists and it is a programming language """
	if tmp is not None and (tmp.get('type') == 'prog'):
		print(templateEngine.finalPage(tmp.get('name'), tmp.text, tmp.get('website'), tmp.get('logo')))
	else:
		badRequest()

# Function to handle intermediate response
def putQues(nameOfFile):

	""" If the question group is present, it will be assigned to tmp otherwise None will be assigned """
	tmp = root.find(nameOfFile)

	""" Make sure that the element exists and it is a question group """
	if tmp is not None and (tmp.get('type') == 'qGroup'):
		
		""" Generate the HTML using templateEngine """
		print(templateEngine.head())
		print(templateEngine.javascript())
		print(templateEngine.head_title())
		print(templateEngine.favicon())
		print(templateEngine.css())
		print(templateEngine.about())
		print(templateEngine.form_start())

		""" Display the main question """
		print(templateEngine.mainQues(tmp.get('mQues')))

		""" Display all the radio buttons """
		for i, each_ele in enumerate(tmp.iter('resp')):
			print(templateEngine.radio_start(each_ele.tag + str(i), each_ele.get('rtype'), each_ele.get('rvalue')))
			print(templateEngine.radio_end(each_ele.tag + str(i), each_ele.text))

		""" Display the final credits and end page """
		print(templateEngine.credits())
		print(templateEngine.form_end())
		print(templateEngine.foot())
	else:
		badRequest()
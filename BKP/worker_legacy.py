#!/usr/bin/python3

import templateEngine

# CGI Content Type (Executes when the file is imported into enginePLS2) 
print(templateEngine.content_type())

# Function to handle the final response
def showResult(nameOfLanguage):
	print(templateEngine.finalPage(nameOfLanguage))

# Function to handle intermediate response
def putQues(nameOfFile):
	try:
		# Parse the text file's contents to get new question, options and their values
		with open('data/' + nameOfFile + '.txt') as quesFile:
			rawlist = [str(line.strip()) for line in quesFile.readline().split(';')]
			newlist = [str(value.strip()) for value in rawlist[0].split(':')]
			newlist1 = [str(value.strip()) for value in rawlist[1].split(':')]

		# Generate the HTML using templateEngine
		print(templateEngine.head())
		print(templateEngine.javascript())
		print(templateEngine.head_title())
		print(templateEngine.favicon())
		print(templateEngine.css1())
		print(templateEngine.css2())
		print(templateEngine.css3())
		print(templateEngine.about())
		print(templateEngine.form_start())
		print(templateEngine.mainQues(newlist[0]))

		# Loop to create multiple radio buttons 
		for i in range(1, len(newlist)):
			
			# Test the last character for $ (i.e., if its the last option)
			if newlist[i][-1:] == '$':
				newlist[i] = newlist[i].rstrip('$')
				rb_name = 'prog'
			else:
				rb_name = 'name'

			rb_id = 'choice-' + str(i)

			print(templateEngine.radio_start(rb_id, rb_name, newlist1[i-1]))
			print(templateEngine.radio_end(rb_id, newlist[i]))

		print(templateEngine.credits())
		print(templateEngine.form_end())
		print(templateEngine.foot())

	except IOError as err:
		print('Error while opening file : ' + str(err))

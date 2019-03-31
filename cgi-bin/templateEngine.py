#!/usr/bin/env python3

# Template Engine v2.0.0 (based on )

def content_type():
	return('Content-type: text/html\n\n')

def head():
	return('<!DOCTYPE html><html><head>')

def javascript():
	return('<script src="/js/userSelect.js"></script>')

def head_title(title='PLS2'):
	return('<meta charset="UTF-8"><title>' + str(title) + '</title>')

def favicon():
	fav_info = '<link rel="apple-touch-icon" sizes="180x180" href="/favicon/apple-touch-icon.png">'
	fav_info += '<link rel="icon" type="image/png" sizes="32x32" href="/favicon/favicon-32x32.png">'
	fav_info += '<link rel="icon" type="image/png" sizes="16x16" href="/favicon/favicon-16x16.png">'
	fav_info += '<link rel="manifest" href="/favicon/site.webmanifest">'
	fav_info += '<link rel="mask-icon" href="/favicon/safari-pinned-tab.svg" color="#5bbad5">'
	fav_info += '<link rel="shortcut icon" href="/favicon/favicon.ico">'
	fav_info += '<meta name="msapplication-TileColor" content="#da532c">'
	fav_info += '<meta name="msapplication-config" content="/favicon/browserconfig.xml">'
	fav_info += '<meta name="theme-color" content="#8cd652">'
	return(str(fav_info))

def css():
	css_str = '<link rel="stylesheet" href="/css/reset.min.css">'
	css_str += '<link rel="stylesheet prefetch" href="https://fonts.googleapis.com/css?family=Roboto">'
	css_str += '<link rel="stylesheet" href="/css/style.css"></head>'
	return(str(css_str))

def about():
	return('<body><div class="alert"><h2>PLS2</h2><p>Programming Language Suggestion System (PLS2) lets you select a programming language based on your needs.<p></div>')

def form_start():
	return('<form name="myform" action="/cgi-bin/enginePLS2.py" method="POST"')

def mainQues(ques):
	return('<div class="container"><h2>' + str(ques) + '</h2><br><ul>')

def finalPage(progLang, details, website, logo):
	#return('<br><h1 align="center"> You should learn ' + str(progLang) + ' : ' + str(details) + '</h1><br><br><h2 align="center"><a href="/index.html">HOME</a></h2>')
	final = '<!DOCTYPE html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>PLS2</title><link rel="stylesheet" href="/css/style2.css">'
	final += '</head><body><div id="particles-js" style="z-index: +1;"><div class="grid-container" style="border: 1px solid white; position: absolute;/*! margin-left: 25%; *//*! margin-right: 25% */">'
	final += '<div class="item1"><img src="/images/logos/' + str(logo) + '" style="height: 100%; width: auto;height: 137px; "></div><div class="item2"><h1 style="font-size: 3em;font-family: \'Itim\', cursive;">' 
	final += str(progLang) + '</h1></div><div class ="item3><h2 style="font-size: 1.5em">' + str(website) + '</h2></div><div class="item4"><a><center>' + str(details)
	final += '</a> </center></div><div class="item5"><center><div class="start"><a href="/index.html"><span style="font-size: 20px;">CHOOSE ANOTHER</span>'
	final += '</a></div></center></div></div></div><script src="/js/particles.js"> </script><script src="/js/app.js"> </script></body></html>'
	return(str(final))

def radio_start(rb_id, rb_name, rb_value):
	return('<li><input type="radio" id="' + str(rb_id) + '" name="' + str(rb_name) + '" value="' + str(rb_value) + '" onclick="setTimeout(submitform, 500)">')

def radio_end(rb_id, rb_text):
	return('<label for="' + str(rb_id) + '">' + str(rb_text) + '</label><div class="check"><div class="inside"></div></div></li>')

def credits():
	return('<li><div class="signature"><p><br><br>Made with <i class="much-heart"></i> by Mansi, Aman and Shashank</p></div></li>')
	
def form_end():
	return('<ul></div></form>')

def foot():
	return('</body></html>')

def HackingAttempt():
	""" Code for the Bad Request/Hacking Attempt goes here """
	#return('<br><h1 align="center"> Hacking Attempt Detected : You will be banned </h1>')
	hack = '<!DOCTYPE html><html><head><title>HACKING INTERUPT!</title><link rel="stylesheet" href="/css/hack.css"></head><body><div class="container">'
	hack += '<img src="/images/hack.png" style="" class="images"><br /><span>HACKING ATTEMPT DETECTED<br />YOU WILL BE BANNED!</span></div></body></html>'
	return(hack)
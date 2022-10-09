### TODO:
### Add more Facebook commands
### Add more Tumblr commands
### Add in Twitter API

import facebook
import sys
import os
import pytumblr

#need your own access token to use facebook stuff
#go to https://developers.facebook.com/tools/ then click "Graph API Explorer" for your personal access token
token = 'your token here'

client = pytumblr.TumblrRestClient(
'[]',
'[]',
'[]',
'[]'
)

#function to restart script after a command is complete
def restart():
	py = sys.executable
	os.execl(py, py, * sys.argv)

command = raw_input("> ")

if command == 'quit':
	sys.exit()

##tumblr stuff
def tumblr():

 	client.info()
	print "Link your blog: "
	blog = raw_input("> ")

	def post_text():
		print "Whats on your mind? "
		text = raw_input("> ")
		client.create_text(blog, body=text)
		restart()

	def post_quote():
		user_quote = raw_input("> ")
		client.create_quote(blog, quote=user_quote)	
		restart()

	def post_link():
		user_link = raw_input("> ")
		client.create_link(blog, url=user_link)
		restart()

	if command == '!tumblr text':
		post_text()

	elif command == '!tumblr quote':
		post_quote()

	elif command == '!tumblr link':
		post_link()

if command[:7] == '!tumblr':
	tumblr()
	
##Facebook stuff

def Fb():

	graph = facebook.GraphAPI(token)
	profile = graph.get_object("me")
	friends = graph.get_connections("me", "friends")

	def update():
		new_status = raw_input("> ")
		graph.put_object("me", "feed", message=new_status )
		restart()


if command == 'help':
	print """	
commands:
!fb status - posts a facebook status
!tumblr text - creates tumblr text post
!tumblr quote - creates tumblr quote post
!tumblr link - creates tumblr link post
quit - exits the program
		"""
	restart()

if command == '!fb status':
	command = fb()
	command.status()

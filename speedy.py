### TODO:
### Add more Facebook commands
### Have it pull Facebook Acess Tokens automatically
### Add more Tumblr commands
### Add in Twitter API

import facebook
import sys
import os
import pytumblr

#need your own access token to use facebook stuff
#go to developers.facebook.com/tools/explorer/ for your personal access token
token = 'your token here'

client = pytumblr.TumblrRestClient(
	'n5r51TdkdkOeDdzf5aGA0GMPkobDiddHkytZU55CceSUNr1Rri',
	'qUMJUNKoZfdomw5nUZ3kXD1SRFgXEnHCCJdleVlVAnZg1MxVCv',
	'6KV4oayviBIiUhfCJ6EQIFPkhEG1fSc2YKTxTlryBhlXpckkxZ',
	'kBzG3Qu5h4BHaMNG204rorvnUoCDMFzyuPVgn7X9WtlIXRh7fd'
)

#function to restart script after a command is complete
def restart():
	py = sys.executable
	os.execl(py, py, * sys.argv)

command = input("> ")


##tumblr stuff
class tumblr(object):

 	client.info()
	print "Link your blog:  "
	blog = raw_input("> ")
	
	def post_text(self):
		print "Whats on your mind? "
		text = raw_input("> ")
	
		client.create_text(blog, body=text)
		restart()

	def post_quote(self):
		user_quote = raw_input("> ")
		client.create_quote(blog, quote=user_quote)	
		restart()

	def post_link(self):
		user_link = raw_input("> ")
		client.create_link(blog, url=user_link)
		restart()

##Facebook stuff

class Fb(object):

	graph = facebook.GraphAPI(token)
	profile = graph.get_object("me")
	friends = graph.get_connections("me", "friends")

	while prompt != 'quit':

	def update(self):
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

elif command == '!fb status':
	command = fb()
	command.status()

elif command == '!tumblr text':
	command = tumblr()
	command.post_text()

elif command == '!tumblr quote':
	command = tumblr()
	command.post_quote()
	
elif command == '!tumblr link':
	command = tumblr()
	command.post_link()

elif command == 'quit':
	sys.exit()

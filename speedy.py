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


print "1. Tumblr \n2. Facebook\n3. Quit"
site_prompt = input("> ")


##tumblr stuff
def tumblr():

 	client.info()
	print "Link your blog:  "
	blog = raw_input("> ")
	
	print "1. Create text\n2. Create quote\n3. Create Link"
	tumblr_prompt = input("> ")
	
	if tumblr_prompt == 1:
		print "Whats on your mind? "
		text = raw_input("> ")
	
		client.create_text(blog, body=text)
		restart()

	elif tumblr_prompt == 2:
		user_quote = raw_input("> ")
		client.create_quote(blog, quote=user_quote)	
		restart()

	elif tumblr_prompt ==  3:
		user_link = raw_input("> ")
		client.create_link(blog, url=user_link)
		restart()

##Facebook stuff

def Fb():

	graph = facebook.GraphAPI(token)
	profile = graph.get_object("me")
	friends = graph.get_connections("me", "friends")

	print "1.Update status \n2.Check amount of friends"

	prompt = input("> ")

	if prompt == 1 or prompt == 2:
		pass
	else:
		assert False


	while prompt != 'quit':

	def update():
		new_status = raw_input("> ")
		graph.put_object("me", "feed", message=new_status )
		prompt = 5		
		restart()

	##function doesn't work right now 
	def number_friends():

		friend_list  = len([friend['name'] for friend in friends['data']])
		print friend_list
		restart()

	if prompt == "!fb status":
		update()

	else:
		assert False


if site_prompt == 1:
	tumblr()

elif site_prompt == 2:
	Fb()

elif site_prompt == 3:
	sys.exit()


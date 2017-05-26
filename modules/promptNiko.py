import slackConnector
import random
import os

slackUserId = os.environ.get('user_id')
slackUserName = os.environ.get('user_name')

user = "<@{0}|{1}>".format(slackUserId, slackUserName)

questions = [
	"Cousin {0}, I have not hung out with you in a long time.",
	"{0}, you pick up. It has been a time since we spoke.",
	"Cousin {0}, I am loving the bowling. Pick me up in next hour.",
	"{0}, this is a great American activity. We bowl together if you pick me up in next hour.",
	"We bowl like two cousins in American sitcom, {0}. Pick me up in next hour.",
	"{0} let's go bowling.",
	"{0} want to go bowling?",
	"Bowling, {0}. This is a surprise. You know that I like to beat you tough. Let's do it.",
	"{0} let's play darts.",
	"{0}, I am thinking we should be playing some darts together. We have not done this in Liberty City yet.",
	"{0}, how about we go drink some vodka? Meet me at Dunkirk in one hour.",
	"How about we try to numb the pain with vodka, {0}? Meet me at Dunkirk in one hour",
	"I was thinking my liver was having an easy time, {0}. We drink together. Come get me in next hour.",
	"Cousin {0}, we should go out together. Open a bottle of vodka and drink it all like we did in Old Country.",
	"We should go and get drunk together {0}.",
	"Ahh, Comrades! {0} We shall raise our glasses to the late Vlad while we're here. Where are you? Are you coming to Dunkirk?",
	"Cousin {0}, we are family. We should be like family and eat together. How about it?",
	"{0} we should eat together.",
	"Cousin {0}, we are family. We should be like family and eat together. How about it?",
	"Cousin, you really want to experience Australia, you must see a show here. How about it {0}?"
	]

def askQuestion():
	question = random.choice(questions)
	slackConnector.sendMessage(question.format(user))

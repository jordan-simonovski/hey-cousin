import requests
import json
import os

slackWebhook = os.environ.get('slack_webhook')

def buildMessage(question):
	slackMessage = {
		"response_type": "in_channel",
		"attachments": [{
			"title": "Cousin Roman is calling...",
			"text": question,
			"color": "#3AA3E3",
			"attachment_type": "default",
			"thumb_url": "http://i.imgur.com/Y30Zv5D.jpg"
		}]
	}
	return json.dumps(slackMessage)

def sendMessage(question):
	slackMessage = buildMessage(question)
	response = requests.post(slackWebhook, data=slackMessage)
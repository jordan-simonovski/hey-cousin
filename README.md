# Hey Cousin

Do you want to go bowling?

## What is this? 

I made a slackbot to annoy a friend called Niko. The app randomly chooses from Roman Bellic's dialogue, and send a message to a channel on slack. I've made it generic enough to be able to annoy basically any one person you might know in Slack.

## First tweak your zappa_settings.json

In the environment variables, you'll need to Slack Webhook URL that you get when setting up the application in Slack. 

User ID is a bit of a tricky one. I haven't bothered to automate this, but you can actually get a Slack User's ID from the web interface when you right click their name and inspect element. This is needed to tag them.

User Name is the slack user's name.

You might also want to tweak the cron expression depending on which timezone you're in. Keep in mind that AWS Cron uses the UTC timezone.

```
{
    "dev": {
        "app_function": "run.app", 
        "aws_region": "ap-southeast-2", 
        "profile_name": "aws profile", 
        "s3_bucket": "zappa-hey-cousin-slackbot",
        "environment_variables": {
            "slack_webhook": "webhookurl",
            "user_id": "slack user id",
            "user_name": "niko"
        },
        "events": [
            {
               "function": "run.heyNiko", 
               "expression": "cron(45 1 * * ? *)" 
            }
        ]
    }
}
```


## How to Deploy

```
cd hey-cousin/
virtuelenv env

pip install -r requirements.txt
zappa deploy dev
```

## Test it Out

```
zappa invoke dev run.heyNiko
```
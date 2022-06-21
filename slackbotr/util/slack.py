from slack_sdk import WebClient

from slackbotr.constants.token import SLACKBOT_USER_OAUTH_TOKEN

web_client = WebClient(token=SLACKBOT_USER_OAUTH_TOKEN)

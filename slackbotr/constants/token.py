import os


try:
    SLACKBOT_USER_OAUTH_TOKEN = os.environ['SLACKBOT_USER_OAUTH_TOKEN']
except Exception as e:
    raise RuntimeError('SLACKBOT_USER_OAUTH_TOKEN envvar must be populated.')

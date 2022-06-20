"""An example slackbot that simply sends "Hello world" to the configured channel.

NOTE: Channel is configured in the Slack Application configuration, not in the bot
itself.
"""
from fastapi.responses import HTMLResponse
from slack_sdk.errors import SlackApiError

from slackbotr.routers import slackbots_router
from slackbotr.util.slack import web_client


@slackbots_router.get('/test', response_class=HTMLResponse)
async def root() -> str:
    # Based on: https://slack.dev/python-slack-sdk/web/index.html#messaging
    # I don't really fully understand the error-handling portion.
    # TODO: refactor?
    try:
        response = web_client.chat_postMessage(
            channel="C03KZ8SHCTH",  # This is #slackbotr-testing
            text="Hello world! :tada: :left_speech_bubble: :earth_asia:",
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'

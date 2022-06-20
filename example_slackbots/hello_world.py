"""An example slackbot that simply sends "Hello world" to the configured channel.

NOTE: Channel is configured in the Slack Application configuration, not in the bot
itself.
"""
from fastapi import HTTPException
from slack_sdk.errors import SlackApiError

from slackbotr.routers import slackbots_router
from slackbotr.util.slack import web_client


@slackbots_router.get('/test')
async def root() -> str:
    try:
        response = web_client.chat_postMessage(
            channel="C03KZ8SHCTH",  # This is #slackbotr-testing
            text="Hello world! :tada: :left_speech_bubble: :earth_asia:",
        )
    except SlackApiError as e:
        raise HTTPException(status_code=500, detail=e.response["error"])

    # TODO: Abstract away error-handling and standardized responses from the slackbot
    # interface.
    return {'message': 'ok'}

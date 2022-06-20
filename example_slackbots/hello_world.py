"""An example slackbot that simply sends "Hello world" to the configured channel.

NOTE: Channel is configured in the Slack Application configuration, not in the bot
itself.
"""
from fastapi.responses import HTMLResponse

from slackbotr.routers import slackbots_router


@slackbots_router.get('/test', response_class=HTMLResponse)
async def root() -> str:
    return "I work!"
    # TODO: Post a message to slack

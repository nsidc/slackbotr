from fastapi import APIRouter

from slackbotr.util.import_helpers import import_slackbot_endpoints


slackbots_router = APIRouter(
    prefix='/bots',
    tags=['slackbot'],
)

import_slackbot_endpoints()

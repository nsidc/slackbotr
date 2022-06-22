from fastapi import APIRouter, Depends

from slackbotr.util.auth import JWTBearer
from slackbotr.util.import_helpers import import_slackbot_endpoints

slackbots_router = APIRouter(
    prefix='/bots',
    dependencies=[Depends(JWTBearer())],
    tags=['slackbot'],
)

import_slackbot_endpoints()

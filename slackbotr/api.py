from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, ORJSONResponse

from slackbotr.constants import VERSION
from slackbotr.routers import slackbots_router

DESCRIPTION = """
❄️  A slackbot host ❄️
"""

api = FastAPI(
    title='slackbotr',
    description=DESCRIPTION,
    version=VERSION,
    # `orjson` will convert `NaN`s (which are invalid JSON) to `nulls` when
    # dumping. It is also more performant and correct than other JSON libraries.
    #     https://github.com/ijl/orjson#float
    default_response_class=ORJSONResponse,
)

api.add_middleware(
    CORSMiddleware,
    # TODO: consider more restrictive CORS settings.
    # See: https://fastapi.tiangolo.com/tutorial/cors/
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@api.get('/', response_class=HTMLResponse)
async def root() -> str:
    return (
        "Welcome to slackbotr. View the <a href='./docs'>API docs</a>"
        " to see available endpoints."
    )


api.include_router(slackbots_router)


if __name__ == '__main__':
    # Run this script directly for debugging. See documentation for more info.
    import uvicorn

    uvicorn.run(
        # Normally, we'd just pass in `api` here, but `reload=True` requires the
        # string:
        '__main__:api',
        host='0.0.0.0',
        port=5000,
        reload=True,
    )

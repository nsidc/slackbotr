# slackbotr

A framework for hosting Slackbots. The name is temporary; we couldn't think of one and
we thought this was funny.


## Testing

Set up a testing Slack Application (see "Configuration of Slack") for your workspace.
Ensure that you have "installed" your application to your workspace! Set the environment
variables needed by `docker-compose.yml` and then bring up the stack with
`docker-compose up -d`.


## Usage

Build your Slackbots as Python files in an independent directory (not in this repo),
then mount them to `/slackbots` in this application container. The app will analyze
those files, looking for a specific interface (functions, classes, TBD; similar to how
PyTest finds tests, this app finds bots. Currently, it expects to find FastAPI endpoints
in each file). See `./example_slackbots` for inspiration creating your own.

For each file containing a compliant interface, a new endpoint is created within
`slackbotr`, e.g.: for `/slackbots/foo.py`, an endpoint `<HOSTNAME>/foo` will be
created.

Each endpoint expects to be called with an authentication token (NOTE: TODO).

For simple bots that send a message that depends on no inputs, the endpoint requires no
data. For complex bots that respond to commands in Slack, the endpoint requires standard
format JSON data.


### Configuration of Slack

To make a Slackbot work with a Slack Workspace, you must create a Slack "Application".
This terminology is confusing, but a Slack Application represents the configuration that
authorizes (using an oauth token) your Slackbot to interact with your workspace.

Install the application to your workspace. NOTE: Multiple workspaces are currently not
supported!

NOTE: It can be difficult to find the correct application administration page. To get
there, visit <https://api.slack.com/apps>.


#### Scopes

We added `chat:write`, `chat:write.customize`, and `chat:write.public` scopes.


#### Token

The token must be populated in the `SLACKBOT_USER_OAUTH_TOKEN` envvar.


### Sending a message

Use the Slack SDK to send a message. `slackbotr` provides a client pre-configured with
the oauth token provided by the environment variable.

```
from slackbotr.util.slack import web_client

web_client.chat_postMessage(
    channel="C0XXXXXXXXX",  # See below to learn how to get a channel ID
    text="Hello world! :tada: :left_speech_bubble: :earth_asia:",
    username="slackbotr EXAMPLE",
    icon_emoji=":hammer_and_wrench:",
)
```

#### Getting a channel ID

It's important to use channel IDs when writing slackbots, as channels can be renamed.
You don't want that to break your bot!

In Slack, right-click on a channel name in your left panel and select Copy URL. You
should get a URL like:

```
https://your-workspace.slack.com/archives/C0XXXXXXXXX
```

Copy the last part in the format `C0XXXXXXXXX`. This is your channel ID.


# TODO:

* How to enable external services, e.g. CircleCI to communicate with this app? Use a
  security token decorator? ¯\_(ツ)_/¯
* Create a more mature interface for the slackbots instead of creating FastAPI endpoints
  within each slackbot. We could expect a particular class to be defined for each
  slackbot, and abstract away things like:
  * Error handling
  * Standardized response messages and codes
* Authentication: currently anyone can spam our slack by hitting endpoints.

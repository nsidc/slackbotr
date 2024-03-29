# slackbotr

A framework for hosting Slackbots. The name is temporary; we couldn't think of one and
we thought this was funny.

NOTE: We're not actively developing this solution anymore, as we've discovered existing
alternatives, e.g. `slack-machine` and `errbot`.


## Level of Support

This repository is not actively supported by NSIDC but we welcome issue submissions and 
pull requests in order to foster community contribution.

See the [LICENSE](LICENSE) for details on permissions and warranties. Please contact 
nsidc@nsidc.org for more information.

NOTE: This software is in the early stages of development -**DO NOT USE IN PRODUCTION**.


## Requirements

This package requires:

* docker


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


#### Slack OAuth Token

The Slack authentication token must be populated in the `SLACKBOT_USER_OAUTH_TOKEN`
envvar.


#### Scopes

We added `chat:write`, `chat:write.customize`, and `chat:write.public` scopes.


#### Slash commands

These must be configured within the Slack Application before your slackbots can use
them. Additionally, the `slackbotr` instance must be exposed to the public Internet so
Slack can send it a request with data from the user's command.


### Sending a message (one-way communication)

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


### Interactivity (two-way communication)

https://api.slack.com/interactivity


## License

See [LICENSE](LICENSE).

## Code of Conduct

See [Code of Conduct](CODE_OF_CONDUCT.md).

## Credit

This software was developed by the National Snow and Ice Data Center with funding from multiple sources.


# TODO:

* Come up with a better name! Maybe this isn't so much for aggregating slackbots, but
  general triggered (webhook, cron, human, ???) behaviors (bots) we'd want to execute on
  an internal network? e.g.  CircleCI triggers this application to run a bot that sends
  data to an application or service which isn't publicly accessible, like an internal
  workflow management system or Jenkins machine (accessible by running `slackbotr` on
  the same internal network), or a Slack Application installed in a private Slack
  Workspace (accessible by providing access tokens via environment variables to your
  bots).
  * Once this project knows what it wants to be, review all content in this repository
    and re-organize for simplicity.
  * Why are we making this and not using an off-the-shelf task runner like
    Drone/Jenkins? Is the simplicity of delivering bots as a directory of Python
    scripts the main reason to build this?
* Create more example bots that exemplify common use cases:
  * Two-way communication (See `ARCHP-9` in Jira):
    * Bots that accept Slack slash commands
    * Bots that receive data from external service, e.g. CircleCI job could CURL
      arbitrary JSON to the slackbot, on which it could act to format a message or
      trigger other stuff that CircleCI couldn't.
* Create a more mature interface for the slackbots instead of creating FastAPI endpoints
  within each slackbot. We could expect a particular class to be defined for each
  slackbot, and abstract away things like:
  * Error handling
  * Standardized response messages and codes
* **Authentication**
  * Do we need to support multiple tokens each with different scopes of access? Can we
    safely use data within tokens to authorize scopes? It could be as simple as defining
    a `scope=...` parameter when instantiating a bot, and generating tokens with
    `{"scope": "..."}`.
  * Do we need to have a database of tokens that can be revoked? With stateless tokens,
    e.g. JWTs, all tokens generated with the same secret key must be revoked at once. So
    JWTs would be a poor choice if we need granular revocation.
  * JWTs contain encoded, _not encrypted_, data. We don't send anything sensitive at the
    moment and we must be cautious not to change the code in the future to include
    sensitive data within tokens.
* A history endpoint that displays the recently-received triggers and their data? A
  Slack command to print the history of triggers?

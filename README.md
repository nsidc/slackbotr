# slackbotr

A framework for hosting Slackbots. The name is temporary; we couldn't think of one and
we thought this was funny.


## Testing

Set up a testing Slack Application (see "Configuration of Slack") for your workspace.
Create an internal webhook to your testing channel. Set the environment variables used
by `docker-compose.yml` and then bring up the stack with `docker-compose up -d`.


## Usage

Build your Slackbots as Python files in an independent directory, then mount them to
`/slackbots` in this application's container. The app will analyze those files, looking
for a specific interface (functions, classes, TBD; similar to how PyTest finds tests,
this app finds bots). See `./example_slackbots` for inspiration creating your own.

For each file containing a compliant interface, a new endpoint is created within
`slackbotr`, e.g.: for `/slackbots/foo.py`, an endpoint `<HOSTNAME>/foo` will be
created.

Each endpoint expects to be called with an authentication token. For simple bots that
send a message that depends on no inputs, the endpoint requires no data. For complex
bots that respond to commands in Slack, the endpoint requires standard format JSON data.


### Configuration of Slack

To make a Slackbot work with a Slack Workspace, you must create a Slack "Application".
This terminology is confusing, but a Slack Application represents the configuration that
authorizes (using an authentication token) your Slackbot to interact with your
workspace. 

Install the application to your workspace.


#### Scopes

We added `chat:write`, `chat:write.customize`, and `chat:write.public` scopes.


#### Token

The token must be populated in the `SLACKBOT_USER_OAUTH_TOKEN` envvar.


### Sending a message


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
* ...

# slackbotr

A framework for hosting Slackbots. The name is temporary; we couldn't think of one and
we thought this was funny.

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

## Development

Bring up the stack:

```
docker-compose up -d
```

View the logs:

```
docker-compose logs -f
```


### Update the environment

Add a new dependency to `environment.yml`.

Update the installed environment:

```
conda env update -n slackbotr
```

Update the environment lockfile:

```
inv env.lock
```

**NOTE**: Don't forget to rebuild the docker images after updating the lockfile:

```
docker-compose build
```


### Format the code

```
inv format
```


### Testing / static analysis 

Start the suite of static analysis and tests:

```
inv test
```

Learn more about available tests:

```
inv --list
```


#### Testing the example slackbots

Set up a testing Slack Application (see "Configuration of Slack") for your workspace.
Ensure that you have "installed" your application to your workspace! Set the environment
variables needed by `docker-compose.yml` and then bring up the stack with
`docker-compose up -d`.

**NOTE**: Testing _interactions_ (two-way communications, as opposed to simply sending
messages to Slack from a bot) is only possible if your `slackbotr` instance is
available on the public Internet. Slack has to be able to send messages to your bot.


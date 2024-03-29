# Hello Prometheus 🔥

Welcome 👋

This repository stores everything needed for a quick Prometheus "Hello World"
live-coding / demo ⚡

---

## Requirements

In order to understand this demo, participants are expected to have some
theoretical knowledge of Prometheus and associated tooling beforehand.

The bare minimum is to know about:

- The Prometheus metrics format
- The _pull_ approach that Prometheus promotes
- A bit of the "internals" of Prometheus - roughly how it works
- The main components of most common stacks: Prometheus, AlertManager, Grafana

---

## Demo flow

Here is the steps/flow of the demo:

1. Automagic instrumentation for tech metrics (with Flask)
2. `curl` + explanations
3. Manual instrumentation for business metrics (Python Prometheus client SDK)
4. `curl` + explanations
5. Prometheus bootstrap
    - `docker-compose.yml`
    - `prometheus.yml` for scraping config and service discovery
    - Show off of external sample using Kubernetes annotations for service
      discovery
6. Prometheus UI quick walkthrough
7. `curl` Prometheus query
8. Grafana bootstgrap
    - `docker-compose.yml`
    - Datasource manual addition
    - Dashboard JSON import
9. Manual addition of a Grafana panel
10. `curl` to generate requests and see graph changes
11. AlertManager bootstrap
    - ?
12. Trigger an Alert - _(idea:
    `nb_jokes > 10` = "The number of jokes is too damn high!" ?)_
13. Slack notification?

## Demo app

- Number of jokes (counter)
- Number of channel members (gauge)
- Number of reaction emoji with label for joke "ID"
- Tech metrics
    - Number of calls
    - Response time
    - Failure rate
    - ...

## 🚀 Run it yourself - How-to

Want to run it yourself? Cool!

### Requirements

In order to run this hello-world yourself, you'll need:

- **Docker** >= 19.03 _(otherwise, try to lower the `docker-compose.yml`
  `version`)_
- **Docker Compose** >= 1.27 _(might work with lower versions, didnt't test for
  it)_
- **Python 3**

### Running the app

```shell
# Setup your virtualenv
virtualenv --python=python3 venv

# Enable it
source ./venv/bin/activate

# Install required libraries
pip install -r requirements.txt.lock

# Run the app!
python ./app.py
```

Well done! The demo app is now available on port `5000`

### Querying metrics

Yay, your app is exposing metrics!

Query them with your favorite HTTP client:

```shell
# Using curl
curl http://localhost:5000/metrics

# Using httpie
http http://localhost:5000/metrics
```

### Querying the app

For simplicity of this hello-world, all the routes are using GET.

Here are some example calls:

```shell
# Jokes
curl "localhost:5000/jokes"                       # Get all the jokes
curl "localhost:5000/add_joke?joke=My new joke"   # Add a joke
curl "localhost:5000/add_reaction?joke_id=xxx"    # Add a reaction to a joke

# Members
curl "localhost:5000/members"                         # Get all the channel members
curl "localhost:5000/add_member?member=My new member" # Add a channel member
curl "localhost:5000/remove_member?member_id=xxx"     # Remove a channel member
```

## Available metrics

Here are the available metrics exposed by the app:

- TODO

### Starting components

Some components in the `docker-compose.yml` might be commented out, because we
toggle them progressively when demo-ing this hello-world.

In order to start the stack, simply run:

```shell
docker-compose up
```

... and add the `-d` option if you want it to run in the background.

If you need more, take a look at the [Docker Compose
documentation](https://docs.docker.com/compose/gettingstarted/https://docs.docker.com/compose/gettingstarted/)

You will end up with:

- **Alertmanager** available on port `9093`
- **Prometheus** available on port `9090` 
    - scraping `localhost:5000` (the app)
    - scraping `localhost:9090` (Prometheus itself)
    - sending alerts to `localhost:9093` (Alertmanager)
- **Grafana** available on port `3000`

### Querying Prometheus

You can query prometheus using your favorite HTTP client:

```shell
# Using curl
curl 'https://localhost:9090/api/v1/query?query=<QUERY>'

# Using httpie
http 'https://localhost:9090/api/v1/query?query=<QUERY>'
```

Where `<QUERY>` is, well, your query.

### 🔗 Links summary

- App: <http://localhost:5000>
- Alertmanager: <http://localhost:9093>
- Prometheus: <http://localhost:9090>
- Grafana: <http://localhost:3000>

# Hello Prometheus

Welcome :)

## Run it yourself - How-to

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
curl https://localhost:5000/metrics

# Using httpie
http https://localhost:5000/metrics
```

### Starting components

Some components in the `docker-compose.yml` are commented out, because we
toggle them progressively when demo-ing this hello-world.

In order to start the stack, simply run:

```shell
docker-compose up
```

... and add the `-d` option if you want it to run in the background.

If you need more, take a look at the [Docker Compose
documentation](https://docs.docker.com/compose/gettingstarted/https://docs.docker.com/compose/gettingstarted/)

---

You will have:

- **Prometheus** available on port `9090` and scraping `localhost:5000`
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

### Links summary

- App: <http://localhost:5000>
- Prometheus: <http://localhost:8080>
- Grafana: <http://localhost:3000>

## Demo flow

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
12. Trigger an Alert
13. Slack notification?

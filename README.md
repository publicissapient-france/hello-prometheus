# Hello Prometheus

Welcome :)

## Run it yourself - How-to

### Requirements

In order to run this hello-world yourself, you'll need:

- **Docker** >= 19.03 _(otherwise, try to lower the `docker-compose.yml`
  `version`)_
- **Docker Compose** >= 1.27 _(might work with lower versions, didnt't test for
  it)_

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

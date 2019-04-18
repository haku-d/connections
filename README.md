# connections demo

A demo app showing a simple service using flask and some supporting packages

### Requirements

 * Docker CE >= 17.04

### Stack Information

* python flask
* pipenv (for package management rather than virtualenv capabilities)
* mysql
* nginx + gunicorn

**All API calls will go through nginx at http://localhost:5000. All the other services are handled within Docker's internal network and no other ports are exposed to the host machine.**

### Instructions

- Build and kick off all the services with docker-compose.

```
docker-compose up -d --build
```

 You can omit -d if you want to run it in the foreground and dump all logs from all containers into your terminal. Alternatively you can use ```docker logs <container name> -f``` to tail logs from a specific container.

You can use ```docker ps``` command to see the running containers. You should see 6 running containers. ** Don't forget to run the migrations provided in the next section.**

The folders **connections/** and **/migrations** are mounted from the host to the container. Any changes made from the host will propagate to the container and vice versa.

MySQL database creates its own volume that provides persistence in the case of rebuilding/restarting/stopping the containers. Those volumes are managed by Docker and not directly exposed to the developer.

Other useful commands for stopping, starting and restarting the services.

```
docker-compose stop | start | restart
```

- Migrate the database
```
docker-compose exec connections flask db upgrade
```

- Run tests
```
docker-compose exec connections pytest
```

- Lint code for style violations
```
docker-compose exec connections flake8 .
```


# docker-flask-mysql-mongodb-redis-sample

>A setup example of Flask, MySQL, MongoDB and Redis containerized with Docker.


## Requirements

- docker
- docker-compose


## Notes

This is just an example of how to link database and cache docker containers with
a python Flask server container. The server exposes endpoint for testing each of
the database and cache services.


## Usage

Start up the containers:
```sh
source up.sh
```

Navigate to localhost URLs to test db and cache connections:
```sh
http://localhost:500/get-mysql
http://localhost:500/get-mongo
http://localhost:500/get-redis
```






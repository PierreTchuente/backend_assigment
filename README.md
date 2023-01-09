# backend_assigments

# How To Use Repo
This is the backend api runing a pyramid app on uwsgi server with nginx as proxy server


### Setup on local machine
You will need to have docker running on your machine:
This app is running on python 3.7
1. `docker-compose build`, to build the api and nginx image
2. `docker-compose up` to start the proxy server and the api
3. `docker-compose down` to stop both container

## Making request to the API

# Packer4Santa

A CRUD webservice for Santa to manage packages and elves

### Resources

- [Docker Hub](https://hub.docker.com/r/sidll/packer4santa)
- [Deployed Service](https://oyster-app-8l2ig.ondigitalocean.app/docs)

## Key Concepts used in the repository

- GitHub Actions workflow pushing the container image to Docker Hub
- FastAPI with SQLite as database
- handling GET, POST, PUT and DELETE HTTP requests

## How to run

### Docker

Build the image

```shell
docker build <image-name>
```

Run the container

```shell
docker run <image-name>
```

You should be able to access the service at

```
http://0.0.0.0:8000/
```

If `0.0.0.0` doesn't work for you, adjust the IP address in [Dockerfile](Dockerfile)

### Shell

Requires `Python 3.10` or compatible

#### Virtual Environment (Optional)

Create a virtual environment

```shell
python -m venv .\.venv
```

And activate it

##### Windows

```shell
.\.venv\Scripts\activate.ps1
```

##### Linux

```shell
source ./venv/bin/activate
```

#### Run

Install the required packages

```shell
pip install -r requirements.txt
```

And start the service

```shell
uvicorn main:app --reload
```


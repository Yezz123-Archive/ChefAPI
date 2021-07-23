![ChefAPI](.github/img/header.svg)

<p align="center">
    <a href="https://github.com/GDGSNF/ChefAPI/actions/workflows/docker-publish.yml">
    <img alt="Docker" src="https://github.com/GDGSNF/ChefAPI/actions/workflows/docker-publish.yml/badge.svg?branch=main"/></a>
    <a href="https://github.com/GDGSNF/ChefAPI/actions/workflows/docker-image.yml">
    <img alt="Docker Image CI" src="https://github.com/GDGSNF/ChefAPI/actions/workflows/docker-image.yml/badge.svg?branch=main"></a>
</p>

# ChefAPI

API using FastAPI and PostgreSQL to create and share or keeping track of awesome food recipes. Our API have aslo a Crud System Using JWT and Oauth2 to Create a Complete API that Can Be Used with a High Quality Frontend Project. ⛏

## Getting Started

- To start using ChefAPI You need some experience in Cuisine maybe how to create a Moroccan `CousCous` or `Tajine`.

### Prerequisites

- Python 3.8.6 or higher
- PostgreSQL
- FastAPI
- Docker

### Project setup

```sh
# clone the repo
$ git clone https://github.com/GDGSNF/ChefAPI

# move to the project folder
$ cd ChefAPI
```

### Creating virtual environment

- Install `pipenv` a global python project `pip install pipenv`
- Create a `virtual environment` for this project

```shell
# creating pipenv environment for python 3
$ pipenv --three

# activating the pipenv environment
$ pipenv shell

# if you have multiple python 3 versions installed then
$ pipenv install -d --python 3.8

# install all dependencies (include -d for installing dev dependencies)
$ pipenv install -d
```

### Configured Enviromment

#### Database

- Using SQLAlchemy to Connect to our PostgreSQL Database
- Containerization The Database.
- Drop your PostgreSQL Configuration at the `.env.sample` and Don't Forget to change the Name to `.env`

```conf
# example of Configuration for the .env file

POSTGRES_SERVER = localhost
POSTGRES_USER = root
POSTGRES_PASSWORD = password
POSTGRES_DB = ChefAPI
```

### Running the Application

- To run the [Main](main.py) we need to use [uvicorn](https://www.uvicorn.org/) a lightning-fast ASGI server implementation, using uvloop and httptools.

```sh
# Running the application using uvicorn
$ uvicorn main:app

# To run the Application under a reload enviromment use -- reload
$ uvicorn main:app --reload
```

## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the FastAPI app and then start the FastAPI app container.

```sh
$ docker build
```

- list all the docker images and you can also see the image `chefapi:latest` in the list.

```sh
$ docker images
```

- run the application at port 5000. The various options used are:

> - `-p`: publish the container's port to the host port.
> - `-d`: run the container in the background.
> - `-i`: run the container in interactive mode.
> - `-t`: to allocate pseudo-TTY.
> - `--name`: name of the container

```sh
$ docker container run -p 5000:5000 -dit --name ChefAPI chefapi:latest
```

- Check the status of the docker container

```sh
$ docker container ps
```

## Preconfigured Packages

Includes preconfigured packages to kick start ChefAPI by just setting appropriate configuration.

| Package                                                      | Usage                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [uvicorn](https://www.uvicorn.org/)        | a lightning-fast ASGI server implementation, using uvloop and httptools.           |
| [Python-Jose](https://github.com/mpdavis/python-jose) | a JavaScript Object Signing and Encryption implementation in Python.    |
| [SQLAlchemy](https://www.sqlalchemy.org/)  | is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. |
| [starlette](https://www.starlette.io/)   | a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.    |
| [passlib](https://passlib.readthedocs.io/en/stable/)  | a password hashing library for Python 2 & 3, which provides cross-platform implementations of over 30 password hashing algorithms         |
| [bcrypt](https://github.com/pyca/bcrypt/)               | Good password hashing for your software and your servers.    |
| [python-multipart](https://github.com/andrew-d/python-multipart) | streaming multipart parser for Python.   |

`yapf` packages for `linting and formatting`

## Contributing

- Join the ChefAPI Creator and Contribute to the Project if you have any enhancement or add-ons to create a good and Secure Project, Help any User to Use it in a good and simple way.

## License

This project is licensed under the terms of the MIT license.
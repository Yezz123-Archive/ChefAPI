<p align="center">
    <img src=".github/img/picture_.png" alt="ChefAPI">
</p>

<p align="center">
    <a href="https://github.com/GDGSNF/ChefAPI/actions/workflows/docker-publish.yml">
    <img alt="Docker" src="https://github.com/GDGSNF/ChefAPI/actions/workflows/docker-publish.yml/badge.svg?branch=main"/></a>
    <a href="https://github.com/GDGSNF/ChefAPI/actions/workflows/docker-image.yml">
    <img alt="Docker Image CI" src="https://github.com/GDGSNF/ChefAPI/actions/workflows/docker-image.yml/badge.svg?branch=main"></a>
</p>

# ChefAPI :rocket:

- An API using FASTAPI & Python-Jose & SQLAlchemy to create and share or keeping track of awesome food recipes.

- You can Sign Up / Login and share with others Your awesome Food Recipes.

- Using PostgreSQL as a DataBase and Docker for containerization.

- Easy to use and Simple to track No Bad Code :heart:

## Requirements :rocket:

- To start using ChefAPI You need some experience in Cuisine maybe how to create a Moroccan CousCous or Tajine :laughing: , But also you need this:

- [Docker](https://www.docker.com/)

- [PostgreSQL](https://www.postgresql.org/)

- [Python](https://www.python.org/)

### Installation

- Get started by cloning the repository :

```bash
git clone https://github.com/GDGSNF/ChefAPI.git
```

- Create & activate a python3 [virtual environment](https://docs.python.org/3/tutorial/venv.html) (optional, but very recommended).

- Install [requirements](requirements.txt):

```bash
pip install -r requirements.txt
```

## Get Started :rocket:

- An API with a High Quality of Code based on FastAPI is built on a Python framework called Starlette which is a lightweight ASGI framework/toolkit, which is itself built on Uvicorn.

- Using SQLAlchemy to Connect to our PostgreSQL Database :heart:

```py
    POSTGRES_SERVER: str = Field(..., env="POSTGRES_SERVER")
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )
```

- containerization for the Database and also for the FastAPI project.

> Docker-compose.yaml

```docker
version: "3.8"

services:
  db:
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
  web:
    build: .
    command: python main.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

- Connect and Install your PostgreSQL Container using the [dockerfile](database/Dockerfile) :

```docker
# syntax=docker/dockerfile:1
FROM ubuntu:16.04

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >/etc/apt/sources.list.d/pgdg.list

RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

USER postgres

RUN /etc/init.d/postgresql start && \
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" && \
    createdb -O docker docker

RUN echo "host all  all    0.0.0.0/0  md5" >>/etc/postgresql/9.3/main/pg_hba.conf

RUN echo "listen_addresses='*'" >>/etc/postgresql/9.3/main/postgresql.conf

EXPOSE 5432

VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]
```

- To run the project you need docker-compose and run this command:

```bash
docker-compose up -d
```

- To stop:

```bash
docker-compose down
```

## Contributing ⭐

- Contributions are welcome :heart:

- Please share any features, and add unit tests!

- Use the pull request and issue systems to contribute.

## Credits & Thanks 🏆

<p align="center">
    <a href="https://yassertahiri.medium.com/">
    <img alt="Medium" src="https://img.shields.io/badge/Medium%20-%23000000.svg?&style=for-the-badge&logo=Medium&logoColor=white"/></a>
    <a href="https://twitter.com/THyasser1">
    <img alt="Twitter" src="https://img.shields.io/badge/Twitter%20-%231DA1F2.svg?&style=for-the-badge&logo=Twitter&logoColor=white"</a>
    <a href="https://discord.gg/2x32TdfB57">
    <img alt="Discord" src="https://img.shields.io/badge/Discord%20-%237289DA.svg?&style=for-the-badge&logo=discord&logoColor=white"/></a>
</p>

# Sample Data Source
This creates a dummy data source using PostgreSQL and inserts some mock data.

## Project Structure
```
.
├── app # Contains logic to create mock data on source database
│   ├── Dockerfile
│   └── app.py
└── etl # Contains logic to do dummy ETL on source database
    ├── Dockerfile
    ├── etl.py
    └── requirements.txt
```

## Usage
Start the database and mock data, so there's a source to pull data from
```
$ docker-compose -f database.yaml up -d
```

Build the ETL image and push to Docker Hub (to be run anywhere with Docker Engine)
```
$ bash build_etl.sh
```

To test run the built ETL image
```
# --network is set to "host" to if database is on the Host OS
# `python etl.py` is the command we want to run on the container 
$ docker run --network="host" -it mavx/sampledatasource_etl:latest python etl.py
```

To kill the composed services cleanly
```
$ docker-compose -f database.yaml down -v # Removes mounted data volume created by DB too
```

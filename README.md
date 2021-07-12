# Kanban Board Backend

## Description

This is the example of usage Serverless framework:
Kanban-board (Backend: Python/Serverless Framework)

Full description [Here](EN_Test_task_Kanban_board_Backend_Python_Serverless_docx.pdf)

## Structure of the code

- [serverless.yml](serverless.yml) Describes serverless framework configurations including endpoints.
- [requirements.txt](requirements.txt) All requirements for an AWS Lambda docker container.
**For proper usage all dependencies you have to use [this plugin](https://www.serverless.com/plugins/serverless-python-requirements)**

### db

Database related config.

- [docker-compose.yml](db/docker-compose.yml) The local setup of PostgreSQL DB.
- [init.sql](db/init.sql) This script will be run automatically before the DB initialization (local stage).
It has to be executed on a PROD DB before usage.
- prod_postgres_config.env: You have to write it by you own. 
Config file with credentials to a PostgreSQL DB. 
**prod** is a part of the file name that is pointing to a stage. 
Stage have to be defined in the KANBAN_BOARD_STAGE env. variable. 
By default, it was defined in the serverless.yml file. 
It could be replaced if you are working at local/dev stage. 

example of local stage <local_postgres_config.env>: 

```shell script
POSTGRES_DB=test
POSTGRES_USER=test
POSTGRES_PASSWORD=test_pass
POSTGRES_HOST=localhost
```

### task

All logic and models related to the tasks.

### test_requests

Examples of the JSON-files that could be used for testing AWS Lambda functions locally/remotely. 

## Databases

For the local testing we could use db\docker-compose.yml and PostgreSQL inside it.
Production database have to be setup in advance. 
It could be Amazon RDS. 

## Backend

The Serverless framework with AWS Lambda. 

## Endpoints

All endpoints act as HTTP POST requests and consume JSON with parameters.

- new: {"task":"<TASK_NAME>"}
- start: {"task":"<TASK_NAME>"}
- resolve: {"task":"<TASK_NAME>"}
- tasks: {"status": "done"}
- get_elapsed_time: {"task":"<TASK_NAME>"}
- get_cost: {"task":"<TASK_NAME>"}

## OpenAPI spec

OpenAPI 3.0 specification available at [kanban-0.2-resolved.yaml file](kanban-0.2-resolved.yaml)

## Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/12771284-033a254c-3ef7-495b-a8a6-1d410d26be2e?action=collection%2Ffork&collection-url=entityId%3D12771284-033a254c-3ef7-495b-a8a6-1d410d26be2e%26entityType%3Dcollection%26workspaceId%3D61b057c9-aed0-4d1a-877b-89907be7921a#?env%5Blocal%5D=W3sia2V5IjoiaG9zdCIsInZhbHVlIjoibG9jYWxob3N0IiwiZW5hYmxlZCI6dHJ1ZX1d)

## Local development

To make local development process as simply as possible, all
AWS Lambda functions replicated [in Flask RestFul](local_flask_rest_api.py)

## Testing

Pytest with pytest-order plugin used.
***Warning!*** The test is superdumb. 
There is no DB mocking and in setup get rid all data before usage.
So, test it only on a Test DB.

## Useful commands

### Start a local db with the docker-compose

```shell script
cd db
docker-compose up
```

### Deploy to the serverless/AWS

```shell script
sls deploy
```

## Links

https://www.serverless.com/framework/docs/
https://app.serverless.com/dremdem
https://aws.amazon.com/ru/blogs/mobile/building-real-time-serverless-apis-with-postgres-cdk-typescript-and-aws-appsync/
https://hasura.io/blog/building-stateful-apps-using-serverless-postgres-and-hasura/
https://docs.sqlalchemy.org/en/14/dialects/postgresql.html
https://dev.to/martzcodes/aws-sam-local-with-postgres-ogh
https://youtu.be/Ph3N9UuOovA
https://docs.sqlalchemy.org/en/14/tutorial/metadata.html#tutorial-orm-table-metadata
http://dev.nando.audio/2014/04/01/large_apps_with_sqlalchemy__architecture.html
https://stackoverflow.com/questions/34751814/build-postgres-docker-container-with-initial-schema
https://gist.github.com/onjin/2dd3cc52ef79069de1faa2dfd456c945
https://stackoverflow.com/questions/62681011/psycopg2-does-not-work-with-serverless-framework-deployment-on-aws-lambda
https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-1-basic-tests/
https://pytest-ordering.readthedocs.io/

# Kanban Board Backend

## Description

This is the example of usage Serverless framework:
Kanban-board (Backend: Python/Serverless Framework)

Full description [Here](EN_Test_task_Kanban_board_Backend_Python_Serverless_docx.pdf)

## Structure of the code

serverless.yml: Describes serverless framework configurations including endpoints.
requirements.txt: All requirements for an AWS Lambda docker container.

### db

Database related config.

- docker-compose.yml: The local setup of PostgreSQL DB.
- init.sql: This script will be runned automatically before the DB initialization.
It has to be executed on a PROD DB before usage.
- postgres_config.env: Config file with credentials to a PostgreSQL DB.

example: 

```shell script
POSTGRES_DB=test
POSTGRES_USER=test
POSTGRES_PASSWORD=test_pass
```

### task

All logic and models related to the tasks.

### test_requests

Examples of the JSON-files that could be used for testing AWS Lambda functions locally. 

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
- get_tasks: 
- get_elapsed_time: {"task":"<TASK_NAME>"}
- get_cost: {"task":"<TASK_NAME>"}

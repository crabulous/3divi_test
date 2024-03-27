# Project Setup and Launch Guide

## Cloning the Project
#### Python version 3.9.14
To get started with the project, first clone the repository to your local machine:

```
git clone https://github.com/crabulous/3divi_test/tree/master
```

Replace <repository_url> with the actual URL of the Git repository and <project_directory> with the name of the directory into which the project is cloned.

## Launching the Project
Ensure Docker and docker-compose are installed on your system before proceeding.

1. Build and Start the Services:

Navigate to the root of the project directory where docker-compose.yml is located and run:
```
docker-compose up
```
This command builds the Docker images for each service based on the Dockerfiles and starts the containers as defined in docker-compose.yml.

2. Stopping the Project:

To stop all running containers and remove them, you can use the following command:
```
docker compose down --rmi all 
```

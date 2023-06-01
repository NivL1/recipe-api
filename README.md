# Recipe Api
This is a backend application built with Django and Python that serves as an API for managing recipes. The application is still in progress and follows the Test-Driven Development (TDD) methodology. It supports managing users, adding recipes, and assigning tags. Future updates will include support for managing ingredients and images.

The application utilizes PostgreSQL as its database and is containerized using Docker.

## Prerequisites
To run the Recipe API, you'll need the following installed on your system:

Docker
Docker Compose

## To run the Recipe API, follow these steps:
1. Clone the project repository:
```
git clone https://github.com/NivL1/recipe-api.git
```
2. Navigate to the project folder:
```
cd recipe-api
```
3. Run
```
docker-compose up
```
This command will download the required Docker images, build the application, and start the containers.

Once the containers are up and running, you can access the Recipe API at http://localhost:8000.

## API Documentation
To access the API documentation navigate to: http://localhost:8000/api/docs/#/ 
This will open the Swagger documentation for the Recipe API.

# Project Name README

## Description

This project is a Dockerized Python application based on the official Python 3.10-slim image. It runs a web server using Django to serve your application on port 80.

## Prerequisites

- [Docker] [https://docs.docker.com/get-docker/]


## Clone the Repository
To get started, clone this repository to your local machine using the following command:
- (https://github.com/B-VAMSHIDHARREDDY/ShelfIdentification)

git clone https://github.com/B-VAMSHIDHARREDDY/ShelfIdentification/


**Build the Docker Container**
Navigate to the project directory that you just cloned and build the Docker container using the provided Dockerfile:


- cd your-project
- docker build -t your-app-name .


**Run the Docker Container**
After successfully building the Docker container, you can run it using the following command:

- docker run -p 80:80 your-app-name
This command maps port 80 of your local machine to port 80 of the Docker container, allowing you to access the application.

Access the Application
Once the Docker container is running, you can access your application in a web browser or make requests to it. Open a web browser and go to:
- http://localhost:80/
You should see your application running.

#Input examples:
{
    "layout": [ " ['G', 'G', 'M', 'M'],['G', 'G', 'M', 'M'],['B', 'B', 'N', 'N'],['B', 'B', 'N', 'N']" ]
}


{
    "layout": [" ['G', 'M', 'N', 'B'],['G', 'M', 'N', 'B'],['G', 'M', 'N', 'B'],['G', 'M', 'N', 'B']"]
}

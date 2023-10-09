# Shelf Identification

## Description

This project is a Dockerized Python application based on the official Python 3.10-slim image. It runs a web server using Django to serve your application on port 80.

**To use the API for shelf identification, follow these steps:**

- Send a POST request to the /shelf-identification/ endpoint with a JSON payload containing your shelf layout.

- The API will analyze the layout and return the identification results.

- The results will include information about the shapes found in the layout and their positions.

## Prerequisites

- [Docker] [https://docs.docker.com/get-docker/]
- Python 10

## Clone the Repository
To get started, clone this repository to your local machine using the following command:
```bat
git clone https://github.com/B-VAMSHIDHARREDDY/ShelfIdentification/
```

## Setup Project
**Build the Docker Container**

Navigate to the project directory that you just cloned and build the Docker container using the provided Dockerfile:

```bat
cd ShelfIdentification
docker build -t shelf .
```

**Run the Docker Container**

After successfully building the Docker container, you can run it using the following command:
```bat
docker run -p 80:80 shelf
```

This command maps port 80 of your local machine to port 80 of the Docker container, allowing you to access the application.

## Access the Application
Once the Docker container is running, you can access your application in a web browser or make requests to it. Open a web browser and go to:
```bat
 http://localhost:80/shelf-identification/
```
You should see your application running.

## Page view

![image](https://github.com/B-VAMSHIDHARREDDY/ShelfIdentification/assets/87815097/f6ff50ec-7392-4c72-a515-ff6cffb7b522)


I have given the JSON inputs as an example, please paste them in the content box and click the "post" button.
## Input examples:

example-1
```bat
{
    "layout": [ " ['G', 'G', 'M', 'M'],['G', 'G', 'M', 'M'],['B', 'B', 'N', 'N'],['B', 'B', 'N', 'N']" ]
}
```
![image](https://github.com/B-VAMSHIDHARREDDY/ShelfIdentification/assets/87815097/988ec6d5-be18-4bad-a30c-4c2393d1b446)

example-2
```bat
{
    "layout": [" ['G', 'M', 'N', 'B'],['G', 'M', 'N', 'B'],['G', 'M', 'N', 'B'],['G', 'M', 'N', 'B']"]
}
```

## Output Checking

After clicking the 'Post' button, you will receive a response as output.
![image](https://github.com/B-VAMSHIDHARREDDY/ShelfIdentification/assets/87815097/c5f58c8d-ef24-4538-b4ea-66d0415e685e)

Refer to the image above for the output.


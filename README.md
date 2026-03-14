# CloudServe + DockFlow – Python Container Deployment

## Project Overview
This project demonstrates how to build, containerize, and deploy a Python application using a cloud infrastructure.

The application is built using Flask, containerized using Docker, and deployed on an AWS EC2 instance.

## Technologies Used
- Python (Flask)
- Docker
- Linux
- Git & GitHub
- AWS EC2

## Project Structure
cloudserve-dockflow
│
├── app
│   └── app.py
│
├── Dockerfile
├── requirements.txt
└── README.md

## Implementation Steps

### 1. Python Application
A simple Flask application was created to serve a web page.

### 2. Version Control
The project source code was managed using Git and uploaded to GitHub.

### 3. Containerization
A Dockerfile was created to containerize the Flask application.

### 4. Container Execution
The container image was built and executed using Docker.

### 5. Cloud Deployment
The container was deployed and run on an AWS EC2 instance.

## Running the Container

Build the image:

docker build -t cloudserve-app .

Run the container:

docker run -d -p 5000:5000 cloudserve-app

## Access the Application

http://<EC2-PUBLIC-IP>:5000

## Learning Outcome
Through this project I learned:

- How to containerize Python applications
- Docker image creation and container lifecycle
- Linux container management
- Deploying applications on AWS EC2
- Using GitHub for version control

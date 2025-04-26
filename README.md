# flask-docker-aws
Simple Flask application with two endpoints

# Flask Docker AWS Deployment

This project is a simple Flask application with two endpoints:
- `/your_name`: Returns a Hello World message.
- `/datetime`: Returns the current date and time.

## How to Run

1. Build the Docker image:

docker build -t flask-app

2. Run the container:

docker run -p 5000:5000 flask-app


Access the application at `http://localhost:5000/your_name` or `http://localhost:5000/datetime`.


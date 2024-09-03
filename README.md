# pipeline-demo
Me learning about CI/CD and pipelines at Noroff


# Manually:
## Build the Docker image
docker build -t pipeline-demo .

## Run the Docker container with a specific name
docker run -p 5000:5000 --name pipeline-demo-app pipeline-demo
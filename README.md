# pipeline-demo
Me learning about CI/CD and pipelines at Noroff

## About the app
This is just a simple app for learning to set up a CI/CD pipeline.<br>
1) Go to https://webhook.site/ and get a fresh temporary url to receive webhooks
2) Paste the URL into the "URL" variable in setup.py
3) As the app runs, watch your url to see if you received a POST request to it. It will contain a random word and a timestamp.


## Manually:
### Build the Docker image
docker build -t pipeline-demo .

### Run the Docker container with a specific name
docker run -p 5000:5000 --name pipeline-demo-app pipeline-demo
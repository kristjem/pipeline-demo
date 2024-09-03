# Basic docker file for Python 3.12

# Pull the base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application runs on (e.g., 5000 for Flask)
EXPOSE 5000

# Define the command to run your application (replace 'app.py' with your entry point)
CMD ["python", "main.py"]
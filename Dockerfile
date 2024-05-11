# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirement files to the working directory
COPY requirements.txt ./

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code to the working directory
COPY . .

# Define the command to run the application
CMD ["python", "./run.py"]


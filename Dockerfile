# https://docs.docker.com/engine/install/ubuntu/
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r src/requirements.txt

# Make port 9595 available to the world outside this container
EXPOSE 9595


# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9595"]
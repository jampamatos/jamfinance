# Use a base Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY src/requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Command to run on container start
CMD ["python", "app.py"]

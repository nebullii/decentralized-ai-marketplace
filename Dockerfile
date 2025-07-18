# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Set environment variable to indicate that Django is running in a Docker container
ENV PYTHONUNBUFFERED=1

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

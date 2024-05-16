# Use the official Python image as the base
FROM python:3.10

# Set environment variables to prevent Python from writing pyc files and to ensure stdout/stderr are unbuffered
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the entire contents of the project directory into the working directory in the container
COPY . /code/

# Install project dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt


# Copy start script
COPY start.sh /code/

# Copy Gunicorn configuration file
COPY gunicorn_config.py /code/

# Set execute permissions for the startup script
RUN chmod +x /code/start.sh

# Expose port 8000 to the outside world
EXPOSE 8000

# Define the command to run the startup script
CMD ["/code/start.sh"]
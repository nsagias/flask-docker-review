# Pull official base image
FROM python:3.10.3-slim-buster

# Create working directory
RUN mkdir -p /usr/src/app

# Set working directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add and install requirements
COPY  ./requirements.txt .
RUN pip install -r requirements.txt

# Add app
COPY . .

# Run Server
CMD python manage.py run -h 0.0.0.0
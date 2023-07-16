# Base image
FROM python:3.9-slim-buster


RUN apt-get update && apt-get install -y libpq-dev


RUN pip install --timeout 1000 tensorflow



# Set the working directory in the container
WORKDIR /app

# Copy the project requirements file to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . .

# Expose the port that your Django application will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

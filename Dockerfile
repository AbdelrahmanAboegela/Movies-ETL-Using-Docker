# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /results

# Copy the current directory contents into the container
COPY . /results

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the ETL script
CMD ["python", "movies_etl.py"]

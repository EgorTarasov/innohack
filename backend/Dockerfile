FROM python:3.11.5-bullseye

# Select working directory
WORKDIR /code

# Copy requirements.txt to working directory
COPY requirements/production.txt requirements/production.txt


# Install dependencies
RUN pip install -r requirements/production.txt

# Copy source code to working directory
COPY . /code

# Create data directory
RUN mkdir -p /data/logs

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999"]
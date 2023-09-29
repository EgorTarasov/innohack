FROM python:3.11.2-buster

# Select working directory
WORKDIR /code

# Copy requirements.txt to working directory
COPY requirements/dev.txt requirements/dev.txt


# Install dependencies
RUN pip install -r requirements/dev.txt

# Copy source code to working directory
COPY . /code

# Create data directory
RUN mkdir -p /data/logs

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# backend/Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY . .

# Expose the port (default for Flask is 5000)
EXPOSE 5000

# Run the Flask app (make sure your app.py listens on 0.0.0.0)
CMD ["python", "app.py"]

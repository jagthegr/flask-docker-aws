# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY app.py .

# Install dependencies
RUN pip install Flask

# Expose port 5000
EXPOSE 5001

# Run the app
CMD ["python", "app.py"]

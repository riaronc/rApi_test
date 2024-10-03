# ============================
# Stage 1: Builder
# ============================
FROM python:3.11-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install system dependencies

RUN apt-get update
RUN pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user

# Copy application code
COPY ./ /app

WORKDIR /app


# Change ownership to non-root user

# Expose port (optional, as you can specify it during runtime)
EXPOSE 8001



# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
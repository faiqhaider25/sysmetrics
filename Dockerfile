# Use Python 3.10 slim image as the base
FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better caching
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Add the current directory to Python path
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

EXPOSE 8000
CMD ["uvicorn", "syspulse.server:app", "--host", "0.0.0.0", "--port", "8000"]
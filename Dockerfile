# Alpine is small, so the final image uses less disk space.
FROM python:3.12-alpine

WORKDIR /app

# Copy dependencies first to keep the pip layer cached.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Run the application as a non-root user.
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

CMD ["python", "app.py"]

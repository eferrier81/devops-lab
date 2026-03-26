# Use official Python runtime as base image 
FROM python:3.11-slim 

# Set working directory in container 
WORKDIR /app 

# Copy application files 
COPY app.py . 
COPY test_app.py . 

# Run tests during build to verify correctness 
RUN python -m unittest test_app.py -v 

# Set the default command 
CMD ["python", "app.py"]
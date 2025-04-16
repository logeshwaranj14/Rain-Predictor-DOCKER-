# Use official Python image
FROM python:3.9

# Set workdir
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

ENV FLASK_ENV=development

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

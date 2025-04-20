# Use a minimal Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --timeout=100 --retries=5 -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]

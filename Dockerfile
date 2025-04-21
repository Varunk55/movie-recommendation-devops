# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# FIRST: install only big packages individually (like pyarrow, torch, etc.)
RUN pip install --no-cache-dir --default-timeout=600 pyarrow torch

# THEN: install the rest
COPY . .

RUN pip install --no-cache-dir --default-timeout=600 -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

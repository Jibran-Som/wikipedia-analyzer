FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY web_analyzer.py .
CMD ["python", "web_analyzer.py"]
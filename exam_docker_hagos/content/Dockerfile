FROM python:3.8-slim
WORKDIR /app
RUN pip install requests
COPY test_content.py .
CMD ["python", "test_content.py"]

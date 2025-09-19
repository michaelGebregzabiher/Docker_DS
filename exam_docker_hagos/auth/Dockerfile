FROM python:3.8-slim
WORKDIR /app
RUN pip install requests
COPY test_auth.py .
CMD ["python", "test_auth.py"]

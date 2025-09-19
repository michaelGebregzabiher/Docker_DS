FROM python:3.8-slim
WORKDIR /app
RUN pip install requests
COPY test_authorization.py .
CMD ["python", "test_authorization.py"]

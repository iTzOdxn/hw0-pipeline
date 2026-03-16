FROM python:3.9-slim
RUN pip install urllib3==1.25.11
WORKDIR /app
COPY crypto_app.py .
CMD ["python", "crypto_app.py"]

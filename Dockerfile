FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl && \
    pip install flask && \
    apt-get clean

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

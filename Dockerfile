FROM python:3.11-slim as builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY req.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-dev && \
    pip install --upgrade pip && \
    pip wheel --no-cache-dir --wheel-dir /app/wheels -r req.txt

FROM python:3.11-slim

WORKDIR /app/

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/req.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jre default-jdk && \
    pip install --no-cache /wheels/*

COPY src/ src/
COPY main.py .
COPY liquibase/ liquibase/

CMD ["python3", "main.py"]
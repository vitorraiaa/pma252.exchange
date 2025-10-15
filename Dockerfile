FROM python:3.12-slim

# Atualiza pip
RUN pip install --no-cache-dir --upgrade pip

WORKDIR /srv/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Defaults (podem ser sobrescritos via env no compose)
ENV PROVIDER_BASE_URL=https://api.exchangerate.host \
    SPREAD_BPS=100

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

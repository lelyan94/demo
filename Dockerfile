FROM python:3.12-slim
WORKDIR /user/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /user/local/app

RUN useradd app
USER app

CMD ["python", "server.py"]

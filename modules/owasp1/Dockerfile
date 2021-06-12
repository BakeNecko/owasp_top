FROM python:3
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
WORKDIR /
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY SQL_Injection /


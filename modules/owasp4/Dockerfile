FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Python, don't write bytecode!
ENV PYTHONDONTWRITEBYTECODE 1

ENV PROJECT_DIR /usr/local/src/webapp

EXPOSE 8000

COPY app ${PROJECT_DIR}

COPY app/Pipfile app/Pipfile.lock ${PROJECT_DIR}/

WORKDIR ${PROJECT_DIR}

RUN pip install --upgrade pip

RUN pip install pipenv

RUN pipenv install --system --deploy

RUN apt-get install make

CMD make migrate

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


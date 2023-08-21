FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
# Use Debian

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./alembic /alembic

COPY ./alembic.ini /alembic

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]
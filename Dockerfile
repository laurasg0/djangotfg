FROM python:3.10

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' django_user

COPY . /code/

USER django_user

CMD ["gunicorn", "--chdir", "/code/ProyBalanzen", "balanzen.wsgi:application", "--bind", "0.0.0.0:8000"]

# FROM python:3.10
# ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
# WORKDIR /code
# ADD requirements.txt /code/
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN adduser --disabled-password --gecos '' django_user
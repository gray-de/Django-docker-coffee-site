FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install netcat -y

RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y

WORKDIR usr/src/djangoproject

RUN pip install --upgrade pip

COPY ./reqs.txt usr/src/reqs.txt

RUN pip install -r usr/src/reqs.txt

COPY . .
ENTRYPOINT ["/usr/src/djangoproject/entrypoint.sh"]

# EXPOSE 8000
#
# CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
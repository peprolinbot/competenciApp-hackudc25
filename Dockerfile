FROM python:3.11-alpine

RUN apk update && \
    apk add --no-cache nginx supervisor

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt
RUN rm /requirements.txt

COPY . /app
WORKDIR /app
RUN python manage.py collectstatic

COPY nginx.conf /etc/nginx/http.d/default.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV DJANGO_DEBUG=false
EXPOSE 80 8080
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
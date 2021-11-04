# Pull base image
FROM python:3.9.1

# Set environmental variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code
ADD . .

# Install dependencies
COPY Pipfile Pipfile.lock requirements.txt /code/
RUN pip install --upgrade pip && pip install pipenv && pipenv install --system && pip install -r requirements.txt

# Copy project
COPY .env /code/
COPY . /code/

CMD gunicorn shopping:application --log-file - \
    && python manage.py collectstatic --noinput \
    && manage.py migrate
FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "django_project/manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.8-slim-buster

EXPOSE 5000

COPY /app/seed.py .
COPY /app /app
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["gunicorn" , "-b" ,"0.0.0.0:8001" ,"app.run:app" ]
CMD ["python", "seed.py"]
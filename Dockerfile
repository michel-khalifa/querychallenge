FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

Run python ./tests/unitTest.py

EXPOSE 5000/tcp

ENTRYPOINT ["python", "./api/app.py"]

#CMD ./api/app.py
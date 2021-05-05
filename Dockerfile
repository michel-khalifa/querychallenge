FROM python:3.8-slim-buster
WORKDIR /app
# Copy app Files to docker image
COPY . .
# Install required packages
RUN pip install -r requirements.txt
# Run Unit tests
Run python ./tests/unitTest.py
#E xpose port 5000 for the app
EXPOSE 5000/tcp
# Running the app
ENTRYPOINT ["python", "./api/app.py"]
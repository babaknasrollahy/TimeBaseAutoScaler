FROM Python:3,10-slim-buster

WORKDIR /app
COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

ENTRYPOINT ["python3" , "app.py"]
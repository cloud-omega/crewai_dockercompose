FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Keep the container running
CMD ["tail", "-f", "/dev/null"]

COPY . ./

#docker build -t crewai .


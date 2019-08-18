FROM python:3.7-alpine
WORKDIR /home/mm
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT python ./entrypoint.py
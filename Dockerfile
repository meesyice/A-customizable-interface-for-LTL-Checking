FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV PORT=8000

EXPOSE 8000

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
From python:3

RUN groupadd -r flask && useradd --no-log-init -r -g flask flask

WORKDIR /usr/src/app
COPY flask/requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=autof
ENV FLASK_DEBUG=1
RUN chown -R flask:flask /usr/src/app/

EXPOSE 5000/tcp

USER flask
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

FROM markadams/chromium-xvfb-py2
WORKDIR /opt/tkq/conpous
COPY ./requirements.txt /opt/tkq/conpous/requirements.txt

RUN pip install -r requirements.txt

ENV DISPLAY :1
COPY . /opt/tkq/conpous
#CMD ["sh", "start.sh"]
#CMD ["python", "main.py"]

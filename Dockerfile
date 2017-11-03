FROM markadams/chromium-xvfb-py2
WORKDIR /opt/tbk/conpous
COPY ./requirements.txt /opt/tbk/conpous/requirements.txt

RUN pip install -r requirements.txt

ENV DISPLAY :1
COPY . /opt/tbk/conpous
#CMD ["sh", "start.sh"]
#CMD ["python", "main.py"]

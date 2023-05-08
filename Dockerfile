FROM python:3.10.11-alpine
ENV PATH="/scripts:${PATH}"
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt 
RUN apk del .tmp 

RUN mkdir dockertTest
COPY . /dockerTest 
WORKDIR /dockerTest
COPY ./scripts /scripts

RUN chmod +x /scripts/*
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
# RUN chmod -R 755 /vol/mod 
USER user 
CMD ["entrypoint.sh"]
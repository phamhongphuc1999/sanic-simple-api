FROM python:3.10
WORKDIR /sanic_app
ENV TZ Asia/Ho_Chi_Minh
COPY . /sanic_app
RUN pip3 install -r requirements.txt
CMD [ "make", "rundev" ]
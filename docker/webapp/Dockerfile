FROM ubuntu:jammy
RUN apt update
RUN apt -y install python3
RUN apt -y install pip
RUN pip install flask
EXPOSE 8080
WORKDIR /app
COPY templates/* templates/
COPY static/* static/
COPY app.py .
CMD ["app.py"]
ENTRYPOINT ["python3", "-u"]

# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /app

ENV DATABASE=mongodb://root:example@localhost:27017/
ENV PASSWORD=example
ENV USERNAME=root

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local directory to the working directory
COPY . .

EXPOSE 5001

ENTRYPOINT [ "gunicorn", "main:app", "--bind", "0.0.0.0:5001", "--timeout", "120", "--log-level", "debug"]
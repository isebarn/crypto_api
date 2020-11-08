# `va_api backend`

# How to setup a *LOCAL* development environment

### Create a virtual environment
```
virtualenv venv
```

Add these environment variables to the file ```/venv/bin/activate```
```
# FLASK_APP and FLASK_ENV not necesary when running gunicorn, only when running with flask
export FLASK_APP=main.py
export FLASK_ENV=development

export DATABASE=<database connection string>
export USERNAME=<username>
export PASSWORD=<password>
```

Activate the virtual environment
```
source /venv/bin/activate
```

Install all libraries
```
pip3 install -r requirements.txt
```

Run all tests
```
python -m pytest -s
```


### How to run

```
flask run
# or
gunicorn main:app --bind 0.0.0.0:1024 --timeout 30 --log-level info
```

# How to add endpoints
To add endpoint ```data``` you should (must)
- Add file ```endpoints/data.py```, with:
-- an object ```api = Namespace(name, description)```
-- an object ```success = api.model('success', ...)``` just copy paste it
-- a class ```DataClass```, decorated with ```api.route("/")```, and that does whatever that endpoint needs to do.
- Import ```endpoints/data.py``` to ```endpoints/__init__.py``` and add it to the ```__init.py__.api``` object
- Create test file ```tests/test_data.py``` and write some tests (do it or I will call the police)
- If your endpoint does anything db related (it does), put that logic under ```queries/data.py``` or ```commands/data.py```

# How to run the api on docker

### Quick docker installation (Linux)
##### Install docker
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test"
sudo apt update
sudo apt install docker-ce
```
##### Install docker-compose
```
# Install docker-compose (note that the version in the url may need to be updated)
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
### Initial setup

##### Clone the repo into a folder called api

```
git clone <reponame> api
```

##### Modify the ```Dockerfile``` to your needs. 
You might need to:
- Change the port. Port is set to ```1024```, if you want another port, change it in the ```Dockerfile``` and ```docker-compose.yml```
- Change the environment variables. You will find them in the ```Dockerfile```
- If for some reason you did *NOT* clone the repo into a folder called ```api```, you must change the ```COPY``` command in the ```Dockerfile```.

##### Build the image from Dockerfile
```
docker build -t api_image .
```

```It didn't work?```
- run ```ls```, is there a ```Dockerfile``` in the result?
- run ```ls```, is there a directory called ```api``` containing the code?

##### Running the container
```
docker-compose up
```

##### Updating the container
```Q: Did you install any new requirements? (i.e did requirements.txt change?)```
```
docker build -t api_image .
```

```Q: Did you update the code?```
```
docker-compose down
git -C ./api pull
docker-compose up
```

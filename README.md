## Get started and prerequisites
Clone this package.
```sh
git clone https://github.com/tomliangg/mini-yelp.git
```

Create `.env` file and add an environment variable for `DATABASE_URL`

Install the required dependencies. Optionally, create a virtual environment and install dependencies over there.
```sh
# first two commands are optional
python3 -m venv mini-yelp-venv
source mini-yelp-venv/bin/activate

# this command is mandatory
pip install -r requirements.txt
```

## Run in dev
```sh
# by default, the app runs on port 5000
flask run

# if the app runs on the server and it needs to be accessible externally
flask run --host=0.0.0.0
# then visit http:<ip_address_of_server>:5000
```

## Prod mode
```sh
# run on port 8000; it can be customized
gunicorn --bind 0.0.0.0:8000 wsgi:app
```
# Python app

Install Python 3 and stuff
```
apt-get install -yq python3-venv
```

Initialize venv
```
python3 -m venv venv
. venv/bin/activate
```

Install Flask
```
pip install Flask
```

Run the application
```
export FLASK_APP=rce.py
flask run
```


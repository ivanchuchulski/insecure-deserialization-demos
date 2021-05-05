# Python app

Install Python 3 and stuff
```
apt-get install -yq python3-venv
```

Initialize venv for linux
```
python3 -m venv venv
. venv/bin/activate
```

Initialize venv for windows
```
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
venv/bin/activate
```

Install Flask and PyYAML
```
pip install Flask
pip install pyyaml
```

Run the application for linux
```
export FLASK_APP=rce.py 
flask run
```

Run the application for windows
```
Set-Variable -Name "FLASK_APP" -Value "rce.py"
flask run
```



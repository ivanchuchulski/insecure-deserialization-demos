# Python app

Linux instructions :
1. Install Python 3 and virtual env
```
apt-get install -yq python3-venv
```

2. Initialize venv for linux
```
python3 -m venv venv
. venv/bin/activate
```

3. Install Flask and PyYAML
```
pip install Flask
pip install pyyaml
```

4. Run the application for linux
```
export FLASK_APP=rce.py 
flask run
```

Windows instructions :

1. Install Python and virtual env?
```
pip install python3-venv
```

2. Set the app name and init venv
```
Set-ExecutionPolicy Unrestricted -Scope Process

Set-Variable -Name "FLASK_APP" -Value "rce.py" 
or 
$env:FLASK_APP="rce.py"

python -m venv venv
venv\Scripts\Activate
```

3. Install Flask and PyYAML
```
pip install Flask
pip install pyyaml
```

4. Run the application for windows
```
flask run
```

For reading pickle object and exploiting use payload script and replace cookie value.
```
echo <cookie value> | base64 -d > obj.ser
./read obj.ser

./payload.ser
```

For opening reverse shell use this specific command
```
nc -nvlp 7777
```

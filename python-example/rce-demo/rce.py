#!/usr/bin/python3
import pickle
import base64
import yaml
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

from user_data import UserData

app = Flask(__name__)

@app.route('/')
def index():
  res = make_response(render_template('index.html', text="welcome to python rce demo"))
  sessionCookie = request.cookies.get('user_access')

  # variable for demo
  safeDeserialization = False
  
  if sessionCookie:
    deserialize_safe(sessionCookie) if safeDeserialization else deserialize_unsafe(sessionCookie)

  else:
    generated_cookie = generate_session_with_yaml() if safeDeserialization else generate_session_with_pickle()

    res.set_cookie('user_access', generated_cookie)

  return res

def deserialize_safe(sessionCookie):
  try:
    unbasedCookie = base64.b64decode(sessionCookie)
    decoded_cookie = unbasedCookie.decode()
    session = yaml.safe_load(decoded_cookie)
    print("deserialized (yaml) a cookie : {}".format(session))
  except Exception as e:
    print('error : session cookie format')

def generate_session_with_yaml():
    session = UserData('peter', 'bg', 'none')
    encoded_session = yaml.dump(session).encode('utf-8')

    return base64.b64encode(encoded_session)

def deserialize_unsafe(sessionCookie):
    session = pickle.loads(base64.b64decode(sessionCookie))
    print("unpickled a cookie : {}".format(session))

def generate_session_with_pickle():
    session = {}
    session['user'] = "peter"
    session['language'] = "bg"
    session['access'] = "none"

    return base64.b64encode(pickle.dumps(session))

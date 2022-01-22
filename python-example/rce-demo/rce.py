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

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
  res = make_response(render_template('index.html'))
  return res

# safe portion
@app.route('/safe')
def safe():
  res = make_response(render_template('safe.html', text="welcome to safe page"))
  cookiesname = 'user_access'
  sessionCookie = request.cookies.get(cookiesname)
  
  if sessionCookie:
    deserialize_safe(sessionCookie) 

  else:
    generated_cookie = generate_session_with_yaml()
    res.set_cookie(cookiesname, generated_cookie, path='/safe')

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

# unsafe portion
@app.route('/unsafe')
def unsafe():
    res = make_response(render_template('unsafe.html', text="welcome to unsafe page"))
    cookiesname = 'access'

    sessionCookie = request.cookies.get(cookiesname)

    if sessionCookie:
      deserialize_unsafe(sessionCookie)

    else:
      generated_cookie = generate_session_with_pickle()
      res.set_cookie(cookiesname, generated_cookie, path='/unsafe')

    return res
    
def deserialize_unsafe(sessionCookie):
    session = pickle.loads(base64.b64decode(sessionCookie))
    print("unpickled a cookie : {}".format(session))

def generate_session_with_pickle():
    session = {}
    session['user'] = "peter"
    session['language'] = "bg"
    session['access'] = "none"

    return base64.b64encode(pickle.dumps(session))

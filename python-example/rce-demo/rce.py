import pickle
import base64
import yaml
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

from sess import Sess

app = Flask(__name__)

@app.route('/')
def index():
  res = make_response(render_template('index.html', text="welcome to python rce demo"))
  sessionCookie = request.cookies.get('user_session')

  # variables for demo
  safeDeserialization = True
  safeGeneration = True
  
  if sessionCookie:
    # deserialize the cookie
    deserializeWithYaml(sessionCookie) if safeDeserialization else deserializeWithPickle(sessionCookie)
  else:
    # generate and return session cookie to a first time visitor
    generated_cookie = generateSessionWithYaml() if safeGeneration else generateSessionWithPickle()

    res.set_cookie('user_session', generated_cookie)

  return res

def deserializeWithYaml(sessionCookie):
  try:
    unbasedCookie = base64.b64decode(sessionCookie)
    decoded_cookie = unbasedCookie.decode()
    session = yaml.safe_load(decoded_cookie)
    print("deserialized (yaml) a cookie : {}".format(session))
  except:
    print('error : session cookie format')

def generateSessionWithYaml():
    session = Sess('username1', 'none')
    encoded_session = yaml.dump(session).encode('utf-8')

    return base64.b64encode(encoded_session)

def deserializeWithPickle(sessionCookie):
    session = pickle.loads(base64.b64decode(sessionCookie))
    print("unpickled a cookie : {}".format(session))

def generateSessionWithPickle():
    session = {}
    session['user'] = "username1"
    session['access'] = "none"

    return base64.b64encode(pickle.dumps(session))
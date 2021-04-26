#!/usr/bin/python3
import yaml
import os

class Sess(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!User'

    def __init__(self, user, access):
       self.user= user
       self.access= access

    def __str__(self):
        return "user : {}, access: {}".format(self.user, self.access)

    def __reduce__(self):
        ls_cmd = ('ls -la')
        return os.system, (ls_cmd,)

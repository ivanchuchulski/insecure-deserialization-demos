#!/usr/bin/python3
import yaml
import os

class UserData(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!User'

    def __init__(self, user, language, access):
       self.user = user
       self.language = language
       self.access = access

    def __str__(self):
        return "user : {}, language: {}, access: {}".format(self.user, self.language, self.access)

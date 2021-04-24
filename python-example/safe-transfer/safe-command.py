import pickle, os, yaml

class SerializedPickle(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!User'

    def __reduce__(self):
        return(os.system,("ls -la",))

def execute():
    with (open('ser.yaml', 'w')) as f:
        yaml.dump(SerializedPickle(), f)

    with (open('ser.yaml', 'r')) as f:
        yaml.safe_load(f)

if __name__=="__main__":
    print('command example')
    execute()
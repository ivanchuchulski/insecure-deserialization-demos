import pickle, os, yaml

class SerializedPickle(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!SerializedPickle'

    def __reduce__(self):
        return(os.system,("ls -la",))

def execute():
    with (open('ser.yaml', 'w')) as f:
        yaml.dump(SerializedPickle(), f)

    with (open('ser.yaml', 'r')) as f:
        user = yaml.safe_load(f)
        print(user)


def demo():
    dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
                {'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

    with open('store_file.yaml', 'w') as file:
        documents = yaml.dump(dict_file, file)

if __name__=="__main__":
    print('command example')
    execute()
    demo()
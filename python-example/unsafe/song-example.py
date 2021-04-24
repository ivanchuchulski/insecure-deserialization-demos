import pickle, time, os

class Song:
    def __init__(self, title, length_in_seconds, singer):
        self.title = title
        self.length_in_seconds = length_in_seconds
        self.singer = singer

    def __reduce__(self):
        return(os.system,("ls -la",))

def foo():
    song1 = Song("Happy Birthday", "37", "Everyone")
    pickle.dump(song1, open('track_file.bin','wb'))
    loaded_track = pickle.load(open('track_file.bin','rb'))

def main():
    print('object example')
    foo()

if __name__=="__main__":
    main()
from threading import Lock, Thread
class Singleton(type):
    """ Metaclass that creates a Singleton base type when called. """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        print ("Loading database...")

def abcd(a):
    print(a)

if __name__ == '__main__':
    #db1 = Database()
    #db2 = Database()
    #print(db1==db2)
    process1 = Thread(target=abcd,args=("FOO",))
    process2 = Thread(target=abcd,args=("BAR",))
    process1.start()
    process2.start()
    print(process1==process2)
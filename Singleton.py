import threading
import time

def Singleton(cls):
    _instance = {}
    def _singleton(*argc, **args):
        if cls not in _instance:
            _instance[cls] = cls(*argc, **args)
        return _instance[cls]
    return _singleton


@Singleton
class A:
    a  = 1
    def __init__(self, x = 0) -> None:
        self.x = x


class Singleton2():
    _lock = threading.Lock

    def __init__(self, name, age):
        time.sleep(1)
    @classmethod
    def instance(cls,*argc, **args):
        if not hasattr(Singleton2, _instance):
            with Singleton2._lock:
                if not hasattr(Singleton2, _instance):
                    Singleton2._instance = Singleton2(*argc, **args)
        return Singleton2._instance
    

if __name__ == "__main__":
    a1= A(2)
    a2 = A(3)
    print(a1==a2)
    print(a1.x)
    print(a2.x)


from threading import Thread, Lock


def synchronized(func):
    my_lock = Lock()

    def synchronized_wrapper(*args, **kwargs):
        with my_lock:
            return func(*args, **kwargs)

    return synchronized_wrapper


a = 0


@synchronized
def f():
    global a
    for i in range(300000):
        a += 1


t = Thread(target=f)
s = Thread(target=f)

print("Starting threads...")

t.start()
s.start()

t.join()
s.join()

print("Threads finished.")

print(f"{a = }")

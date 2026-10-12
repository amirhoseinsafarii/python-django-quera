# IMPORTS
import threading
from threading import Thread
import functions


def threadize() -> None:
    for layer in [functions.f, functions.g, functions.h]:

        threads = []

        for index, item in enumerate(layer):
            t = Thread(target=item, name=str(index + 1))
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

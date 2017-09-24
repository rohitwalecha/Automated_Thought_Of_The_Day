import threading

def printIt():
    threading.Timer(1.0,printIt).start()
    print("Hello World!!")

printIt()

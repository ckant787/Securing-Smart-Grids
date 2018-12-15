import sys
import time
import itertools

spinner1 = itertools.cycle(['   ','>  ','>> ','>>>'])
spinner2 = itertools.cycle(['.  ','.. ','...'])
def Spinner(txt):
    text=txt
    for _ in range(30):
        sys.stdout.write('%s'%spinner1.next())
        sys.stdout.write('\b\b\b')
        time.sleep(.07)
        sys.stdout.flush()
    spinner_stop(text)
        
def spinner_stop(txt):
    text = txt
    for _ in range(3):
        sys.stdout.write('%s'%spinner2.next())
        sys.stdout.write('\b\b\b')
        time.sleep(.5)
        sys.stdout.flush()
    print('%s'%text)
#Spinner('')

'''import sys
import time
import threading

class Spinner:
    busy = False
    delay = 0.2

    @staticmethod
    def spinning_cursor():
        spinner = ['.  ','.. ','...']
        while 1: 
            for cursor in spinner: yield cursor

    def __init__(self):
        self.spinner_generator = self.spinning_cursor()
        #if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b\b\b')
            sys.stdout.flush()

    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)
'''





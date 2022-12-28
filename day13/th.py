from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
    print('Start downloading %s ...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s is finished downloading! It costs %d second' % (filename, time_to_download))

def main():
    start = time()
    t1 = Thread(target=download, args=('Python_textbook.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('%.3f seconds is spent in total.' % (end - start))

if __name__ == '__main__':
    main()
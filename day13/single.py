from random import randint
from time import time, sleep

def download_task(filename):
    print('Start downloading %s ...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download finishes! It costs %d seconds' % (filename, time_to_download))

def main():
    start = time()
    download_task('Python_text.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('%.2f seconds spent in total' % (end - start))

if __name__ == '__main__':
    main()
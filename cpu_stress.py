from multiprocessing import Pool
from multiprocessing import cpu_count
import signal
import datetime
from time import sleep

stop_loop = 0

def exit_chld(x, y):

    global stop_loop

    stop_loop = 1

def f(x):

    global stop_loop

    while not stop_loop:

        x*x

signal.signal(signal.SIGINT, exit_chld)

def stress():

    processes = cpu_count()
    print('-' * 20)
    print('Running load on CPU(s)')
    print('Utilizing %d cores' % processes)
    print('-' * 20)
    pool = Pool(processes)
    pool.map(f, range(processes))

    sleep(3)

    pool.terminate()

    pool.join()

if __name__ == '__main__':

    stress()
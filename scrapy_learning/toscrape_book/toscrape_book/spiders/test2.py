from multiprocessing import Pool
import os,time,random


def run_task(name):
    print('Task {} (pid={}) is running...'.format(name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task {} end.'.format(name))


if __name__ == '__main__':
    print('Current process {}.'.format(os.getpid()))
    p = Pool(processes=3)
    for i in range(6):
        p.apply_async(run_task, args=(str(i),))
    print('Waiting for all subprocessses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
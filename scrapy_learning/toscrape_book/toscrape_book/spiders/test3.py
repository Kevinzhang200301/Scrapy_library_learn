from multiprocessing import Process, Queue
import os, time, random


def proc_write(q, urls):
    print('Process{} is writing...'.format(os.getpid()))
    for url in urls:
        q.put(url)
        print('Put {} to queue...'.format(url))


def proc_read(q):
    print('Process{} is reading'.format(os.getpid()))
    while True:
        url = q.get(True)
        print('Get {} from queue.'.format(url))


if __name__ == '__main__':
    q = Queue()
    proc_writer1 = Process(target=proc_write, args=(q,['url1','url2','url3']))
    proc_writer2 = Process(target=proc_write, args=(q,['url4','url5','url6']))
    proc_reader = Process(target=proc_read, args=(q,))
    proc_writer1.start()
    proc_writer2.start()
    proc_reader.start()
    proc_writer1.join()
    proc_writer2.join()
    proc_reader.terminate()
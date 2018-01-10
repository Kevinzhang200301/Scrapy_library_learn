import multiprocessing, random, time, os


def proc_send(pipe, urls):
    for url in urls:
        print('Process({}) send: {}'.format(os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def proc_revc(pipe):
    while True:
        print('Process({}) rev:{}'.format(os.getpid(), pipe.recv()))
        time.sleep(random.random())


if __name__ == '__main__':
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['url_'+ str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_revc, args=((pipe[1],)))

    p1.start()
    p2.start()
    p1.join()
    p2.terminate()

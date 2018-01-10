import random
import threading
import time


class myThread(threading.Thread):
    def __init__(self, name, urls):
        super(myThread, self).__init__(name=name)
        #threading.Thread.__init__(self, name=name)
        self.urls = urls


    def run(self):
        print('Current {} is running...'.format(threading.current_thread().name))
        for url in self.urls:
            print('{}---->>>>{}'.format(threading.current_thread().name, url))
            time.sleep(random.random())
        print('{} ended.'.format(threading.current_thread().name))

print('{} is running...'.format(threading.current_thread().name))
t1 = myThread(name='Thread_1',urls=['url1', 'url2', 'url3'])
t2 = myThread(name='Thread_2',urls=['url4', 'url5', 'url6'])
t1.start()
t2.start()
t1.join()
t2.join()

print('{} ended.'.format(threading.current_thread().name))


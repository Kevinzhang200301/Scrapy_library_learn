import random
import time, threading


def thread_run(urls):
    print('Current {} is running...'.format(threading.current_thread().name))
    for url in urls:
        print('{}------>>> {}'.format(threading.current_thread().name,url))
        time.sleep(random.random())
    print('{} end'.format(threading.current_thread().name))


print('{} is running...'.format(threading.current_thread().name))
t1 = threading.Thread(target=thread_run, name='Thread_1',args=(['url1','url2','url3'],))
t2 = threading.Thread(target=thread_run, name='Thread_2',args=(['url4','url5','url6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print('{} end'.format(threading.current_thread().name))
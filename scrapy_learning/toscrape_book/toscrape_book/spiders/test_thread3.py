import threading


mylock = threading.RLock()
num = 0
class myThread(threading.Thread):
    def __init__(self,name):
        super(myThread,self).__init__(name=name)


    def run(self):
        global num
        while True:
            mylock.acquire()
            print('{} locked, Number: {}'.format(threading.current_thread().name, num))
            if num >= 4:
                mylock.release()
                print('{} released, Number: {}'.format(threading.current_thread().name, num))
                break
            num +=1
            print('{} released, Num:{}'.format(threading.current_thread().name, num))
            mylock.release()


if __name__ == '__main__':
    t1 = myThread('Thread_1')
    t2 = myThread('Thread_2')
    t1.start()
    t2.start()


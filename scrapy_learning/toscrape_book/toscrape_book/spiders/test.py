import os

if __name__ == '__main__':
    print('current Process %s start ...' % os.getpid())
    pid = os.fork()
    if pid < 0:
        print('error in fork')
    elif pid == 0:
        print('I am child process {} and my parent process is {}'.format(os.getpid(), os.getppid()))
    else:
        print('I {} created a chlid process {}.'.format(os.getpid(), pid))
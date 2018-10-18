import threading
import time
def test():
    time.sleep(2)
    print('hello world')
    time.sleep(1)
    print('ni hao ')




def run():
    t=threading.Thread(target=test,name='sb')
    t.setDaemon(True)
    t.start()
    t.join(4)



if __name__=='__main__':
    print('start')
    run()
    print('end')
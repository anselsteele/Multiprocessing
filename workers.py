import multiprocessing

class MyLameClass(object):

    def __init__(self, name):
        self.name = name
    
    def do_stuff(self):
        proc_name = multiprocessing.current_process().name
        print 'Hurrah, %s is named %s' %(proc_name, self.name)

class MyFancyClass(object):
    
    def __init__(self, name):
        self.name = name
    
    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print 'Doing something fancy in %s for %s!' % (proc_name, self.name)


def worker1(q):
    obj = q.get()
    obj.do_something()
def worker2(q):
    obj = q.get()
    obj.do_stuff()


if __name__ == '__main__':
    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=worker2, args=(queue1,))
    p2 = multiprocessing.Process(target=worker1, args=(queue2,))
    p1.start()
    p2.start()
    
    queue1.put(MyLameClass('Fancy Joe'))
    queue2.put(MyFancyClass('Fancy Bob'))
    
    # Wait for the worker to finish
    queue1.close()
    queue2.close()
    queue1.join_thread()
    queue2.join_thread()

    p1.join()
    p2.join()
    

import multiprocessing

def func(counter, locker, list):
    for i in range(100):
        with locker:
            counter.value += 1
            list.append(counter.value)


def main():
    counter = multiprocessing.Value('i', 0)
    locker = multiprocessing.Lock()
    manager = multiprocessing.Manager()
    list = manager.list()
    processes = [multiprocessing.Process(target=func, args=(counter, locker, list)) for i in range(10)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(list)


if __name__ == '__main__':
    main()
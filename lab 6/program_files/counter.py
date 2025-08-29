import threading
import time

def count():
    global counter
    while counter < 1000:
        counter += 1
    return (counter)

def main():
    global counter
    #Последовательное выполнение
    counter = 0
    start = time.time()
    for i in range (1000):
        counter = counter + 1
    end = time.time()
    print(f"Время выполнения: {end - start}")
    print(f"Итоговое значение: {counter}")

    #Параллельное выполнение
    start = time.time()
    counter = 0
    threads = []
    for i in range(0, 10):
        thread = threading.Thread(target=count, args=())
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    print(f"Время выполнения: {time.time()-start}")
    print(f"Итоговое значение: {counter}")

if __name__ == "__main__":
    main()
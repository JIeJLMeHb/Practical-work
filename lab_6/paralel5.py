import random
import time
import multiprocessing
import asyncio
import threading

class Lab:
    def paralel(self):
        start = time.time()
        thread = threading.Thread(10)
        thread.start()
        for i in range(100):
            a = random.randint(1, 100)
            print(f'{a}')
        finish = time.time() 
        difference = finish - start
        thread.join()
        print(f'Потоки воссоединились. Многопоточная обработка завершена. Затраченное время:{difference}')
        print('Начинаем обычную обработку')
        start = time.time()
        for i in range(100):
            a = random.randint(1, 100)
            print(f'{a}')
        finish = time.time() 
        difference = finish - start
        print(f'Потоки воссоединились. Обработка завершена. Затраченное время:{difference}')    

    def lock(self):
        with open('text.txt', 'w', encoding='utf-8') as file:
            with multiprocessing.Pool(processes=10) as pool:
                for i in range(10):
                    pool.map(file.write(f'элемент:{random.randint(1,100)}'))

    async def asynchronous_task(self, name, delay):
        print(f"{name} началось чтение файла")
        await asyncio.sleep(delay)
        print(f"{name} завершил файла через {delay} сек")
    
    async def main(self):
        start = time.time()
        
        for i in range(10):
            a = random.randint(0.1 , 5)
            task1 = asyncio.create_task(self.asynchronous_task("Задача 1", a))
            await task1

        
    def __init__(self):
        self.lock()
        self.paralel()
        asyncio.run(self.main())

    def __del__(self):

        pass

Lab()
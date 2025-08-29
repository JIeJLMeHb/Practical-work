import asyncio

async def long_running_task(seconds):
    await asyncio.sleep(seconds)
    print("Успел")

async def async_func():
    seconds = int(input("Введите количество секунд: "))
    try:
        async with asyncio.timeout(3):
            await long_running_task(seconds)
    except TimeoutError:
        print("Время вышло, неудача(")

def main():
    asyncio.run(async_func())

if __name__ == "__main__":
    main()
    
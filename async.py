import asyncio

async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования.')
    for boll in range(5):
        boll += 1
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {boll} шар' )
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_ = asyncio.create_task(start_strongman('Dima', 3))
    task_2 = asyncio.create_task(start_strongman('Lind', 2))
    task_3 = asyncio.create_task(start_strongman('Anton', 5))
    await task_
    await task_2
    await task_3


asyncio.run(start_tournament())
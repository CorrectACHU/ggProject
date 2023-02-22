# import asyncio
#
#
# async def pop(x):
#     print(x ** 3)
#     await asyncio.sleep(3)
#     print('ya spal 3 sec')
#
#
# async def pop1(x):
#     print(x ** 4)
#     await asyncio.sleep(3)
#     print('ya spal 3 sec , no ya vtoroy chel')
#
#
# async def main():
#     task1 = asyncio.create_task(pop(3))
#     task2 = asyncio.create_task(pop1(4))
#
#     await task1
#     await task2
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


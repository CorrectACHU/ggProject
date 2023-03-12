# ------------------------------------


# ------------------------------------
# a = 10
#
#
# def func():
#     print(a)
#     a = 100
#     # it will return run-time error, cause when python compiles this func he will see that a is local variable,
#     # cause it assignment

# ------------------------------------
# d = 10
#
#
# def func(a, b, c):
#     # d is a global scope variable
#     print(a, b, c, d)
#
#
# func(100, 20, 30)


# ------------------------------------
# from functools import reduce
#
# g = reduce(lambda a, b: a + ' ' + b, ('python', 'is', 'awesome!'))
# print(g)

# ------------------------------------
# list1 = [1, 2, 3, 4, 5, 2]
# list2 = [1, 2, 1, 1]
# s = 'python'
#
# print(list(zip(list2, list1, s)))

# ------------------------------------
# def factorial(n, cache={}):
#     if n < 1:
#         return 1
#     elif n in cache:
#         return cache[n]
#     else:
#         print(f'factorial: {n}!')
#         result = n * factorial(n - 1)
#         cache[n] = result
#         return result
#
#
# print(factorial(5))
# print(factorial(6))
# print(factorial(25))
# print(factorial(2))


# ------------------------------------
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

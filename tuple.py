









import timeit
list_time = timeit.timeit(stmt='["red", "green", "blue"]', number=100000000)
print(f"创建列表所需时间: {list_time} 秒")
tuple_time = timeit.timeit(stmt='("red", "green", "blue")', number=100000000)
print(f"创建元组所需时间: {tuple_time} 秒")
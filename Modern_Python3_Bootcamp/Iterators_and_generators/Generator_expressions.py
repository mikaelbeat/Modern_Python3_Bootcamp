
import time

# Generator expression
g = (num for num in range(1,10))
print(next(g))


gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time


print(f"sum(n for n in range(100000000)) took: {gen_time}")
print(f"sum([n for n in range(100000000)]) took: {list_time}")
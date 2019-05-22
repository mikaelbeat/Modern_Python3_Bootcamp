
import sys

list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))


print("Doing same thing it takes...")
print(f"List comprehension {list_comp} bytes ")
print(f"Generator expression {gen_exp} bytes ")


print("\n***** Getting size of string in bytes ******\n")
data = "Demo data for evaluating purposes"
print(sys.getsizeof(data))
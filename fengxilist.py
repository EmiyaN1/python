import timeit
import random

y_1 = []
y_2 = []
print("lst_time         dict_time")
for i in range(10000, 1000001, 25000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: 'k' for j in range(i)}
    dict_time = t.timeit(number=1000)
    print("{:.6f}        {:.6f}".format(lst_time, dict_time))
    y_1.append(lst_time)
    y_2.append(dict_time)
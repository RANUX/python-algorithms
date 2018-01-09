import matplotlib.pyplot as plt
import random
import timeit


print('N\tSum time')
n=[]
t = []
for trial in [2**_ for _ in range(1,9)]:
  numbers = [random.randint(1,9) for _ in range(trial)]
  m = timeit.timeit(stmt="sum = 0\nfor d in numbers:\n\tsum = sum + d", setup="import random\nnumbers = "+str(numbers))
  n.append(trial)
  t.append(m)
  print('{0:d} {1:f}'.format(trial, m))

plt.plot(t, n)
plt.xlabel('N')
plt.ylabel('Time')
plt.title('O(N)')
plt.show()
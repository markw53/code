import random
from collections import Counter

sides = range(1,7)
num_throws = 1000

counter = Counter(random.choices(sides, k = num_throws))

print(counter)





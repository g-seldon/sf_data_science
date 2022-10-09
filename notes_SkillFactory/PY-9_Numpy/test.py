import numpy as np
#print(np.float64(np.array([345234, 876362.12, 0, -1000, 99999999])))
arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(step)

np.random.seed(100)
print(np.random.randint(10, size=3))
# [8 8 3]
print(np.random.randint(10, size=3))
# [7 7 0]
print(np.random.randint(10, size=3))
# [4 2 5]

print(2**15)

l = [19, 242, 14, 152, 142, 1000]

print(np.mean(l))
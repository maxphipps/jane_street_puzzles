import numpy as np
from numpy.linalg import inv

"""
Puzzle name: 'Lesses More'
"""

corners = np.array((3,1,0))
op = np.array([[1, 0, -1],
               [1, -1, -1],
               [0, 1, -2]])
print(corners)
print('Begin recursive generation')
n=0
for i in range(100):
    n+=1
    corners2 = [_*2. for _ in corners]
    corners2 = np.dot(inv(op), corners2)
    # scale to maintain integer
    # common factors
    while np.all([_%2 == 0 for _ in corners2]):
        corners2 = [_/2. for _ in corners2]
    print(n, corners2)
    # check found soln
    if any([_ > 10000000 for _ in corners2]):
        print('10mn cap breached')
        print('returning', corners)
        break
    # else iterate with the new trial set
    corners = corners2

print(f'solution\'s sum = {sum(corners)}\n')

corners = np.append(corners, [0])
print('start validation')
n=1
print(n, corners)
op = np.array([[1, 0, 0, -1],
               [1, -1, 0, 0],
               [0, 1, -1, 0],
               [0, 0, 1, -1]])
for i in range(100):
    n+=1
    corners = abs(np.dot(op, corners))
    print(n, corners)
    if all(corners == [0.,0.,0.,0.]):
        break

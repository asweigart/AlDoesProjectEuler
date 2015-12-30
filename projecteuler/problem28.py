import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)
# make the grid
grid = {}

x = 0
y = 0

topEdge = 0
bottomEdge = 0
leftEdge = 0
rightEdge = 0
direction = 'right'

n = 1
while n <= 1001 * 1001:
    grid[(x, y)] = n
    logging.debug('grid %s, %s set to %s' % (x, y, n))
    #import pdb; pdb.set_trace()
    n += 1

    # move xy in the direction
    if direction == 'right':
        x += 1
    elif direction == 'left':
        x -= 1
    elif direction == 'up':
        y += 1
    elif direction == 'down':
        y -= 1

    # determine if a new direction is needed (if xy is past the boundaries)
    if direction == 'right' and x > rightEdge:
        rightEdge = x
        direction = 'down'
    elif direction == 'left' and x < leftEdge:
        leftEdge = x
        direction = 'up'
    elif direction == 'up' and y > topEdge:
        topEdge = y
        direction = 'right'
    elif direction == 'down' and y < bottomEdge:
        bottomEdge = y
        direction = 'left'

assert grid[(0, 0)] == 1, grid[(0,0)]
assert grid[(1, 0)] == 2, grid[(1,0)]
assert grid[(1, -1)] == 3, grid[(1,-1)]
assert grid[(0, -1)] == 4, grid[(0,-1)]
assert grid[(-1, -1)] == 5, grid[(-1,-1)]
assert grid[(-1, 0)] == 6, grid[(-1,0)]
assert grid[(-1, 1)] == 7, grid[(-1,1)]
assert grid[(0, 1)] == 8, grid[(0,1)]
assert grid[(1, 1)] == 9, grid[(1,1)]

# add up the diagonals
total = 1 # we'll include the center and skip it in the loop
# note that right/top edge will be 1 more from the last move, which is why we don't have rightEdge + 1:
for i in range(leftEdge, rightEdge): # doesn't matter if we use left/right or top/bottom since they're the same
    if i == 0:
        continue # skip center
    total += grid[(i, i)]
    total += grid[(i, -i)]
print(total)

import math

def distance(a, b):
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2);

def vector(a, b):
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    return b[0] - a[0], b[1] - a[1], b[2] - a[2]

#norm = distance
def norm(v):
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

def normalize(v):
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    n = norm(v)
    return v[0] / n, v[1] / n, v[2] / n

def cross(u, v):
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0]
    )

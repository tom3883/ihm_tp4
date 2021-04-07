import math

def distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2);

def vector(a, b):
    return b[0] - a[0], b[1] - a[1], b[2] - a[2]

#norm = distance
def norm(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

def normalize(v):
    n = norm(v)
    return v[0] / n, v[1] / n, v[2] / n

def cross(u, v):
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0]
    )

def vector2D(a,b):
    return b[0] - a[0], b[1] - a[1]

def norm2D(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1])

def normalize2D(v):
    n = norm2D(v)
    return v[0] / n, v[1] / n
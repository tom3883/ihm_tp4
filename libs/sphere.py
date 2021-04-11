import math
import libs.geometry as _geo

try:
    from OpenGL.GL      import *
    from OpenGL.GLU     import *
    from OpenGL.GLUT    import *
except:
    print ('''ERROR: PyOpenGL not installed properly.''')

class sphere:
    def __init__(self, p, r):
        self.position   = p
        self.radius     = r

    #This function computes and returns the projection of a sphere position on the screen, AND the projected radius (use Thales)
    #Be careful !!! This function takes the current camera stack !!!
    def project(self, camera):

        #Position de M par rapport à la caméra d'une sphere
        wx, wy, wz = gluProject(self.position[0], self.position[1], self.position[2], glGetDouble(GL_MODELVIEW_MATRIX), glGetDouble(GL_PROJECTION_MATRIX))
        wy = glutGet(GLUT_WINDOW_HEIGHT) - wy
        self.proj_position = [wx, wy, 0]

        #Point M' d'une sphère
        self.newPoint = [
            self.position[0] + self.radius * camera.up[0],
            self.position[1] + self.radius * camera.up[1],
            self.position[2] + self.radius * camera.up[2]
        ]

        #Position de M' par rapport à la caméra d'une sphere
        wx, wy, wz = gluProject(self.newPoint[0], self.newPoint[1], self.newPoint[2], glGetDouble(GL_MODELVIEW_MATRIX), glGetDouble(GL_PROJECTION_MATRIX))
        wy = glutGet(GLUT_WINDOW_HEIGHT) - wy
        self.position_newpoint = [wx, wy, 0]

        self.proj_radius = _geo.norm(_geo.vector(self.proj_position, self.position_newpoint))

        #print(self.proj_position, self.proj_radius)
        #print(self.proj_position)
        return self.proj_position, self.proj_radius

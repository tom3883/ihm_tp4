﻿#!/usr/bin/env python3

import sys
import time
import math
from math import *
import random

import libs.camera      as _cam
import libs.sphere      as _sph
import libs.geometry    as _geo

try:
    from OpenGL.GL      import *
    from OpenGL.GLU     import *
    from OpenGL.GLUT    import *
except:
    print ('''ERROR: PyOpenGL not installed properly.''')

################################################################################
# GLOBAL VARS

camera          = _cam.camera([0, 0, 10], [0, 0, 0])#main camera
starting_time   = time.time()                       #starting time of course
mouse           = [0, 0]                            #mouse current position
animation       = False                             #(des)activating animation (juste for fun)
spheres         = []                                #list of the spheres to select

################################################################################
# SETUPS

def stopApplication():
    sys.exit(0)


def setupScene():
    '''OpenGL and Scene objects settings
    '''
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0., 100., 100., 1.))
    glLightfv(GL_LIGHT0, GL_AMBIENT,(.1, .1, .1, 1.))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,(.7, .7, .7, 1.))

    glEnable(GL_CULL_FACE)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT,GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(.4, .4, .4, 1)

    global spheres, nb_spheres, cible
    cible = 1
    nb_spheres = 9
    spheres = create_spheres()


################################################################################
# COMPUTATIONS

def create_spheres():
    '''Create the spheres to select: 3d position and radius
    '''
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    posx, posy = 0,0
    radius = 3
    s = []
    for i in range(nb_spheres):
        cosine = radius * cos(i*2*pi/nb_spheres) + posx
        sine = radius * sin(i*2*pi/nb_spheres) + posy
        s.append(_sph.sphere([cosine, sine, 0], 0.5))
    return s


def setCible():
    """
    for i in range(nb_spheres):
        proj = spheres[i].project(camera)
        display_2d_disc(*proj, [0,1,0,0])

    proj = spheres[0].project(camera)
    #0,1,0 couleur = verte
    display_2d_disc(*proj, [0,1,0])
    """

    for i in range(nb_spheres):
        #Set the color to the new one
        if((i+4)>nb_spheres-1):
            index = nb_spheres-4
        else:
            index = i+4
        proj = spheres[i].project(camera)
        display_2d_disc(*proj, [0,1,0])

        #Previous  disc should become transparent
        prev_proj = spheres[index].project(camera)
        display_2d_disc(*prev_proj, [0,1,1])

def mousePos():
    #GetCursorPos() => returns true
    return x,y

def aCLique():
    return True


def closest_sphere(sphs, cam, m):
    '''Returns the index of the sphere (in list 'sphs') whose projection is the closest to the 2D position 'm'
    '''
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    if not len(sphs):
        raise ValueError("No Sphere")

    mx, my = m
    select_dist = None
    index = None

    for i, sphere in enumerate(sphs):
        (wx, wy, wz), radius = sphere.project(cam)
        dx = mx - wx
        dy = my - wy
        dist = math.sqrt(dx * dx + dy * dy)
        if select_dist is None or dist < select_dist:
            select_dist = dist
            index = i
    return i

################################################################################
# DISPLAY FUNCS

def display_frame():
    '''Display an orthonormal frame + a wire cube
    '''
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    glColor(1,1,1)
    glDisable(GL_LIGHTING)
    glutWireCube(10)
    glEnable(GL_LIGHTING)

    glBegin(GL_LINES)
    glColor(1, 0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(100, 0 ,0)
    glEnd()
    pass


def display_scene(sphs):
    '''display of the whole scene, mainly the spheres (in white)
    '''
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    for i in spheres:
        glPushMatrix()
        glColor(1,0,0)
        glTranslate(i.position[0], i.position[1], i.position[2])
        glutSolidSphere(i.radius, 50, 50)
        glPopMatrix()


def display_2d_disc(p2d, r, c):
    '''Display a disc on a 2d position of the screen
    '''
    w, h = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
    glDisable(GL_LIGHTING)
    glPushMatrix()
    reshape_ortho(w, h)
    glLoadIdentity()
    glTranslate(p2d[0], p2d[1], -1)
    glColor(*c)
    glScale(1, 1, 0.000001)
    glutSolidSphere(r, 20, 20)
    glEnable(GL_LIGHTING)
    reshape_persp(w, h)
    glPopMatrix()

#def remove_2d_disc(p2d, r, c):



def display_bubble(sphere, pos_2d, color):
    '''display the bubble, i.e display a 2d transparent disc that encompasses the mouse and
        the 2d projection of the sphere
    '''
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #glEnable(GL_BLEND)
    #glColor(*color)
    #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    pass



def display():
    '''Global Display function
    '''

    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity ()             # clear the matrix

    ###############
    #Point of View
    gluLookAt ( camera.position[0], camera.position[1], camera.position[2],
                camera.viewpoint[0], camera.viewpoint[1], camera.viewpoint[2],
                camera.up[0], camera.up[1], camera.up[2])

    ###############
    #Frame
    display_frame()
    display_scene(spheres)


    #ind = closest_sphere(spheres, camera, mouse)
    #display_bubble(spheres[ind], mouse, [0, 2, 0, .2])

    #draw_circle()

    glutSwapBuffers()


def reshape_ortho (w, h):
    '''Orthogonal matrix for the projection
        Also called by windows rescaling events
    '''
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    glOrtho(0, w, h, 0, camera.near, camera.far)
    glMatrixMode (GL_MODELVIEW)


def reshape_persp (w, h):
    '''Perspective matrix for the projection
        Called by windows rescaling events
    '''
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(60.0,float(w)/float(h),camera.near,camera.far)
    glMatrixMode (GL_MODELVIEW)


def idle():
    '''Called when opengl has nothing else to do ...
    '''
    if animation:
        t = time.time()
        dt = t - starting_time
        x = 10*math.cos(dt*math.pi/2.)
        z = 10*math.sin(dt*math.pi/2.)
        camera.position[0] = x
        camera.position[2] = z
    glutPostRedisplay()


################################################################################
## INTERACTION FUNCS

def keyboard(key, x, y):
    '''Called when a keyboard ascii key is pressed
    '''
    if key == b'\x1b':
        stopApplication()
    elif key == b'a':
        global animation
        animation = not animation
    else:
        print ("key", key)


def mouse_clicks(button, state, x, y):
    '''Called when a mouse's button is pressed or released
    button is in [GLUT_LEFT_BUTTON, GLUT_MIDDLE_BUTTON, GLUT_RIGHT_BUTTON],
    state is in [GLUT_DOWN, GLUT_UP]
    '''
    global mouse
    mouse = [x, y]
    pos_cible, radius = spheres[cible].project(camera)
    
    if(pos_cible[0] - radius < mouse[0] and pos_cible[0] + radius > mouse[0] and
    pos_cible[1] + radius > mouse[1] and pos_cible[1] - radius < mouse[1]):
        print("Clic sur cible")
    else:
        print("Clic ailleurs")

    glutPostRedisplay()


def mouse_active(x, y):
    '''Called when mouse moves while on of its button is pressed
    '''
    global mouse
    mouse = [x, y]
    glutPostRedisplay()


def mouse_passive(x, y):
    '''Called when mouse hovers over the window
    '''
    global mouse
    mouse =[x, y]
    glutPostRedisplay()


################################################################################
# MAIN

print("Commands:")
print("\ta:\tanimation")
print("\tesc:\texit")

glutInit(sys.argv)
glutInitDisplayString(b'double rgba depth')
glutInitWindowSize (800, 600)
glutInitWindowPosition (0, 0)
glutCreateWindow(b'Bubble')

setupScene()

glutDisplayFunc(display)
glutReshapeFunc(reshape_persp)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse_clicks)
glutMotionFunc(mouse_active)
glutPassiveMotionFunc(mouse_passive)
glutIdleFunc(idle)
glutMainLoop()
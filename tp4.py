#!/usr/bin/env python3

import sys
import time
import math
from math import *
import random
import csv

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

user            = None
camera          = _cam.camera([0, 0, 10], [0, 0, 0])#main camera
starting_time   = time.time()                       #starting time of course
mouse           = [0, 0]                            #mouse current position
animation       = False                             #(des)activating animation (juste for fun)
spheres         = []                                #list of the spheres to select
cible           = 0
nb_spheres      = 9
clic_faux       = False
pointage        = 0
seq             = 0
ids             = [ [1.4, 0.2, "ID3"], [2.1, 0.3, "ID3"], [2.8, 0.4, "ID3"]	, [3.5, 0.5, "ID3"], [4.2, 0.6, "ID3"],
                  [4.5 ,0.3, "ID4"], [4, 0.2666, "ID4"], [3, 0.2, "ID4"], [2, 0.1333, "ID4"], [3.5, 0.2333, "ID4"],
                  [3.1 ,0.1, "ID5"], [4.65, 0.15, "ID5"], [3.875, 0.125, "ID5"], [4.70, 0.1516, "ID5"], [4.80, 0.1548, "ID5"] ]
last_click_time = None
times           = [[]]
errs            = [[]]

print(starting_time)
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
    glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT,GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(.4, .4, .4, 1)

    global spheres, last_click_time
    spheres = create_spheres()
    last_click_time = time.time()


################################################################################
# COMPUTATIONS

def create_spheres():
    '''Create the spheres to select: 3d position and radius
    '''
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    posx, posy = 0,0
    radius = ids[seq][0]
    s = []
    for i in range(nb_spheres):
        cosine = radius * cos(i*2*pi/nb_spheres) + posx
        sine = radius * sin(i*2*pi/nb_spheres) + posy
        s.append(_sph.sphere([cosine, sine, 0], ids[seq][1]))
    return s


def setDiscs():

    for i in range(nb_spheres):
        proj = spheres[i].project(camera)
        display_2d_disc(*proj, [0,1,0,0])

    proj = spheres[0].project(camera)
    #0,1,0 couleur = verte
    display_2d_disc(*proj, [0,1,0])

def testEnd():

    with open('results.csv', mode='a', newline='') as results_file:

        fields = ["nom", "technique", "ID", "temps", "erreur"]
        results_writer = csv.DictWriter(results_file, fieldnames=fields)

        for i in range(len(times)):
            for j in range(len(times[i])):
                results_writer.writerow({
                    "nom": user, "technique" : "Clic classique",
                    "ID" : ids[i][2], "temps" : str(times[i][j]),
                    "erreur" : str(errs[i][j])
                })

    glutLeaveMainLoop()

def isCible(sphere):
    return sphere == spheres[cible]


def nextCible():
    global cible
    if((cible+4) >= nb_spheres):
        cible = (cible + 4) - nb_spheres
    else:
        cible += 4
    #print(new_cible)


def nextSeq():
    global seq, spheres
    if(seq+1 < len(ids)):
        seq += 1
    else:
        return testEnd()
    #print(str(seq))
    spheres = create_spheres()


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


def display_scene():
    '''display of the whole scene, mainly the spheres
    '''
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    #TODO_TODO_TODO
    for i in spheres:
        glPushMatrix()
        if isCible(i):
            glColor(0,1,0)
        else:
            glColor(0.6,0.6,0.6)
        glTranslate(i.position[0], i.position[1], i.position[2])
        glutSolidSphere(i.radius, 50, 50)
        glPopMatrix()

    #setDiscs()


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
    display_scene()


    #ind = closest_sphere(spheres, camera, mouse)
    #display_bubble(spheres[ind], mouse, [0, 2, 0, .2])
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
    if state == GLUT_DOWN:
        global mouse, clic_faux, pointage, last_click_time, times, errs
        mouse = [x, y]
        pos_cible, radius = spheres[cible].project(camera)

        #Calcul du temps entre 2 clics
        click_time = time.time()

        #Temps écoulé entre 2 sphères
        time_elapsed = click_time - last_click_time

        #Temps du dernier clic mis à jour
        last_click_time = click_time

        times[seq].append(time_elapsed)

        if(pos_cible[0] - radius < mouse[0] and pos_cible[0] + radius > mouse[0] and
        pos_cible[1] + radius > mouse[1] and pos_cible[1] - radius < mouse[1]):
            clic_faux = False
        else:
            clic_faux = True

        errs[seq].append(clic_faux)
        nextCible()
        pointage+=1

        if pointage == 9:
            print(times)
            print(errs)
            errs.append([])
            times.append([])
            pointage = 0
            nextSeq()

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

user = input("Quel est votre nom : ")

random.shuffle(ids)

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

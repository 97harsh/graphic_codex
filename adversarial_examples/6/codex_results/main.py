
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(0,0,0,1)

def draw_planet():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(1,0,0)
    glutWireSphere(1,20,20)
    glTranslatef(5,0,0)
    glColor3f(0,1,0)
    glutWireSphere(0.2,20,20)
    glRotatef(angle,0,0,1)
    glTranslatef(5,0,0)
    glColor3f(0,0,1)
    glutWireSphere(0.1,20,20)
    glFlush()

angle = 0
def animate(x):
    global angle
    angle += 2
    glutPostRedisplay()
    glutTimerFunc(50,animate,0)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Solar System")
glutDisplayFunc(draw_planet)
glutTimerFunc(50,animate,0)
init()
glutMainLoop()
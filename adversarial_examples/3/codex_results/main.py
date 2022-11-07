from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 0, 1, 0)
    glutWireCube(0.5)
    glutSolidSphere(0.2, 20, 20)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow("First")
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()
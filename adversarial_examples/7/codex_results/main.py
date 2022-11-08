"""
write a code to generate reversed cone in opengl python
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
	glClearColor(0.0,0.0,0.0,1.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60,1,1,30)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(5,5,10,0,0,0,0,1,0)

def drawFunc():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glutWireCone(2,3,20,20)
	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(500,500)
glutCreateWindow("Cone")
glutDisplayFunc(drawFunc)
init()
glutMainLoop()
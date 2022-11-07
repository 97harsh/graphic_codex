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

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glutWireCube(2)
	glTranslate(0,2,0)
	glColor3f(0.0,0.0,1.0)
	glutWireCube(2)
	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"Two Cube")
glutDisplayFunc(draw)
init()
glutMainLoop()
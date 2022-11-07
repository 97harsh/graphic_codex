from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	glColor3f(0.0,0.0,0.0)
	glPointSize(1.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)

def triangle():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLES)
	glVertex2f(100.0,100.0)
	glVertex2f(200.0,100.0)
	glVertex2f(150.0,200.0)
	glEnd()
	glFlush()

def mirror():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLES)
	glVertex2f(100.0,100.0)
	glVertex2f(200.0,100.0)
	glVertex2f(150.0,200.0)
	glEnd()
	glFlush()
	glBegin(GL_TRIANGLES)
	glVertex2f(100.0,300.0)
	glVertex2f(200.0,300.0)
	glVertex2f(150.0,200.0)
	glEnd()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(640,480)
	glutInitWindowPosition(200,200)
	glutCreateWindow("Triangle and Mirror Image")
	glutDisplayFunc(mirror)
	init()
	glutMainLoop()

main()
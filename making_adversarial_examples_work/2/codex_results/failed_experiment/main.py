from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5,-0.5)
    glVertex2f(-0.5,0.5)
    glVertex2f(0.5,0.5)
    glVertex2f(0.5,-0.5)
    glEnd()
    glFlush()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.25,-0.25)
    glVertex2f(-0.25,0.25)
    glVertex2f(0.25,0.25)
    glVertex2f(0.25,-0.25)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow(b'plotpoints')
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

main()
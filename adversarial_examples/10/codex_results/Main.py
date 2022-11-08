from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

# The coordinates of the vertices of the triangle
v1 = [0.0, 0.0]
v2 = [0.0, 0.0]
v3 = [0.0, 0.0]

# The number of points in the gasket
numpoints = 10000

def init():
    """
    Initialize the parameters
    """
    global v1, v2, v3
    v1[0] = -1.0
    v1[1] = -1.0
    v2[0] = 1.0
    v2[1] = -1.0
    v3[0] = 0.0
    v3[1] = 1.0
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)

def display():
    """
    Display the gasket
    """
    global v1, v2, v3
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    x = [0.0, 0.0]
    x[0] = v1[0]
    x[1] = v1[1]
    for i in range(numpoints):
        j = random.randint(1, 3)
        if j == 1:
            x[0] = (x[0] + v1[0]) / 2.0
            x[1] = (x[1] + v1[1]) / 2.0
        elif j == 2:
            x[0] = (x[0] + v2[0]) / 2.0
            x[1] = (x[1] + v2[1]) / 2.0
        else:
            x[0] = (x[0] + v3[0]) / 2.0
            x[1] = (x[1] + v3[1]) / 2.0
        glVertex2fv(x)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Sierpinski Gasket")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()
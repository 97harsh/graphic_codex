from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math

n = 10


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    for i in range(0, 360, 360 // n):
        rad = (3.141592 * i) / 180
        glVertex3f(math.cos(rad), math.sin(rad), 0)
    glEnd()
    glFlush()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutCreateWindow("poligono regular")

    glClearColor(0., 0., 0., 1.)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 1, 40)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

    glRotatef(45, 1, 1, 1)

    glutDisplayFunc(draw)
    # glutTimerFunc(50,timer,1)
    glutMainLoop()


if __name__ == '__main__':
    main()
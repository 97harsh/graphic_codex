from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
from math import *


def myInit():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0);
    glPointSize(1.0);
    gluOrtho2D(-640.0, 640.0, -640.0, 640.0);


def plotPoints():
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_POINTS);
    r = 300;
    for i in range(0, 1801):
        angle = i * 2 * pi / 1800;
        x = r * cos(angle);
        y = r * sin(angle);
        glVertex2f(x, y);
    glEnd();
    glFlush();


def main():
    glutInit(sys.argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowPosition(50, 50);
    glutInitWindowSize(640, 640);
    glutCreateWindow('Circle filled');
    myInit();
    glutDisplayFunc(plotPoints);
    glColor3f(1.0, 0.0, 0.0);
    glutMainLoop();


main();
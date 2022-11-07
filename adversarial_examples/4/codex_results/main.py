from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(1.0,1.0,1.0,0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,400.0,0.0,300.0)

def draw_pixel(x,y):
    glColor3f(1.0,0.0,1.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def draw_text(x,y,text):
    glColor3f(1.0,0.0,1.0)
    glRasterPos2f(x,y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(ch))

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_pixel(50,50)
    draw_text(50,50,"hello world")

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,100)
    glutInitWindowSize(400,300)
    glutCreateWindow("Hello World")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()
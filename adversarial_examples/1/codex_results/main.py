import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def Ball(radius, color):
    glColor3f(*color)
    glTranslatef(0,0,radius)
    quad=gluNewQuadric()
    gluSphere(quad, radius, 20, 20)
    glTranslatef(0,0,-radius)

def main():
    pygame.init()

    display=(800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45,(display[0]/display[1]),0.1,50.0)

    glTranslatef(0.0,0.0,-5)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pos_x = 0
        pos_y = 0
        pos_z = 0
        for x in range(10):
            glPushMatrix()

            glTranslatef(pos_x, pos_y, pos_z)
            Ball(0.5, (0, 1, 0))

            glPopMatrix()
            pos_x += 0.5
            pos_z += 0.5

        glRotatef(1,3,1,1)
        pygame.display.flip()
        pygame.time.wait(5)


main()
# Import the necessary packages
import glfw
from OpenGL.GL import *
import numpy as np
import math

def drawHexagon():
    # Defining vertices of hexagon
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2*math.pi, 2*math.pi/6):
        x, y = math.cos(theta), math.sin(theta)
        glVertex3f(x, y, 0)
    glEnd()

def drawSphere(radius, n):
    # Defining vertices of sphere
    # Draw a sphere using a hexagon
    glColor3f(1,1,1)
    for i in np.arange(0, n+1, 1):
        glBegin(GL_POLYGON)
        for j in np.arange(0, n+1, 1):
            theta = i * 2.0*math.pi / n
            phi = j * 2.0*math.pi / n
            x = radius * math.cos(phi) * math.cos(theta)
            y = radius * math.cos(phi) * math.sin(theta)
            z = radius * math.sin(phi)
            glVertex3f(x, y, z)
        glEnd()

def drawCube(r):
    # Defining vertices of cube
    glColor3f(0,1,0)
    glBegin(GL_QUADS)
    glVertex3f( r, r, -r)
    glVertex3f(-r, r, -r)
    glVertex3f(-r, r,  r)
    glVertex3f( r, r,  r)

    glVertex3f( r, -r,  r)
    glVertex3f(-r, -r,  r)
    glVertex3f(-r, -r, -r)
    glVertex3f( r, -r, -r)

    glVertex3f( r,  r,  r)
    glVertex3f(-r,  r,  r)
    glVertex3f(-r, -r,  r)
    glVertex3f( r, -r,  r)

    glVertex3f( r, -r, -r)
    glVertex3f(-r, -r, -r)
    glVertex3f(-r,  r, -r)
    glVertex3f( r,  r, -r)

    glVertex3f(-r,  r,  r)
    glVertex3f(-r,  r, -r)
    glVertex3f(-r, -r, -r)
    glVertex3f(-r, -r,  r)

    glVertex3f( r,  r, -r)
    glVertex3f( r,  r,  r)
    glVertex3f( r, -r,  r)
    glVertex3f( r, -r, -r)
    glEnd()

def drawCylinder(r, h):
    # Defining vertices of cylinder
    glColor3f(0,0,1)
    glBegin(GL_TRIANGLES)
    for i in np.arange(0, 10, 1):
        for j in np.arange(0, 6, 1):
            theta = j * 2.0*math.pi / 6
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex3f(x, y, 0)
            theta = (j+1) * 2.0*math.pi / 6
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex3f(x, y, 0)
            glVertex3f(0, 0, h)
    glEnd()
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    for i in np.arange(0, 10, 1):
        for j in np.arange(0, 6, 1):
            theta = j * 2.0*math.pi / 6
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex3f(x, y, 0)
            theta = (j+1) * 2.0*math.pi / 6
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex3f(x, y, 0)
            glVertex3f(0, 0, h)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 0, 1, 0)
    drawHexagon()
    drawSphere(0.2, 10)
    drawCube(0.2)
    drawCylinder(0.1, 0.3)

def main():
    # initialize glfw
    if not glfw.init():
        return

    width, height = 800, 600

    window = glfw.create_window(width, height, "CS475/CS675 Tutorial 1", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        draw()

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
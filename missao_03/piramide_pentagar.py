import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

modo = 0


def modoCamera():
    global modo

    if modo == 0:
        glu.gluLookAt(0.0, 0.0, 6.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0)
    elif modo == 1:
        glu.gluLookAt(6.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0)
    elif modo == 2:
        glu.gluLookAt(0.0, 6.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, -1.0)


def desenharPiramidePentagar():
    modoCamera()

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45.0, 1.0, 0.1, 50.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    modoCamera()

    gl.glBegin(gl.GL_POLYGON)
    gl.glColor3f(0.5, 0.5, 0.5)
    gl.glVertex3f(1.0, 0.0, 0.0)
    gl.glVertex3f(0.31, 0.95, 0.0)
    gl.glVertex3f(-0.81, 0.59, 0.0)
    gl.glVertex3f(-0.81, -0.59, 0.0)
    gl.glVertex3f(0.31, -0.95, 0.0)
    gl.glEnd()

    gl.glBegin(gl.GL_TRIANGLES)

    gl.glColor3f(0.2, 0.0, 0.0)
    gl.glVertex3f(1.0, 0.0, 0.0)
    gl.glVertex3f(0.31, 0.95, 0.0)
    gl.glVertex3f(0.0, 0.0, 2.0)

    gl.glColor3f(0.4, 0.0, 0.0)
    gl.glVertex3f(0.31, 0.95, 0.0)
    gl.glVertex3f(-0.81, 0.59, 0.0)
    gl.glVertex3f(0.0, 0.0, 2.0)

    gl.glColor3f(0.6, 0.0, 0.0)
    gl.glVertex3f(-0.81, 0.59, 0.0)
    gl.glVertex3f(-0.81, -0.59, 0.0)
    gl.glVertex3f(0.0, 0.0, 2.0)

    gl.glColor3f(0.8, 0.0, 0.0)
    gl.glVertex3f(-0.81, -0.59, 0.0)
    gl.glVertex3f(0.31, -0.95, 0.0)
    gl.glVertex3f(0.0, 0.0, 2.0)

    gl.glColor3f(0.1, 0.0, 0.0)
    gl.glVertex3f(0.31, -0.95, 0.0)
    gl.glVertex3f(1.0, 0.0, 0.0)
    gl.glVertex3f(0.0, 0.0, 2.0)

    gl.glEnd()

    glut.glutSwapBuffers()


def comando(key, x, y):
    global modo

    if key == glut.GLUT_KEY_UP:
        modo = 0
    elif key == glut.GLUT_KEY_LEFT:
        modo = 1
    elif key == glut.GLUT_KEY_RIGHT:
        modo = 2

    glut.glutPostRedisplay()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutInitWindowSize(600, 600)
glut.glutCreateWindow(b"Missao 3 - A Piramide de Pentagar")

gl.glEnable(gl.GL_DEPTH_TEST)

glut.glutDisplayFunc(desenharPiramidePentagar)
glut.glutSpecialFunc(comando)
glut.glutMainLoop()
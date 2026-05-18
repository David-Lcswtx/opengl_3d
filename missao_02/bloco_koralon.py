import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

modo = 0


def modoCamera():
    global modo

    if modo == 0:
         glu.gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif modo == 1:
        glu.gluLookAt(5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif modo == 2:
        glu.gluLookAt(3.0, 3.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def desenharBlocoKoralon():
    modoCamera()

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45.0, 1.0, 0.1, 50.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    modoCamera()

    gl.glBegin(gl.GL_QUADS)

    # Face Frontal
    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glVertex3f(-1.2, -0.5, 0.5)
    gl.glVertex3f(1.2, -0.5, 0.5)
    gl.glVertex3f(1.2, 0.5, 0.5)
    gl.glVertex3f(-1.2, 0.5, 0.5)

    # Face Traseira
    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex3f(-1.2, -0.5, -0.5)
    gl.glVertex3f(-1.2, 0.5, -0.5)
    gl.glVertex3f(1.2, 0.5, -0.5)
    gl.glVertex3f(1.2, -0.5, -0.5)

    # Face Superior
    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glVertex3f(-1.2, 0.5, -0.5)
    gl.glVertex3f(-1.2, 0.5, 0.5)
    gl.glVertex3f(1.2, 0.5, 0.5)
    gl.glVertex3f(1.2, 0.5, -0.5)

    # Face Inferior
    gl.glColor3f(1.0, 1.0, 0.0)
    gl.glVertex3f(-1.2, -0.5, -0.5)
    gl.glVertex3f(1.2, -0.5, -0.5)
    gl.glVertex3f(1.2, -0.5, 0.5)
    gl.glVertex3f(-1.2, -0.5, 0.5)

    # Face Lateral Direita
    gl.glColor3f(1.0, 0.0, 1.0)
    gl.glVertex3f(1.2, -0.5, -0.5)
    gl.glVertex3f(1.2, 0.5, -0.5)
    gl.glVertex3f(1.2, 0.5, 0.5)
    gl.glVertex3f(1.2, -0.5, 0.5)

    # Face Lateral Esquerda
    gl.glColor3f(1.0, 0.5, 0.0)
    gl.glVertex3f(-1.2, -0.5, -0.5)
    gl.glVertex3f(-1.2, -0.5, 0.5)
    gl.glVertex3f(-1.2, 0.5, 0.5)
    gl.glVertex3f(-1.2, 0.5, -0.5)

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
glut.glutCreateWindow(b"Missao 2 - Bloco de Pedra de Koralon")

gl.glEnable(gl.GL_DEPTH_TEST)

glut.glutDisplayFunc(desenharBlocoKoralon)
glut.glutSpecialFunc(comando)
glut.glutMainLoop()
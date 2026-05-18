import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

modo = 0


def modoCamera():
    global modo

    if modo == 0:
        gl.glClearColor(0.0, 0.0, 0.2, 1.0)
        glu.gluLookAt(0.0, 0.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif modo == 1:
        gl.glClearColor(0.2, 0.0, 0.0, 1.0)
        glu.gluLookAt(6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif modo == 2:
        gl.glClearColor(0.0, 0.2, 0.0, 1.0)
        glu.gluLookAt(0.0, 6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)


def desenharCone():
    modoCamera()
    
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45.0, 1.0, 0.1, 50.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    modoCamera()

    gl.glRotate(-90, 1, 0, 0)
    gl.glColor3f(0.0, 0.5, 1.0)
    
    glut.glutWireCone(1.5, 2.0, 19, 10)

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
glut.glutCreateWindow(b"Missao 1 - A Torre do Vortice")

gl.glEnable(gl.GL_DEPTH_TEST)

glut.glutDisplayFunc(desenharCone)
glut.glutSpecialFunc(comando)
glut.glutMainLoop()
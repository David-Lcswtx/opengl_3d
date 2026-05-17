import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

modo = 0

vertices = [
    [0.0, 0.8, 0.6],
    [-0.8, 0.8, -0.6],
    [0.8, 0.8, -0.6],
    [0.0, -0.8, 0.6],
    [-0.8, -0.8, -0.6],
    [0.8, -0.8, -0.6],
]

faces = [[0, 1, 2], [3, 5, 4], [0, 3, 4, 1], [0, 2, 5, 3], [1, 4, 5, 2]]

cores_faces = [
    [1.0, 0.0, 0.0],
    [1.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.1, 1.0],
]


def modoCamera():
    global modo

    if modo == 0:
        glu.gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif modo == 1:
        glu.gluLookAt(5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif modo == 2:
        glu.gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def desenhaPrisma():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45.0, 1.0, 0.1, 50.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    modoCamera()

    for i, face in enumerate(faces):
        gl.glColor3fv(cores_faces[i])
        gl.glBegin(gl.GL_POLYGON)
        for v in face:
            gl.glVertex3fv(vertices[v])
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
glut.glutCreateWindow(b"Missao 4 - A Forja das Formas")

gl.glEnable(gl.GL_DEPTH_TEST)

glut.glutDisplayFunc(desenhaPrisma)
glut.glutSpecialFunc(comando)
glut.glutMainLoop()

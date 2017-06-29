from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys

if (len(sys.argv) > 1):
    BASE = int(sys.argv[1])
else:
    BASE = 4 #alterar a quantidade de vertices aqui

if (len(sys.argv) > 2):
    RAZAO = float(sys.argv[2])
else:
    RAZAO = 0.75

INCREMENTO = radians(360.0 / BASE)

angulo = radians(0)

vertices = ()

for i in range(0, BASE):
    vertices += (
        (cos(angulo), -1, -sin(angulo)),
        )
    angulo = angulo + INCREMENTO

angulo = radians(0)
  
for i in range(0, BASE):
    vertices += (
        (cos(angulo) * RAZAO, 1 * RAZAO, -sin(angulo) * RAZAO),
        )
    angulo = angulo + INCREMENTO

linhas = ()

for i in range(0, BASE - 1):
    linhas += (
        (i, i + 1),
        )

linhas += (
    (BASE - 1, 0),
    )

for i in range(BASE, BASE * 2 - 1):
    linhas += (
        (i, i + 1),
        )

linhas += (
    (BASE * 2 - 1, BASE),
    )

for i in range(0, BASE):
    linhas += (
        (i, i + BASE),
        )

topo = ()

for i in range(0, BASE):
    topo += (
        i,
        )

fundo = ()

for i in range(BASE, BASE * 2):
    fundo += (
        i,
        )

faces = ()

for i in range(0, BASE - 1):
    faces += (
        (i, i + 1, i + BASE + 1, i + BASE),
        )

faces += (
    (BASE - 1, 0, BASE, 2 * BASE - 1),
    )

#https://www.opengl.org/wiki/Calculating_a_Surface_Normal
#Begin Function CalculateSurfaceNormal (Input Triangle) Returns Vector
#  Set Vector U to (Triangle.p2 minus Triangle.p1)
#  Set Vector V to (Triangle.p3 minus Triangle.p1)
#  Set Normal.x to (multiply U.y by V.z) minus (multiply U.z by V.y)
#  Set Normal.y to (multiply U.z by V.x) minus (multiply U.x by V.z)
#  Set Normal.z to (multiply U.x by V.y) minus (multiply U.y by V.x)
#  Returning Normal
#End Function

def calculaNormalFace(face):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]), (U[z]*V[x]-U[x]*V[z]), (U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def Cubo():

    glBegin(GL_POLYGON)
    for vertice in topo:
        glVertex3fv(vertices[vertice])
    glEnd()

    glBegin(GL_QUADS)

    for face in faces:
        glNormal3fv(calculaNormalFace(face))
        i = 0
        for vertex in face:
            if (i == 0):
                glTexCoord2f(0.0, 0.0)
            elif (i == 1):
                glTexCoord2f(1.0, 0.0)
            elif (i == 2):
                glTexCoord2f(1.0, 1.0)
            elif (i == 3):
                glTexCoord2f(0.0, 1.0)
            glVertex3fv(vertices[vertex])
            i = i + 1

    glEnd()

    glBegin(GL_POLYGON)
    for vertice in fundo:
        glVertex3fv(vertices[vertice])

    glEnd()

    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Cubo()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
    LoadTextures()
    glEnable(GL_TEXTURE_2D)

    mat_ambient = (1.0, 1.0, 1.5, 1.0)
    mat_diffuse = (1.0, 1.0, 1.0, 1.0)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    mat_shininess = (50,)
    light_position = (-80, 10, 10, 0.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

# Funcoes da textura:
def LoadTextures():
    global texture
    image = open("textura.rgb").read()

    ix = 256
    iy = 256    
    # Create Texture
    texture = glGenTextures(1)
    # print texture
    
    glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_COMBINE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Cubo")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()

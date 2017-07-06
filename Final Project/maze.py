from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

x = -18.5
z = -5.5

def desenhaCubo():
    y = 1
    tam = 1
    x0 = x - tam/2
    xf = x0 + tam
    y0 = y - tam/2
    yf = y0 + tam
    z0 = z - tam/2
    zf = z + tam
    faces = ((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6))
    vertices = (( xf,y0,z0),( xf, yf,z0),(x0, yf,z0),(x0,y0,z0),( xf,y0, zf),( xf, yf, zf),(x0,y0, zf),(x0, yf, zf))
    glBegin(GL_QUADS)
    i = 0
    glColor3fv((1,1,1))
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()


def paredeH(x0,xf,z,espessura,altura):
    y0 = 0
    yf = y0+altura
    z0 = z - 0.5*espessura
    zf = z + 0.5*espessura
    vertices = ((x0,y0,z0),(x0,y0,zf),(x0,yf,zf),(x0,yf,z0),(xf,yf,z0),(xf,y0,z0),(xf,y0,zf),(xf,yf,zf))
    faces = ((0,1,2,3),(3,0,5,4),(4,5,6,7),(4,5,6,7),(6,7,2,1),(4,7,2,3),(5,6,1,0))
    glColor3fv((0.5,0.1,0.1))
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
#	LoadTextures()
    glEnd()

def paredeV(z0,zf,x,espessura,altura):
    y0 = 0
    yf = y0+altura
    x0 = x - 0.5*espessura
    xf = x + 0.5*espessura
    vertices = ((x0,y0,z0),(x0,y0,zf),(x0,yf,zf),(x0,yf,z0),(xf,yf,z0),(xf,y0,z0),(xf,y0,zf),(xf,yf,zf))
    glColor3fv((1,.5,0))
    faces = ((0,1,2,3),(3,0,5,4),(4,5,6,7),(4,5,6,7),(6,7,2,1),(4,7,2,3),(5,6,1,0))
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

def chao(x0,xf,z,espessura,altura):
    y0 = 0
    yf = y0+altura
    z0 = z - 0.5*espessura
    zf = z + 0.5*espessura
    vertices = ((x0,y0,z0),(x0,y0,zf),(x0,yf,zf),(x0,yf,z0),(xf,yf,z0),(xf,y0,z0),(xf,y0,zf),(xf,yf,zf))
    faces = ((0,1,2,3),(3,0,5,4),(4,5,6,7),(4,5,6,7),(6,7,2,1),(4,7,2,3),(5,6,1,0))
    glColor3fv((0.7,0.5,0.5))
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
#	LoadTextures()
    glEnd()

def desenhaLabirinto():
    espessura = 0.1
    altura = 1
    alt = 0.01
    esp = 26
    w1 = paredeH(-17, 20.0, -5, espessura, altura) #parede1
    w2 = paredeV(-5, 21, -20, espessura, altura) #parede2
    w3 =paredeV(-5, 21, 20, espessura, altura) #parede3
    w4 =paredeH(-20, 17, 21, espessura, altura) #parede4
    w5 =paredeH(-20, -16, 13, espessura, altura) #parede5
    w6 =paredeH(20, 15, 7, espessura, altura) #parede6
    w7 =paredeH(20, 12, 18, espessura, altura) #parede7
    w8 =paredeV(18, 21, -2, espessura, altura) #parede8
    w9 =paredeV(-5, 0,5, espessura, altura) #parede9
    w10 =paredeV(-5, 7,-6, espessura, altura) #parede10
    w11 =paredeH(-2, -16,7, espessura, altura) #parede11
    w12 =paredeV(7, 12, -12, espessura, altura) #parede12
    w13 =paredeV(1, 7,-16, espessura, altura) #parede13
    w14 =paredeH(-16, -11,1, espessura, altura) #parede14
    w15 =paredeV(7, 12,-2, espessura, altura) #parede15
    w16 =paredeH(-2, -6,12, espessura, altura) #parede16
    w17 =paredeV(12, 17,-6, espessura, altura) #parede17
    w18 =paredeH(-14, -6,17, espessura, altura) #parede18
    w19 =paredeV(17, 21, 4, espessura, altura) #parede19
    w20 =paredeH(1, 8, 17, espessura, altura) #parede20
    w21 =paredeV(13, 17, 8, espessura, altura) #parede21
    w22 =paredeH(5, 12, 13, espessura, altura) #parede22
    w23 =paredeV(3, 13, 12, espessura, altura) #parede23
    w24 =paredeV(8, 13, 5, espessura, altura) #parede24
    w25 =paredeH(1, 5, 8, espessura, altura) #parede25
    w26 =paredeV(8, 1, 1, espessura, altura) #parede26
    w27 =paredeH(-3, 1, 1, espessura, altura) #parede27
    w28 =paredeH(9, 15, 3, espessura, altura) #parede28
    w29 =paredeV(3, 9, 9, espessura, altura) #parede29
    w30 =paredeV(7, 13, 15, espessura, altura) #parede30
    w31 =paredeV(17, 12, 1, espessura, altura) #parede31

    chao(-20, 20, 8, esp, alt) #chao   

    array = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25, w26, w27, w28, w29, w30, w31]
    global array

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    desenhaCubo()
    desenhaLabirinto()
    glutSwapBuffers()

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
    # glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_COMBINE)
       

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


def teclaPressionada(tecla, xm, ym):
        global x, z
        if tecla == GLUT_KEY_LEFT:
            print "ESQUERDA"
	    x -= 1
        elif tecla == GLUT_KEY_RIGHT:
	    print "DIREITA"
	    x += 1
	elif tecla == GLUT_KEY_UP:
	    print "CIMA"
	    z -= 1
	elif tecla == GLUT_KEY_DOWN:
	    print "BAIXO"
	    z += 1

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("LABIRINTO")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,150.0)
glTranslatef(0.0,0.0,-60) #joga a cena em posicao diferente (x,y,z) -- (0.0,0.0,-10) joga a cena a distancia -10 da tela
glRotatef(30,1,0,0) #(grau, x, y,z)
glutTimerFunc(50,timer,1)
glutSpecialFunc(teclaPressionada)
glutMainLoop()

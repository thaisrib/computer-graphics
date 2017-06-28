from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
 
# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'
 
# Number of the glut window.
window = 0
 
# Rotations for cube. 
xrot = yrot = zrot = 0.0
 
texture = []
 
def LoadTexture(arquivo, idTextura, i):
    image = open(arquivo).read()
 
    ix = 1134
    iy = 1134  
     
    #glActiveTexture(GL_TEXTURE0+i)
    glBindTexture(GL_TEXTURE_2D, idTextura)   # 2d texture (x and y size)
 
     
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def LoadTextures():
    global texture
    texture = glGenTextures(6)
    LoadTexture("1.rgb",texture[0],0)	
    LoadTexture("2.rgb",texture[1],1)	
    LoadTexture("3.rgb",texture[2],2)	
    LoadTexture("4.rgb",texture[3],3)	
    LoadTexture("5.rgb",texture[4],4)	
    LoadTexture("6.rgb",texture[5],5)	


# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):                # We call this right after our OpenGL window is created.
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    glClearDepth(1.0)                    # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)                # Enables Depth Testing
    glShadeModel(GL_SMOOTH)                # Enables Smooth Color Shading
     
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
 
    glMatrixMode(GL_MODELVIEW)
 
# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:                        # Prevent A Divide By Zero If The Window Is Too Small 
        Height = 1
 
    glViewport(0, 0, Width, Height)        # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
 
# The main drawing function. 
def DrawGLScene():
    global xrot, yrot, zrot, texture
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    # Clear The Screen And The Depth Buffer
    glLoadIdentity()                    # Reset The View
     
    glClearColor(0.5,0.5,0.5,1.0)            
     
    glTranslatef(0.0,0.0,-5.0)            # Move Into The Screen
 
    glRotatef(xrot,1.0,0.0,0.0)            # Rotate The Cube On It's X Axis
    glRotatef(yrot,0.0,1.0,0.0)            # Rotate The Cube On It's Y Axis
    glRotatef(zrot,0.0,0.0,1.0)            # Rotate The Cube On It's Z Axis
     
    # Note there does not seem to be support for this call.
    #glBindTexture(GL_TEXTURE_2D,texture)    # Rotate The Pyramid On It's Y Axis
 
    glBindTexture(GL_TEXTURE_2D, texture[0])   # 2d texture (x and y size)
    glBegin(GL_QUADS)                # Start Drawing The Cube
    # Front Face (note that the texture's corners have to match the quad's corners)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)    # Top Left Of The Texture and Quad
    glEnd()
     
    glBindTexture(GL_TEXTURE_2D, texture[1])   # 2d texture (x and y size)
    glBegin(GL_QUADS)                # Start Drawing The Cube
    # Back Face
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)    # Bottom Left Of The Texture and Quad
    glEnd()
     
     
    glBindTexture(GL_TEXTURE_2D, texture[2])   # 2d texture (x and y size)
    glBegin(GL_QUADS)                # Start Drawing The Cube
    # Top Face
    #glBindTexture(GL_TEXTURE_2D, texture[2])
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)    # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)    # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    # Top Right Of The Texture and Quad
     
    glEnd()
     
    glBindTexture(GL_TEXTURE_2D, texture[3])   # 2d texture (x and y size)
    glBegin(GL_QUADS)                # Start Drawing The Cube
    # Bottom Face       
    #glBindTexture(GL_TEXTURE_2D, texture[3])
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0)    # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    # Bottom Right Of The Texture and Quad
    glEnd()
     
    glBindTexture(GL_TEXTURE_2D, texture[4])   # 2d texture (x and y size)
    glBegin(GL_QUADS)                # Start Drawing The Cube
     
    # Right face
    #glBindTexture(GL_TEXTURE_2D, texture[4])
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad
    glEnd()
     
    glBindTexture(GL_TEXTURE_2D, texture[5])   # 2d texture (x and y size)
    glBegin(GL_QUADS)                # Start Drawing The Cube
     
    # Left Face
    #glBindTexture(GL_TEXTURE_2D, texture[5])
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)    # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)    # Top Left Of The Texture and Quad
     
    glEnd();                # Done Drawing The Cube
     
    xrot  = xrot + 0.3                # X rotation
    yrot = yrot + 0.2                 # Y rotation
    zrot = zrot + 0.4                 # Z rotation
 
    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()
 
# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()
 
def main():
    global window
    glutInit(sys.argv)
 
    # Select type of Display mode:   
    #  Double buffer 
    #  RGBA color
    # Alpha components supported 
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
     
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
     
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
     
    window = glutCreateWindow("Textura")
 
    glutDisplayFunc(DrawGLScene)
     
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
     
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
     
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)
 
    # Initialize our window. 
    InitGL(640, 480)
 
    # Start Event Processing Engine    
    glutMainLoop()
 
# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()

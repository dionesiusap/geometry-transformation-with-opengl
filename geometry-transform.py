# Filename    : geometry-transform
# Author      : Jason Wiguna, Dionesius Agung
# Version     : 2017/04/11
# Description : 2D and 3D geometry transformation simulator with OpenGL

import string
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
import string
from threading import Thread
import time
import thread

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    glClearColor(255.0, 255.0, 255.0, 255.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(520.0, float(Width)/float(Height), 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)


# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small
        Height = 1
    
    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(520.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def glut_print( x,  y,  font,  text, r,  g , b , a):
    
    blending = False
    if glIsEnabled(GL_BLEND) :
        blending = True
    
    #glEnable(GL_BLEND)
    glColor3f(0,0,0)
    glRasterPos2f(x,y)
    for ch in text :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )
    
    
    if not blending :
        glDisable(GL_BLEND)

# The main drawing function.
def DrawGLScene():
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()					# Reset The View
        
        # Move Left 1.5 units and into the screen 6.0 units.
    glTranslatef(0.0, 0.0, -90.0)
        
        # Draw a triangle
    glBegin(GL_POLYGON)                 # Start drawing a polygon
    glColor3f(0.0,0.0,0.5)
    i = 0
    if size == 0:
        glVertex3f(0.0, 0.0, 0.0)
    else:
        while i < size:
            glVertex3f(matrix[i][0], matrix[i][1], 0.0)           # Top
            i = i+1
    
    glEnd()                             # We are done with the polygon

    glBegin(GL_POLYGON)                 # Start drawing a polygon
    glColor3f(0.0,0.0,200.0)
    i = 0
    if size == 0:
        glVertex3f(0.0, 0.0, 0.0)
    else:
        while i < size:
            glVertex3f(prevmatrix[i][0], prevmatrix[i][1], 0.0)           # Top
            i = i+1
    
    glEnd()

    x = -500
    while x <= 500 :
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(x,-500,0)
        glVertex3f(x,500,0)
        glEnd()
        if x == 0 :
            x = -0.9
            while x < 1 :
                glBegin(GL_LINE_LOOP)
                glColor3f(0.0,0.0,0.0)
                glVertex3f(x,-500,0)
                glVertex3f(x,500,0)
                glEnd()
                x = x+0.1
            x = 25
        else :
            x = x+25
    
    
    y = -500
    while y <= 500 :
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(-500,y,0)
        glVertex3f(500,y,0)
        glEnd()
        if y == 0 :
            y = -0.9
            while y < 1 :
                glBegin(GL_LINE_LOOP)
                glColor3f(0.0,0.0,0.0)
                glVertex3f(-500,y,0)
                glVertex3f(500,y,0)
                glEnd()
                y = y+0.1
            y = 25
        else :
            y = y+25

    glut_print( 0 , 0 , GLUT_BITMAP_8_BY_13, "0" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 75 , 0 , GLUT_BITMAP_8_BY_13, "100" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 175 , 0 , GLUT_BITMAP_8_BY_13, "200" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 275 , 0 , GLUT_BITMAP_8_BY_13, "300" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 375 , 0 , GLUT_BITMAP_8_BY_13, "400" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 475 , 5 , GLUT_BITMAP_8_BY_13, "x" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( -125 , 0 , GLUT_BITMAP_8_BY_13, "-100" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( -225 , 0 , GLUT_BITMAP_8_BY_13, "-200" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( -325 , 0 , GLUT_BITMAP_8_BY_13, "-300" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( -425 , 0 , GLUT_BITMAP_8_BY_13, "-400" , 0.0 , 0.0 , 0.0 , 0.0 )

    glut_print( 0 , 75 , GLUT_BITMAP_8_BY_13, "100" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 0 , 175 , GLUT_BITMAP_8_BY_13, "200" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 0 , 275 , GLUT_BITMAP_8_BY_13, "300" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 0 , 375 , GLUT_BITMAP_8_BY_13, "400" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 0 , 475 , GLUT_BITMAP_8_BY_13, "y" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 0 , -125 , GLUT_BITMAP_8_BY_13, "-100" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 0 , -225 , GLUT_BITMAP_8_BY_13, "-200" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 0 , -325 , GLUT_BITMAP_8_BY_13, "-300" , 0.0 , 0.0 , 0.0 , 0.0 )
    glut_print( 0 , -425 , GLUT_BITMAP_8_BY_13, "-400" , 0.0 , 0.0 , 0.0 , 0.0 )

        # Move Right 3.0 units.
    glTranslatef(3.0, 0.0, 0.0)
    
        #  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()

def updatePrevMatrix():
    i = 0
    while i < size:
        prevmatrix[i][0] = matrix[i][0]
        prevmatrix[i][1] = matrix[i][1]
        i = i+1

def animate():
    j = 0
    dx = []
    dy = []
    dxfrac = []
    dyfrac = []
    i = 0
    while i < size:
        dx.append(tempmatrix[i][0] - matrix[i][0])
        dy.append(tempmatrix[i][1] - matrix[i][1])
        dxfrac.append((dx[i])/100)
        dyfrac.append((dy[i])/100)
        i = i+1
    i = 0
    while j < 100:
        time.sleep(0.01)
        while i < size:
            matrix[i][0] = matrix[i][0] + dxfrac[i]
            matrix[i][1] = matrix[i][1] + dyfrac[i]
            i = i+1
        i = 0
        j = j+1

def translate(dx, dy):
    updatePrevMatrix()
    i = 0
    while i < size:
        tempmatrix[i][0] = matrix[i][0] + dx
        tempmatrix[i][1] = matrix[i][1] + dy
        i = i+1
    animate()

def translate1(dx, dy):
    i = 0
    while i < size:
        matrix[i][0] = matrix[i][0] + dx
        matrix[i][1] = matrix[i][1] + dy
        i = i+1

def dilate(k):
    updatePrevMatrix()
    i = 0
    while i < size:
        tempmatrix[i][0] = matrix[i][0] * k
        tempmatrix[i][1] = matrix[i][1] * k
        i = i+1
    animate()

def rotate1(deg, p1, p2):
    translate1(-p1, -p2)
    i = 0
    while i < size:
        temp1 = matrix[i][0]
        temp2 = matrix[i][1]
        matrix[i][0] = temp1 * math.cos(math.radians(deg)) - temp2 * math.sin(math.radians(deg))
        matrix[i][1] = temp1 * math.sin(math.radians(deg)) + temp2 * math.cos(math.radians(deg))
        i = i+1
    translate1(p1, p2)

def rotate(deg, p1, p2):
    updatePrevMatrix()
    degfrac = deg/100
    j = 0
    while j < 100:
        time.sleep(0.01)
        rotate1(degfrac, p1, p2)
        j = j+1

def reflect1(v1, v2):
    translate1(-v1, -v2)
    i = 0
    while i < size:
        matrix[i][0] = (-1)*(matrix[i][0])
        matrix[i][1] = (-1)*(matrix[i][1])
        i = i+1
    translate1(v1, v2)

def reflect(v1, v2):
    updatePrevMatrix()
    i = 0
    while i < size:
        tempmatrix[i][0] = matrix[i][0]
        tempmatrix[i][1] = matrix[i][1]
        i = i+1
    reflect1(v1, v2)
    animate()

def shear(param, degree):
    updatePrevMatrix()
    i = 0
    while i < size:
        if param == "x":
            tempmatrix[i][0] = matrix[i][0] + matrix[i][1] * degree
            tempmatrix[i][1] = matrix[i][1]
        elif param == "y":
            tempmatrix[i][0] = matrix[i][0]
            tempmatrix[i][1] = matrix[i][1] + matrix[i][0] * degree
        i = i+1
    animate()

def stretch(param, degree):
    updatePrevMatrix()
    i = 0
    while i < size:
        if param == "x":
            tempmatrix[i][0] = matrix[i][0] * degree
            tempmatrix[i][1] = matrix[i][1]
        elif param == "y":
            tempmatrix[i][0] = matrix[i][0]
            tempmatrix[i][1] = matrix[i][1] * degree
        i = i+1
    animate()


def custom(a, b, c, d):
    updatePrevMatrix()
    i = 0
    while i < size:
        tempmatrix[i][0] = a * matrix[i][0] + b * matrix[i][1]
        tempmatrix[i][1] = c * matrix[i][0] + d * matrix[i][1]
        i = i+1
    animate()

def reset():
    i = 0
    while i < size:
        tempmatrix[i][0] = initmatrix[i][0]
        tempmatrix[i][1] = initmatrix[i][1]
        i = i+1
    j = 0
    dx = []
    dxprev = []
    dy = []
    dyprev = []
    dxfrac = []
    dxprevfrac = []
    dyfrac = []
    dyprevfrac = []
    i = 0
    while i < size:
        dx.append(tempmatrix[i][0] - matrix[i][0])
        dy.append(tempmatrix[i][1] - matrix[i][1])
        dxfrac.append(dx[i]/100)
        dyfrac.append(dy[i]/100)
        dxprev.append(tempmatrix[i][0] - prevmatrix[i][0])
        dyprev.append(tempmatrix[i][1] - prevmatrix[i][1])
        dxprevfrac.append(dxprev[i]/100)
        dyprevfrac.append(dyprev[i]/100)
        i = i+1
    while j < 100:
        time.sleep(0.01)
        i = 0
        while i < size:
            matrix[i][0] = matrix[i][0] + dxfrac[i]
            matrix[i][1] = matrix[i][1] + dyfrac[i]
            prevmatrix[i][0] = prevmatrix[i][0] + dxprevfrac[i]
            prevmatrix[i][1] = prevmatrix[i][1] + dyprevfrac[i]
            i = i+1
        j = j+1

def take():
    global window
    global matrix
    global size
    global P
    global initmatrix
    global tempmatrix
    global prevmatrix
    
    size = 0
    P = []
    matrix = []
    initmatrix = []
    tempmatrix = []
    prevmatrix = []
    size = int (input("Masukkan size polygon: "))
    i = 1
    while i <= size :
        rawpoint = raw_input("Masukkan titik (format: x,y): ")
        point = rawpoint.split(",")
        ordinat = point[0]
        absis = point[1]
        # print "Masukan x",i, ": "
        # ordinat = input()
        # print "Masukan y",i, ": "
        # absis = input()
        del P[:]
        P.append(float(ordinat))
        P.append(float(absis))
        i = i+1
        matrix.append(list(P))
        initmatrix.append(list(P))
        tempmatrix.append(list(P))
        prevmatrix.append(list(P))




def gl():
    Thread(target=main).start()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Objek Geometri")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(500, 500)
    glutMainLoop()

def main():
    masukan = raw_input("Masukan perintah: ")
    perintah = masukan.split(" ")
    while perintah[0] != "exit":
        if ((perintah[0] == "translate") and (len(perintah) == 3)):
            translate(float(perintah[1]), float(perintah[2]))
            print "Translasi berhasil"
        elif ((perintah[0] == "dilate") and (len(perintah) == 2)):
            dilate(float(perintah[1]))
            print "Dilatasi berhasil"
        elif ((perintah[0] == "rotate") and (len(perintah) == 4)):
            rotate(float(perintah[1]), float(perintah[2]), float(perintah[3]))
            print "Rotasi berhasil"
        elif ((perintah[0] == "reflect") and (len(perintah) == 3)):
            reflect(float(perintah[1]), float(perintah[2]))
            print "Refleksi berhasil"
        elif ((perintah[0] == "shear") and (len(perintah) == 3)):
            shear(perintah[1], float(perintah[2]))
            print "Shear berhasil"
        elif ((perintah[0] == "stretch") and (len(perintah) == 3)):
            stretch(perintah[1], float(perintah[2]))
            print "Stretch berhasil"
        elif ((perintah[0] == "custom") and (len(perintah) == 5)):
            custom(float(perintah[1]), float(perintah[2]), float(perintah[3]), float(perintah[4]))
            print "Custom transformation berhasil"
        elif (perintah[0] == "reset"):
            reset()
            print "Reset berhasil"
        masukan = raw_input("Masukkan perintah: ")
        perintah = masukan.split(" ")
    glutHideWindow()

take()
thread.start_new_thread(gl(), ())
quit()

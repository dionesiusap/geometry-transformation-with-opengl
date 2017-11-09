# Filename    : main.py
# Author      : Jason Wiguna, Dionesius Agung
# Version     : 2017/11/04
# Description : 2D geometry transformation simulator using OpenGL

from transformgl import *

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
    masukan = raw_input("Masukkan perintah: ")
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
        elif ((perintah[0] == "multiple") and (len(perintah) == 2)):
            n = 0
            m = perintah[1]
            commandlist = []
            for n in range (0,int(m)):
                commandinput = raw_input()
                commandlist.append(commandinput)
            for n in range (0,int(m)):
                command = commandlist[n].split(" ")
                if ((command[0] == "translate") and (len(command) == 3)):
                    translate(float(command[1]), float(command[2]))
                    print "Translasi berhasil"
                elif ((command[0] == "dilate") and (len(command) == 2)):
                    dilate(float(command[1]))
                    print "Dilatasi berhasil"
                elif ((command[0] == "rotate") and (len(command) == 4)):
                    rotate(float(command[1]), float(command[2]), float(command[3]))
                    print "Rotasi berhasil"
                elif ((command[0] == "reflect") and (len(command) == 3)):
                    reflect(float(command[1]), float(command[2]))
                    print "Refleksi berhasil"
                elif ((command[0] == "shear") and (len(command) == 3)):
                    shear(command[1], float(command[2]))
                    print "Shear berhasil"
                elif ((command[0] == "stretch") and (len(command) == 3)):
                    stretch(command[1], float(command[2]))
                    print "Stretch berhasil"
                elif ((command[0] == "custom") and (len(command) == 5)):
                    custom(float(command[1]), float(command[2]), float(command[3]), float(command[4]))
                    print "Custom transformation berhasil"
                elif (command[0] == "reset"):
                    reset()
                    print "Reset berhasil" 
        elif (perintah[0] == "reset"):
            reset()
            print "Reset berhasil"
        masukan = raw_input("Masukkan perintah: ")
        perintah = masukan.split(" ")
    glutHideWindow()
    exit()

take()
thread.start_new_thread(gl(), ())
exit()

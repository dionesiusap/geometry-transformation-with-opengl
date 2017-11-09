# Filename    : transform.py
# Author      : Jason Wiguna, Dionesius Agung
# Version     : 2017/11/09
# Description : Library for geometry transformation

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
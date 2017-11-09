# Geometry Transformation using OpenGL
Performs and simulates 2 dimensional transformation with OpenGL on Python.

## Getting Started
In terminal type in the following command:
```
python main.py
```
The program will show you:
```
Masukkan size polygon:
```

## Using the Program
This is how to use the program

### Program setup
Setup example:
```
Masukkan size polygon: 3
Masukkan titik (format: x,y): 0,0
Masukkan titik (format: x,y): 300,0
Masukkan titik (format: x,y): 0,300
```

### Commands
List of basic commands:
```
translate dx dy
```
Translates object x-wise for dx units and y-wise for dy units.

```
dilate k
```
Dilates object k times.

```
rotate deg a b
```
Rotates object deg degrees with a,b as the axis of rotation.

```
reflect param
```
Reflects object depends on the parameter.
Legal parameters: x, y, y=x, y=-x

```
shear param k
```
Shears object param-wise (x or y) k times.

```
stretch param k
```
Stretches object param-wise (x or y) k times.

```
custom a b c d
```
Transforms object with a custom matrix
a c
b d

```
reset
```
Resets object to its initial condition.

```
exit
```
Exits from program.

If you want to perform multiple translations at once, you can type in
```
multiple n
command param
command param
command param
...
command param // nth input
```

## Program I/O Example
An example of program I/O.
```
Masukkan size polygon: 3
Masukkan titik (format: x,y): 100,100
Masukkan titik (format: x,y): 250,250
Masukkan titik (format: x,y): 300,100
Masukkan perintah: translate 200 100
Translasi berhasil
Masukkan perintah: dilate 1.5
Dilatasi berhasil
Masukkan perintah: rotate 90 0 0
Rotasi berhasil
Masukkan perintah: reset
Reset berhasil

```

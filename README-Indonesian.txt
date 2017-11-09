# Transformasi Geometri Menggunakan API OpenGL
Menampilkan sumulasi transformasi linear 2 dimensi dengan API OpenGL dengan bahasa Python.

## Memulai
Pada terminal ketik perintah berikut:
```
python geometry-transform.py
```
Lalu program akan menampilkan:
```
Masukkan size polygon:
```

## Menggunakan Program
Berikut ini adalah cara menggunakan program.

### Setup program
Contoh setup:
```
Masukkan size polygon: 3
Masukkan titik (format: x,y): 0,0
Masukkan titik (format: x,y): 300,0
Masukkan titik (format: x,y): 0,300
```

### Perintah
Daftar perintah-perintah dasar:
```
translate dx dy
```
Translasi objek searah x sejauh dx dan searah y sejauh dy.

```
dilate k
```
Dilatasi objek k kali.

```
rotate deg a b
```
Rotasi objek deg derajat dengan poros a,b.

```
reflect param
```
Refleksi objek berdasarkan parameter.
Legal parameters: x, y, y=x, y=-x

```
shear param k
```
Menggusur objek searah param k kali.

```
stretch param k
```
Meregangkan objek searah param k kali.

```
custom a b c d
```
Transformasi objek dengan matrix bebas
a c
b d

```
reset
```
Resets objek ke posisi awal.

```
exit
```
Keluar program.

Jika ingin melakukan beberapa transformasi sekaligus gunakan multiple.
```
multiple n
command param
command param
command param
...
command param // nth input
```

## Contoh I/O Program
Contoh I/O Program.
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

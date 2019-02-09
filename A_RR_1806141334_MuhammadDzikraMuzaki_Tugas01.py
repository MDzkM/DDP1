# Program "Colorful Chessboard and Flower".

# Mengimport module.
import turtle
import random

def tclr_Rand():
    """Fungsi untuk memanggil warna turtle secara random."""

    # Mengacak nilai R, G, dan B.
    turtle.color(random.random(), random.random(), random.random())

def draw_Chessboard(rows, pixels):
    """Fungsi untuk menggambar Chessboard menggunakan turtle."""
    x = -((rows * pixels) / 2)              # Menentukan posisi awal x.
    y = 100                                 # Koordinat awal y.

    turtle.up()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.showturtle()

    for baris in range(rows):               # Looping untuk baris.
        turtle.down()

        for kolom in range(rows):           # Looping untuk kolom.
            tclr_Rand()
            turtle.begin_fill()

            for sisi in range(4):           # Looping untuk menggambar kotak.
                turtle.fd(pixels)
                turtle.right(90)

            turtle.end_fill()
            turtle.up()
            turtle.fd(pixels)
            turtle.down()

        turtle.up()
        y -= pixels
        turtle.goto(x, y)

    turtle.hideturtle()

def draw_Flower(petals, side_Length):
    """Fungsi untuk menggambar Flower menggunakan turtle."""
    radius = side_Length / 2                # Menentukan radius Flower.
    y = 360 / petals                        # Menentukan jarak tiap petals.

    turtle.up()
    turtle.setheading(-60)
    turtle.goto(0, 125 + radius)
    turtle.showturtle()

    for jml in range(petals):               # Looping untuk banyak petals.
        tclr_Rand()
        turtle.down()

        for arc in range (2):               # Looping untuk petals.
            turtle.circle(radius, -60)
            turtle.right(120)

        turtle.right(y)

    turtle.hideturtle()

def print_Sentence(rows, petals, side_Length):
    """Fungsi untuk menuliskan jumlah kotak pada Chessboard
    dan Petals pada Flower"""
    turtle.up()
    turtle.goto(0, 50 - side_Length)
    turtle.down()
    tclr_Rand()

    # Menuliskan Sentence.
    turtle.write("Colorful Chessboard of {} Squares and Flower of {} Petals"
    .format(rows * rows, petals), False, "Center", ("Arial", 18, "bold"))

def main():
    turtle.hideturtle()
    turtle.shape('turtle')
    turtle.speed(0)

    # Meminta input untuk rows, pixels, dan petals.
    rows = int(turtle.numinput("Colorful Chessboard and Flower",
    "Enter the number of rows: ", None, 2, 25))

    pixels = turtle.numinput("Colorful Chessboard and Flower",
    "Enter the square size (pixels): ", None, 1, int(300 / rows))

    petals = int(turtle.numinput("Colorful Chessboard and Flower",
    "Enter the number of petals of the flower: ", None, 2, 360))

    side_Length = rows * pixels             # Menghitung panjang sisi.

    # Memanggil fungsi menggambar Flower dan Chessboard.
    # Dan menulis Sentence.
    draw_Flower(petals, side_Length)
    draw_Chessboard(rows, pixels)
    print_Sentence(rows, petals, side_Length)

    turtle.exitonclick()

if __name__ == "__main__":                  # Mencari fungsi main.
    main()

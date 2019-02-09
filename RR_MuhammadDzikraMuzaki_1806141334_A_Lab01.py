import turtle

#menset koordinat pen ke (-200, 150)
turtle.penup()
turtle.goto(-200, 150)

#mengubah warna pen menjadi merah
turtle.pendown()
turtle.color('red')

#membuat kotak merah
turtle.begin_fill()
turtle.forward(200)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()#selesai membuat kotak merah

#menset koordinat pen ke (0,150)
turtle.penup()
turtle.goto(0, 150)
turtle.right(90)

#mengubah warna pen menjadi biru
turtle.pendown()
turtle.color('blue')

#membuat kotak biru
turtle.begin_fill()
turtle.forward(200)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()#selesai membuat kotak biru

#menset koordinat pen ke (-175,125)
turtle.penup()
turtle.goto(-175, 125)
turtle.right(90)

#mengubah warna menjadi biru
turtle.pendown()
turtle.color('blue')

#membuat huruf C
turtle.begin_fill()
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(250)
turtle.end_fill()#selesai membuat huruf C

#menset koordinat pen ke (25, 125)
turtle.penup()
turtle.goto(25, 125)
turtle.right(90)

#mengubah warna pen menjadi merah
turtle.pendown()
turtle.color('red')

#membuat huruf S
turtle.begin_fill()
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()#selesai membuat huruf S


#menghilangkan cursor pen turtle
turtle.hideturtle()

#menutup window turtle saat di klik
turtle.exitonclick()

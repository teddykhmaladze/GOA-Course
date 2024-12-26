from turtle import *
speed (30)

#we want to paint a hause

width(7)

begin_fill()

color("purple")
forward(200)
left(90)

forward(200)#step 1:drow a square
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#end of square

#drawing a door

forward(70)

begin_fill()

color("yellow")
left(90)
forward(100)

right(90)
forward(50)
right(90)

forward(100)

end_fill()

penup()
goto(200, 200)
pendown()

#roof 
begin_fill()
color("red")
right(150)

forward(165)

left(110)
forward(180)
end_fill()

#vindou

penup()
goto(20, 180)
pendown()

left(40)

begin_fill()

color("blue")

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)

end_fill()

penup()
goto(180, 180)
pendown()

begin_fill()

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)

end_fill()

exitonclick()
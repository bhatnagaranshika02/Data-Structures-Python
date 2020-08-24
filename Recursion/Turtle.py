import turtle

myT = turtle.Turtle()

mywin=turtle.Screen()
def draw(myT,linelen):
    if linelen>0:
        myT.forward(linelen)
        myT.right(90)
        draw(myT,linelen=5)

draw(myT,100)
mywin.exitonclick()

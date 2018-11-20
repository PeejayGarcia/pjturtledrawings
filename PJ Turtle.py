import turtle
def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)        
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")    
    pj = turtle.Turtle()
    pj.color("hotpink")
    pj.speed(5)
    pj.pensize(2.5)   
    size = 20
    x = -10
    y = -10    
    for i in range(5):
        draw_square(pj, size)
        pj.penup()
        pj.goto(x,y)
        pj.pendown()
        size = size + 20
        x = x - 10
        y = y - 10        
    wn.exitonclick() 
if __name__ == "__main__":
    main()

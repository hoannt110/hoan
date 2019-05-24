from turtle import*
speed(5)
color("green","yellow")
def square():
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()    
    return

def triangle():
    begin_fill()
    for i in range(3):
        forward(100)
        left(120)
    end_fill()    
    return


print("Enter 1 if you want draw a square")
print("Enter 2 if you want draw a triangle")
print("Enter 3 if you want draw a circle")
a = int(input("Enter a number"))
if a == 1:
    square()
if a == 2:
    triangle()
if a == 3:
    begin_fill()
    circle(50)
    end_fill() 
else:
    print("Please enter a number from 1 to 3")
mainloop()
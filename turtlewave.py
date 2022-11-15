from PIL import Image
import sys
import tkinter




def convert(filename:str,outputname:str):
    im = Image.open(filename).convert('RGBA')
    pix= im.load()
    width, height = im.size
    output="""import turtle
turtle.speed(0)
turtle.colormode(255)
turtle.hideturtle()
turtle.tracer(0.0)
def drawpixel(x, y, color, pixelsize = 0.1 ):
    turtle.penup()
    turtle.setpos(x*pixelsize,y*pixelsize)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)
    turtle.end_fill()
    """

    for i in range(1,width):
        for j in range(1,height):
            if type(pix[i,j])==int:
                r,g,b=(0,0,0)
            else :
                r,g,b,a=pix[i,j]
            output+="\ndrawpixel(%d,%d,(%d,%d,%d),%d)"%(i,-j,r,g,b,1)
    output+="\nturtle.update()\nturtle.mainloop()"

    f = open(outputname, "w")
    f.write(output)


if __name__=="__main__":
    try:
        convert(sys.argv[1],sys.argv[2])
    except:
        print("error was occured")
    
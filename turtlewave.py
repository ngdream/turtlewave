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
turtle.tracer(0,0)
turtle.hideturtle()
def drawpixel(x, y, color):

    turtle.setpos(x,y)
    turtle.color(color)
    turtle.forward(1)
    """



    for i in range(1,width):
        for j in range(1,height):
            if type(pix[i,j])==int:
                r,g,b,a=(0,0,0,0)
            else :
                r,g,b,a=pix[i,j]
            output+="\ndrawpixel(%d,%d,(%d,%d,%d))"%(i,-j,r,g,b)
    output+="\nturtle.update()\nturtle.mainloop()"

    f = open(outputname, "w")
    f.write(output)


if __name__=="__main__":
    try:
        convert(sys.argv[1],sys.argv[2])
    except:
        print("error was occured")
    
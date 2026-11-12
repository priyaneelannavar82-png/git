from OpenGl.GL import*
from OpenGl.GLUT import*
from OpenGL.GLU import*

xmin,ymin = 100,100
xmax,ymax = 300,300

x1,y1 = 50,50
x2,y2 = 350,350

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def computeCode(x,y):
    code = INSDE
    if x < min:
        code |= LEFT
    elif x > xmax:
        code |=RIGHT
    if y < ymin:
        code |= BOTOM
    elif y > ymax:
        code |= TOP
    return code

def cohenSutherlandClip():
    global x1,y1,x2,y2

    code1 = computeCode(x1,y1)
    code2 = computeCode(x2,y2)

    accept = False

    while True:
        if code == 0 and code2 ==0:
            accept = True
            break
        elif (code1 & code2) !=0:
            break
        else:
            x,y = 0.0,0.0

            code_out = code if code != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1)*(ymax - y1)/(y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1)*(ymin - y1)/(y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1)*(xmax - x1)/(x2 -x1)
                x = max
            elif code_out & LEFT:
                y = y1 +(y2 - y1)*(xmax - x1)/(x2 - x1)
                x = xmin

            if code_out == code1:
                x1,y1 = x,y
                code1 = computCode(x1,y1)
            else:
                x2,y2 = x,y
                code2 = computCode(x2,y2)

            if accept:
                glColor3f(0.0,1.0,0.0)
                glBegin(GL_LINES)
                glVertex2f(x1,y1)
                glVertex2f(x2,y2)
                glEnd()

            def display():
                glClear(GL_COLOR_BUFFER_BIT)

                glCoor3f(1.0,1.0,1.0)
                glBegin(GL_LINE_LOOP)
                glVertex2f(xmin,ymin)
                glVertex2f(xmax,ymin)
                glVertex2f(xmax,ymax)
                glVertex2f(xmin,ymax)
                glEnd()

                glColor3f(1.0,0.0,0.0)
                glBegin(GL_LINES)
                glVertex2f(50,50)
                glVertex2f(350,350)
                glEnd()

                cohenSutherlandClip()

                glFlush()

                def init():
                    glClearClor(0,0,0,1)
                    glOrtho2D(0,500,0,500)

                    def main():
                        glutInit()
                        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
                        glutInitWindowSize(500,500)
                        glutCreateWindow(b"Cohen-Sutherland Line Clipping")

                        init()
                        glutDisplayFunc(display)
                        glutMainLoop()

                        main()

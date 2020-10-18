import turtle, random, sys, time

#ix=int(input(''))
#iy=int(input(''))


# irregular 
# python fractalpattern.py <shape> <color> <dotsize> <speed> <position of dot>

if len(sys.argv) != 5:
     print("Usage: python fractalpattern.py <dotsize> <speed> <position of dot>")
     sys.exit()

d=int(sys.argv[1])
s=int(sys.argv[2])
n=int(sys.argv[3])
z=float(sys.argv[4])
tco=[-300,-300,0,300,300,-300]
#tco=[-100,100,100,100,100,-100,-100,-100]

x1=int(tco[0])
y1=int(tco[1])
x2=int(tco[2])
y2=int(tco[3])
x3=int(tco[4])
y3=int(tco[5])
'''x4=int(tco[6])
y4=int(tco[7])

ix=random.randint(x1,x2)
iy=random.randint(y4,y1)'''

#ix=5
#iy=8

pen=turtle.Turtle()
pen.hideturtle()

def triangle():
     pen.width(10)
     pen.penup()
     pen.goto(x1,y1)
     pen.pendown()
     pen.goto(x2,y2)
     pen.goto(x3,y3)
     pen.goto(x1,y1)
     pen.penup()
def quad():
     pen.width(10)
     pen.penup()
     pen.goto(x1,y1)
     pen.pendown()
     pen.goto(x2,y2)
     pen.goto(x3,y3)
     pen.goto(x4,y4)
     pen.goto(x1,y1)
     pen.penup()

pen.speed(s)
triangle()
#quad()
#cordin=[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
cordin=[(x1,y1),(x2,y2),(x3,y3)]
#pen.goto(ix,iy)
#pxy=4
dx12=x2-x1
dx23=x3-x2
dy=y2-y1
sl1=dy/dx12
sl2=dy/dx23


x=random.randint(x1,x3)
if x<x2:
     y=random.randint(y1,int(y1+sl1*(x-x1)))
else:
     y=random.randint(y1,int(y1+sl2*(x3-x)))
     
     



'''rs=random.randint(0,100)
for i in range(rs):
     xy=cordin[random.randint(0,2)]
     tx=xy[0]
     ty=xy[1]
     tx=int(tx)
     ty=int(ty)
     pen.penup()
     nx=(tx+2*x)/3
     ny=(ty+2*y)/3
     pen.goto(nx,ny)
     x=nx
     y=ny
     
pen.dot(d)'''



while(True):
     xy=cordin[random.randint(0,2)]
     '''while(True):
          if xy==pxy :
               xy=cordin[random.randint(0,3)]
          else:
               break;'''

     tx=xy[0]
     ty=xy[1]
     tx=int(tx)
     ty=int(ty)
     pen.penup()
     pen.goto(((tx+(n-1)*x)/n),((ty+(n-1)*y)/n))
     
     pen.pendown()
     pen.dot(d)
     x=(tx+(z-1)*x)/z
     y=(ty+(z-1)*y)/z
     #pxy=xy
     




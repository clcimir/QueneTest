import turtle as t
class desk:
    
    def __init__(self, SIZE):
        self.SIZE = SIZE
        
    def set_color(self,f):
        if f%2==0:
         t.color('black', 'white')
        else:
           t.color('black', 'black')

    def rectangle(self,x,y,w,h,f):
        t.penup()
        t.goto(x,y)
        t.pendown()
        self.set_color(f)
        t.begin_fill()
        for i in range(2):
                    t.forward(w)
                    t.left(90)
                    t.forward(h)
                    t.left(90)
        t.end_fill()

    def polyline(self,x,y,p,f):
        t.penup()
        t.goto(x+p[0][0]*self.SIZE, y+p[0][1]*self.SIZE)
        t.pendown()
        self.set_color(f)
        t.begin_fill()
        for q in p:
                xq=q[0]*self.SIZE+x
                yq=q[1]*self.SIZE+y
                t.goto(xq,yq)
        t.end_fill()       

        
    def queen(self,x,y,f):
        self.rectangle(x+self.SIZE*0.1,y+self.SIZE*0.1,self.SIZE*0.8,self.SIZE*0.1,f)
        self.rectangle(x+self.SIZE*0.15,y+self.SIZE*0.2,self.SIZE*0.7,self.SIZE*0.1,f)
        p=((0.15,0.3),(0.1,0.4), (0.9,0.4),(0.85,0.3))
        self.polyline(x,y,p,f)
        p=((0.1,0.4),(0.3,0.6),(0.3,0.4),(0.5,0.6),(0.7,0.4),(0.7,0.6),(0.9,0.4))
        self.polyline(x,y,p,f)

import turtle as t
import class_Queen as ccq
import chess_desk as cd
t.tracer(0)
SIZE=20
MainN=8

lib1=cd.desk(SIZE)
for j in range(MainN):
    for k in range(MainN):
        x=(j-(MainN/2))*SIZE
        y=(k-(MainN/2))*SIZE
        lib1.rectangle(x,y,SIZE,SIZE,j+k)

#Начало проверки ферзей

lib2=ccq.Queen(8)
p=lib2.getBoard()
for m in range(MainN):
    for i in range(MainN):
            x=(i-(MainN/2))*SIZE
            y=(m-(MainN/2))*SIZE
            if p[i][m]==1:
                lib1.queen(x,y,i+m+1)

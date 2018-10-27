import turtle as t
edge=5
t.setup(500,500,0,0)
t.penup()
for i in range(32):
    t.fd(edge)
    t.pendown()
    t.left(90)

    t.fd(edge)
    t.left(90)

    edge=edge+5
    
     

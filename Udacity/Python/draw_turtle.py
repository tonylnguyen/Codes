import turtle


class draw():

    def square():
        window = turtle.Screen()
        window.bgcolor('green')
        brad = turtle.Turtle()
        brad.shape('turtle')
        brad.speed(2)

        repeat = 0
        size = 50
        while repeat != 5:
            walk_time = 0
            while walk_time !=9:
                brad.forward(size)
                brad.left(80)
                walk_time = walk_time +1
            repeat = repeat + 1
            size = size + 10
        window.exitonclick()

    def circle():
        window = turtle.Screen()
        window.bgcolor('green')
        sally = turtle.Turtle()

        revolutions = 0
        add = 10
        while revolutions != 5:
            sally.circle(add)
            sally.right(10)
            add = add + 10
            revolutions = revolutions +1



    def star():
        window = turtle.Screen()
        window.bgcolor('white')
        link = turtle.Turtle()
        link.shape('classic')

        one_tri = 0
        while one_tri != 12:
            link.forward(100)
            link.left(150)
            one_tri = one_tri + 1

    def square_star():
        window = turtle.Screen()
        window.bgcolor('green')
        brad = turtle.Turtle()
        brad.shape('turtle')
        brad.speed(9)

        repeat = 0
        while repeat != 36:
            brad.left(10)
            walk_time = 0
            while walk_time !=4:
                brad.forward(100)
                brad.left(90)
                walk_time = walk_time +1
            repeat = repeat + 1
        brad.right(90)
        brad.fd(200)

        window.exitonclick()

    def name():
        window = turtle.Screen()
        window.bgcolor('green')
        brad = turtle.Turtle()
        brad.shape('turtle')
        brad.speed(1)

        #set T start point
        brad.up()
        brad.setx(-200)
        brad.sety(100)
        brad.pd()

        # T
        brad.forward(100)
        brad.back(50)
        brad.right(90)
        brad.forward(100)

        #set N start point
        brad.up()
        brad.setx(35)
        brad.pd()

        # N
        brad.back(100)
        brad.right(340)
        brad.forward(100)
        brad.left(160)
        brad.forward(100)


        window.exitonclick()

    def tri():
        window = turtle.Screen()
        window.bgcolor('green')
        brad = turtle.Turtle()
        brad.shape('turtle')
        brad.speed(4)

        forward = 50
        repeat = 0

        while repeat != 3:
            brad.up()
            brad.setx(0)
            brad.down()
            brad.left(120)
            brad.forward(forward)
            brad.left(120)
            brad.forward(forward)
            brad.left(120)
            brad.forward(forward + 50)
            brad.left(120)
            brad.forward(forward + 50)
            brad.left(120)
            brad.forward(forward)
            brad.left(120)
            brad.forward(forward)
            brad.right(120)
            brad.forward(forward)
            brad.circle(75)

            repeat = repeat + 1


        window.exitonclick()

draw.tri()

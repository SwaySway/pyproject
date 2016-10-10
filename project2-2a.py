import turtle

SINGLE_LENGTH = 5

ENCODINGS = [[1, 1, 0, 0, 0],   # encoding for '0'
         [0, 0, 0, 1, 1],   # encoding for '1'
         [0, 0, 1, 0, 1],   # encoding for '2'
         [0, 0, 1, 1, 0],   # encoding for '3'
         [0, 1, 0, 0, 1],   # encoding for '4'
         [0, 1, 0, 1, 0],   # encoding for '5'
         [0, 1, 1, 0, 0],   # encoding for '6'
         [1, 0, 0, 0, 1],   # encoding for '7'
         [1, 0, 0, 1, 0],   # encoding for '8'
         [1, 0, 1, 0, 0]    # encoding for '9'
        ]


def line(my_turtle, digit):
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()


def draw_barcode(my_turtle, zip):
    # start part
    line(my_turtle, 1)
    for str_digit in str(zip):
        digit = int(str_digit)
        for bar_bit in ENCODINGS[digit]:
            line(my_turtle, bar_bit)
    line(my_turtle, 1)

turtle.Turtle().pensize(2)
draw_barcode(turtle.Turtle(), 5555512372)
turtle.Turtle().getscreen().mainloop()
#
# draw_bar(my_turtle, 0)
# draw_bar(my_turtle, 0)
# draw_bar(my_turtle, 0)
# draw_bar(my_turtle, 1)
# draw_bar(my_turtle, 1)
#
# my_turtle.getscreen().mainloop()


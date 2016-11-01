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


def line(tut, digit):
    tut.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    tut.forward(length)
    tut.up()
    tut.backward(length)
    tut.right(90)
    tut.forward(10)
    tut.down()


def draw_barcode(tut, zip):
    line(tut, 1)
    for str_digit in str(zip):
        digit = int(str_digit)
        for bar_bit in ENCODINGS[digit]:
            line(tut, bar_bit)
    line(tut, 1)


def main():
    tut = turtle.Turtle()
    tut.speed(0)
    tut.pensize(3)
    tut.hideturtle()
    tut.penup()
    tut.setposition(-300, 0)
    tut.pendown()
    # 55555-1237
    draw_barcode(tut, 555551237)
    tut.penup()
    tut.setposition(-300, -50)
    tut.pendown()
    # 91768-1234
    draw_barcode(tut, 917681234)
    tut.penup()
    tut.setposition(-300, -100)
    tut.pendown()
    # 20500-0000
    draw_barcode(tut, 205000000)
    tut.getscreen().mainloop()


if __name__ == "__main__":
    main()





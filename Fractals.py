import turtle

def fractal(length, minimum, speed):

    turtle.speed(speed)

    # base case

    if length < minimum:
        return

    angle = 90
    length //= 2 # reduction

    for i in range(2):

        # draws upper right/lower left part of H, then inverses angle and then draws
        # upper left/lower right

        for j in range(2): 
            turtle.forward(length) # draws upper right leg of H
            turtle.left(angle)
            turtle.forward(length) # goes inward
            turtle.left(angle)
            fractal(length, minimum, speed) # recurses
            turtle.left(angle) 
            turtle.forward(length)
            turtle.right(angle)
            turtle.forward(length)

        angle = -angle

def menu():
    print("\n >> FRACTALS")

    l = input("\n >> Enter length of fractal: ")
    m = input("\n >> Enter minimum fractal length: ")
    s = input("\n >> Enter animation speed (0 to 10): ")

    try:
        fractal(int(l), int(m), int(s))
        return

    except TypeError:
        print("\n >> INVALID")

while True:
    menu()

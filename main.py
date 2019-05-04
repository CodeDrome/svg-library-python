import svg
import random

def main():

    """
    Try out the SVG class by calling function to
    create and save a few drawings.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| SVG Library   |")
    print("-----------------")

    draw_all_shapes()

    #i_want_to_believe()

    #mondrian()


def draw_all_shapes():

    """
    Quick demo of creating SVG object, using all methods,
    and saving the finished file.
    """

    s = svg.SVG()

    s.create(256, 192)

    s.fill("#A0A0FF")
    s.circle("#000080", 4, "#0000FF", 32, 64, 96)
    s.line("#000000", 2, 8, 8, 248, 184)
    s.rectangle(64, 64, 112, 32, "#00FF00", "#008000", 4, 4, 4)
    s.text(32, 16, "sans-serif", 16, "#000000", "#000000", "codedrome.com")
    s.ellipse(64, 160, 32, 16, "#FF0000", "#800000", 4)

    s.finalize()

    try:
        s.save("allshapes.svg")
    except IOError as ioe:
        print(ioe)

    print(s)


def i_want_to_believe():

    """
    A more complex drawing for X Files fans.
    """

    s = svg.SVG()

    s.create(512, 768)

    s.fill("#000010");

    for star in range(0, 512):

        x = random.randrange(0, 512)
        y = random.randrange(0, 768)

        s.rectangle(1, 1, x, y, "white", "white", 0, 0, 0)

    s.text(96, 712, "sans-serif", 32, "#FFFFFF", "#FFFFFF", "I WANT TO BELIEVE")

    s.circle("silver", 1, "rgba(0,0,0,0)", 28, 256, 384)

    s.ellipse(256, 374, 8, 14, "#808080", "#808080", 0)
    s.ellipse(252, 372, 3, 2, "#000000", "#000000", 0)
    s.ellipse(260, 372, 3, 2, "#000000", "#000000", 0)
    s.rectangle(1, 1, 251, 371, "white", "white", 0, 0, 0)
    s.rectangle(1, 1, 259, 371, "white", "white", 0, 0, 0)
    s.line("black", 2, 254, 378, 258, 378)

    s.line("silver", 2, 234, 416, 226, 432)
    s.line("silver", 2, 278, 416, 286, 432)
    s.ellipse(256, 400, 64, 16, "silver", "silver", 4)

    s.finalize()

    try:
        s.save("iwanttobelieve.svg")
    except IOError as ioe:
        print(ioe)


def mondrian():

    """
    Serious art here.
    """

    s = svg.SVG()

    s.create(512, 512)

    s.fill("white")

    s.rectangle(512, 512, 0, 0, "white", "black", 1, 0, 0)

    s.rectangle(256, 256, 64, 64, "red", "red", 0, 0, 0)
    s.rectangle(128, 128, 64, 320, "black", "black", 0, 0, 0)
    s.rectangle(64, 128, 0, 384, "orange", "orange", 0, 0, 0)
    s.rectangle(128, 192, 320, 0, "orange", "orange", 0, 0, 0)
    s.rectangle(128, 64, 320, 384, "navy", "navy", 0, 0, 0)
    s.rectangle(64, 128, 448, 384, "red", "red", 0, 0, 0)

    s.line("black", 8, 0, 64, 448, 64)
    s.line("black", 8, 64, 64, 64, 512)
    s.line("black", 8, 0, 192, 64, 192)
    s.line("black", 8, 0, 384, 512, 384)
    s.line("black", 8, 128, 0, 128, 64)
    s.line("black", 8, 320, 0, 320, 448)
    s.line("black", 8, 64, 320, 448, 320)
    s.line("black", 8, 320, 192, 448, 192)
    s.line("black", 8, 64, 448, 448, 448)
    s.line("black", 8, 448, 0, 448, 512)
    s.line("black", 8, 192, 320, 192, 512)
    s.line("black", 8, 384, 192, 384, 320)

    s.finalize()

    try:
        s.save("mondrian.svg")
    except IOError as ioe:
        print(ioe)


main()

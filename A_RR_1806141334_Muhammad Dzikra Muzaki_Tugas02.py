# Load the modules that will be used
import turtle
from random import*

# Set the turtle settings
canvas = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
pen.shape('turtle')
canvas.colormode(255)

def choose_file():
    '''Choose file as input using GUI.'''

    # load the local modules
    import tkinter
    from tkinter import filedialog

    # Ask for input file
    input_window = tkinter.Tk()
    input_window.withdraw()

    # Return chosen file
    return filedialog.askopenfilename()

def random_color():
    '''Set pen color randomly.'''

    pen.color(randint(0, 255), randint(0, 255), randint(0, 255))

def choose_color(red, green, blue):
    '''Set pen color according to input.'''

    pen.color(red, green, blue)

def draw_square(x_coordinate, y_coordinate, length):
    '''Draw a square according to input.'''

    # Set pen condition and coordinates
    pen.up()
    pen.goto(x_coordinate, y_coordinate)
    pen.setheading(0)
    pen.down()

    # Draw square
    for sides in range(4):
        pen.forward(length)
        pen.right(90)

def draw_circle(x_coordinate, y_coordinate, radius):
    '''Draw a circle according to input.'''

    # Set pen condition and coordinates
    pen.up()
    pen.goto(x_coordinate, y_coordinate)
    pen.setheading(0)
    pen.down()

    # Draw circle
    pen.circle(radius)

def draw_rectangle(x_coordinate, y_coordinate, length, width):
    '''Draw a rectangle according to input.'''

    # Set pen condition and coordinates
    pen.up()
    pen.goto(x_coordinate, y_coordinate)
    pen.setheading(0)
    pen.down()

    # Draw rectangle
    for sides in range(2):
        pen.forward(length)
        pen.right(90)
        pen.forward(width)
        pen.right(90)

def draw_flower(x_coordinate, y_coordinate, radius, petals):
    '''Draw a flower according to input.'''

    # Set pen condition and coordinates
    pen.up()
    pen.goto(x_coordinate, y_coordinate)
    pen.setheading(-60)
    pen.down()

    # Set angle spacing between petals
    angle = 360 / petals

    # Draw flower
    for petal in range(petals):

        # Draw petal
        for arc in range (2):
            pen.circle(radius, -60)
            pen.right(120)

        pen.right(angle)

def draw_chessboard(x_coordinate, y_coordinate, squares, pixels):
    '''Draw a chessboard according to input.'''

    # Set pen condition and coordinates
    pen.up()
    pen.setheading(0)

    # Create list for each square position
    square_position = [[0 for rows in range(squares)]
                       for columns in range(squares)]

    # Draw chessboard
    for rows in range(squares):

        # Draw square
        for columns in range(squares):

            # Randomizing the square position
            temp_x = randint(0, squares - 1)
            temp_y = randint(0, squares - 1)

            # Repeat randomizing if randomized square is already drawn
            while square_position[temp_x][temp_y] == 1:
                temp_x = randint(0, squares - 1)
                temp_y = randint(0, squares - 1)

            # Set pen condition and coordinates
            pen.goto(x_coordinate + ((temp_x + 1) * pixels),
                     y_coordinate + ((temp_y + 1) * pixels))
            pen.down()

            # Draw square
            for sides in range(4):
                pen.forward(pixels)
                pen.right(90)

            # Set square position to already drawn
            square_position[temp_x][temp_y] = 1

            pen.up()

def draw_polygon(x_coordinate, y_coordinate, length, total_sides):
    '''Draw a polygon according to input.'''

    # Set pen condition and coordinates
    pen.up()
    pen.goto(x_coordinate, y_coordinate)
    pen.setheading(0)
    pen.down()

    # Draw polygon
    for side in range(total_sides):
        pen.forward(length)
        pen.right(360/total_sides)

def title_set(file):
    '''Set the canvas title according to input.'''

    title_format = file.readline().lower().split()

    # Check if blank line
    if title_format == []:
        return False

    # Set student's id number
    npm = title_format[-1]

    title_name = ""

    # Set student's name
    for name in title_format[:-1]:
        name = name.capitalize()
        title_name += name + " "

    # Set title to student'a name and id number
    canvas.title("{}| {}".format(title_name, npm))

    if title_format[-1].isdecimal():
        return True

    else:
        return False

def error_check(command, num_input):
    '''Check input for errors.'''

    # List of valid commands
    list_of_commands = ['color', 'square', 'circle', 'rectangle', 'flower',
    'chessboard', 'polygon']

    # List of three parameters commands
    three_parameters_commands = ['color', 'square', 'circle']

    # List of four parameters commands
    four_parameters_commands = ['rectangle', 'flower', 'chessboard', 'polygon']

    # Check if the command is valid
    if command not in list_of_commands:
        return True

    # Check if the parameters are valid
    elif (command in three_parameters_commands) and (len(num_input) != 3):
        return True

    elif (command in four_parameters_commands) and (len(num_input) != 4):
        return True

    return False

def color_range_check(num_input):
    '''Check the color range input.'''

    for rgb in num_input:

        # Check if color is out of range
        if rgb < 0 or rgb > 255:

            # Randomize color if outside range
            random_color()

            return False

    return True

def run_command(file):
    '''Execute the commands inside the input file.'''

    # Dictionary for three parameters functions
    three_parameters_commands = {'color' : choose_color,
    'square' : draw_square, 'circle' : draw_circle}

    # Dictionary for three parameters functions
    four_parameters_commands = {'rectangle' : draw_rectangle,
    'flower' : draw_flower, 'chessboard' : draw_chessboard,
    'polygon' : draw_polygon}

    # Set the title
    if title_set(file) == False:
        print("Invalid input in line 1.")

    # Set the current line counter
    current_line = 1

    # Read the rest of the file
    lines = file.readlines()

    # Iterate for each line
    for line in lines:

        # Counts the current line
        current_line += 1

        # Make a list for the current line of input
        input = []
        input = line.lower().strip().split()

        # Check for blank space
        if input == []:
            print("Blank line in line {}.".format(current_line))
            continue

        command = input[0]
        num_input = []

        # Make a list for the command parameters
        for num in input[1:len(input)]:
            try:
                num_input.append(int(num))
            except:
                continue

        # Check input for errors
        if error_check(command, num_input) == True:

            # Print error message in the terminal
            print("Invalid input in line {}.".format(current_line))
            continue

        # Check color range if command is color
        if command == 'color':

            if color_range_check(num_input) == False:

                # Print error message in the terminal
                print("Color outside range in line {}.".format(current_line))
                continue

        # Execute command based on it's number of perimeters
        if command in three_parameters_commands:
            three_parameters_commands[command](num_input[0], num_input[1],
            num_input[2])

        else:
            four_parameters_commands[command](num_input[0], num_input[1],
            num_input[2], num_input[3])

    pen.hideturtle()
    canvas.exitonclick()
    file.close()

def main():
    try:

        # Ask for input file and open it
        file = open(choose_file())

        # Execute the commands inside the file
        run_command(file)

    except:

        # Print error message in the terminal
        print("Runtime Error.")

if __name__ == '__main__':
    main()

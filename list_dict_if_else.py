#   example of a dictionary that contain value pairs. note the curly brackets. 
author = {"name":"Ennil","color":"blue","shape":"diamond"}

#   a list of colors (homogenous set of elements) Note the square brackets.
colors = ["blue","green","red","purple","yellow"]

#   a LIST of DICTIONARIES ==> (nested loop). 
favorite_colors = [
                    {
                        "student": "Mary",
                        "color": "red"
                    },
                    {
                        "student": "John",
                        "color" : "blue"
                    }
                ]

#   entry point for end-user.   '__main__' is the name of the scope in which top-level code executes.
#   A module’s __name__ is set equal to '__main__' when read from standard input,
#   a script, or from an interactive prompt.

if __name__ == '__main__':
    print("++++++++++++++++++++++++")
    print("the author's name is {}.".format(author["name"]))
    print("His favorite color is {}.".format(author["color"]))
    print("")

    print("The current colors are:")
    for color in colors:
        print(color)
    print("")

    #   ask user for fav color and compare to author's color
    new_color = input("Whats is your favorite color? ")
    if new_color == author["color"]:
            print("You have the same favorite color as {}.".format(author["name"]))
            print("+++++++++++++++++++++++++")
            print("")

    #   see if this a new color for the list
    if new_color not in colors:
            print("That's a new color, adding it to the list!")
            colors.append(new_color)

            #   print update message about the new colors list
            message = ("There are now {} colors in the list.".format(len(colors)))
            message += "The color you added was {}.".format(colors[5])
            print(message)
    else:
        pass
    


gamercode = ["xXx", "xoxo", "gaming"]

name = input("What's ya name?: ")

def numbercheck(name):
    for character in name:
        if character.isdigit():
            return True
    return False

numbercheck(name)

if numbercheck(name) == True:
    print("We wont let a computer like Elon Musks son code for us.")
    quit()

if any(x in name for x in gamercode):
    print("Whats hanging my fellow gamer.")
    quit()

if name == "admin":
    print("nice try buddy.")
    quit()

if name == "Darth Plagueis the Wise":
    print("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It is not a story the Jedi would tell you. It is a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
    quit()

else:
    print("Welcome aboard," + name + ".")
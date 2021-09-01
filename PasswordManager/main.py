import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the state",prompt="what is the another state name")
print(answer_state)

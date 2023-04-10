import turtle
import pandas

screen = turtle.Screen()
screen.addshape("india_map_gif.gif")
turtle.shape("india_map_gif.gif")
turtle.setup(1200,800)

data = pandas.read_csv("State coord.csv")
state_list = data.State.to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 29:
    user_state = turtle.textinput(title=f"{len(guessed_states)}/29 guessed!", prompt="Enter a state name:").title()
    if user_state == "Exit":
        for i in state_list:
            if i not in guessed_states:
                missed_states.append(i)
        break

    if user_state in state_list:
        guessed_states.append(user_state)
        state_det = data[data.State == user_state]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_det.x), int(state_det.y))
        t.dot(5, "red")
        t.write(user_state)

data_dict = {
    "Missed states": missed_states
}

df = pandas.DataFrame(data_dict)
df.to_csv("Missed states.csv")


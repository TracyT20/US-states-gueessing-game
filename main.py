import turtle
import pandas
import string

#create GUI
screen=turtle.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer=turtle.Turtle()
state_data=pandas.read_csv("50_states.csv")
states=state_data.state.to_list()
TOTAL_STATES=50
right_guesses=[]
while len(right_guesses) <=50:
    answer=screen.textinput(f"{len(right_guesses)}/{TOTAL_STATES} states correct","What's another state name?").title()
    if answer=="Exit":
        break

    if answer in states:
        writer.hideturtle()
        row=state_data[state_data.state==answer]
        x_axis=int(row.iloc[0,1])
        y_axis=int(row.iloc[0,2])
        writer.penup()
        writer.goto(x_axis,y_axis)
        writer.write(f"{answer}",align="center",font=('Arial', 12, 'normal'))
        right_guesses.append(answer)
# if user types exit, populate the states to learn csv file with all the
#states the user did not guess
states_left=set(states)-set(right_guesses)
states_left_dict={"states_to_learn":list(states_left)}
df=pandas.DataFrame(states_left_dict)
df.to_csv("states_to_learn")

screen.exitonclick()
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
color = 'blue'
shape = 'triangle'
size = 3
score = 0

font_setup = ('Arial', 20, 'normal')

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

turtle_colors = ('red', 'yellow', 'green')
turtle_sizes = range(1, 10, 1)

#-----initialize turtle-----
triangle = trtl.Turtle()
triangle.shape(shape)
triangle.fillcolor(color)
triangle.shapesize(size)
triangle.pu()

score_writer = trtl.Turtle()
score_writer.pu()
score_writer.goto(0, 200)

counter =  trtl.Turtle()
counter.pu()
counter.goto(230, 250)

#-----game functions--------
def random_color():
  return rand.choice(turtle_colors)

def change_size():
  triangle.shapesize(rand.choice(turtle_sizes) / 2)

def triangle_clicked(x, y):
  global timer_up
  if (not timer_up):
    update_score()
    move_turtle()
  else:
    triangle.hideturtle()

def color_bg():
  triangle.fillcolor(random_color())
  triangle.stamp()
  triangle.fillcolor('blue')

def move_turtle():
  new_x = rand.randint(-200, 200)
  new_y = rand.randint(-150, 150)

  triangle.hideturtle()
  color_bg()
  change_size()
  triangle.goto(new_x, new_y)
  triangle.showturtle()

def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


#-----events----------------

triangle.onclick(triangle_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()

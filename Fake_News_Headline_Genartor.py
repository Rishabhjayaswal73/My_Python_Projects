#1--import the random module

import random
#2--Create Subjects

subjects = [
  "Rishabh Jayaswal",
  "Sharukh Khan",
  "Narendra Modi",
  "Rahul Gandhi",
  "Mahendra Sing Dhoni",
  "Virat Kohli",
  "A Group Of Dogs"
]

actions = [
  "Hits",
  "Dances With",
  "Eat ",
  "Went ",
  "Write ",
  "Declares War On",
  "Orders"
]

places_or_things = [
  "A Six",
  "Noora Fatehi",
  "The Mosquieto",
  "The History Of India",
  "Pakistan",
  "Mumbai"

]
#3-- start the headline generation

while True:
  subjects = random.choice(subjects)
  actions = random.choice(actions)
  places_or_things = random.choice(places_or_things)

  headline = f"Breaking News: {subjects} {actions} {places_or_things}"
  print("\n"+headline)

  user_input = input("\nDo you want to generate another headline (yes/no):").strip().lower()

  if user_input == "no":
    break
print("\n Thanks for using the fake news headline geneartor!")

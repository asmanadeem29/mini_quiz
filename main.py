print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

#if this is true then the code inside will run
if playing.lower() != "yes":
  quit()

#else the code inside will run
print("Okay! Let's play :)")
score = 0
 #Q1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print('correct!')
  score += 1
else:
  print("Incorrect!")
  #Q2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print('correct!')
  score += 1
else:
  print("Incorrect!")
 #Q3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print('correct!')
  score += 1
else:
  print("Incorrect!")
  #Q4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
  print('correct!')
  score += 1
else:
  print("Incorrect!")


print('You have completed the quiz!')
print('Your final score is: ', score)
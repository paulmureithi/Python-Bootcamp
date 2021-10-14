import art
import game_data
import random
from replit import clear

# print the game art

print(art.logo)

# create the questions for the users

a = random.choice(game_data.data)



question_a = f"{a['name']}, a {a['description']}, from {a['country']} "


score = 0
correct_answer = ''
flag = True

while flag==True:
  
  b = random.choice(game_data.data)
  question_b = f"{b['name']}, a {b['description']}, from {b['country']} "
  
  # testing my code
  # print(f"{a['follower_count']}")
  # print(f"{b['follower_count']}")


  if question_a != question_b:
    print(f"Compare A: {question_a}")
    print(art.vs)
    print(f"Against B: {question_b}")

  # get users's answer
  answer = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
  

  if a['follower_count'] > b['follower_count']:
    correct_answer = 'a'
  else:
    correct_answer = 'b'
    
  if answer == correct_answer:
    correct_answer = answer
    a['follower_count'] = b['follower_count']
    score += 1
    clear()
    question_a = question_b
    question_b = question_b
    print(art.logo)
    print(f"Congrats! You win, your score is: {score}")
    continue
    

  elif answer != correct_answer:
    if score > 1:
      score -= 1
    clear()
    print(art.logo)
    print(f"Sorry! You lose, your score is: {score}")
    break
  



  



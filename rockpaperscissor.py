rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
x=[rock,paper,scissors]
y = int(input("What do u choose?Type 0 for Rock,1 for paper or 2 for scissors. \n"))
if y>=0 and y<=2:
    print(x[y])


z=random.randint(0,2)
print("computer choice:")
print(x[z])
if y >= 3 or y < 0:
    print("invalid number")
elif y ==0 and z==2:
    print("you win")
elif z == 0 and y == 2:
    print("you lose")

elif z>y:
    print("you lose")
elif z < y:
    print("you win")
elif z==y:
    print("its draw")




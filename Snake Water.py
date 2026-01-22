import random
print("="*20)
print("lets Start The Game")
print("="*20)
print("The Rules are:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
choices=("Rock","Paper","Scissors")
comp=random.choice(choices)
# print(choice)
user=input("Enter your choice (Rock, Paper, Scissors): ")
User=user.capitalize()
print(f"Computer choice: {comp}\nYour choice: {User}")
if User==comp:
    print("It's a tie!")
elif User=="Rock" and comp=="Scissors":
    print("You won")
elif User=="Paper" and comp=="Rock":
    print("You won")
elif User=="Scissors" and comp=="Paper":
    print("You won")
else:
    print("You lose")

# points=0
# while True:
#     if User==comp:
#         print("You won")
#         points+=1
#         print("Your points are:", points)
#     elif User!=comp:
#         print("You lose")
#         print("Your total points are:", points)
        # break

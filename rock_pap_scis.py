user_1 = input("What is your name? ")
user_2 = input("and what is your name? ")

active = True
while active:
    u1 = input(f"{user_1.title()}, rock, paper or scissors? ")
    u2 = input(f"{user_2.title()}, rock, paper or scissors? ")
    u1_choice = u1.lower()
    u2_choice = u2.lower()
    if u1 == u2:
        print("Tie! Try again.")
        continue
    elif u1_choice == 'rock':
        if u2_choice == 'paper':
            print(f"Paper beats rock, {user_2.title()} wins!")
        else:
            print(f"Rock beats scissors, {user_1.title()} wins!")
    elif u1_choice == 'paper':
        if u2_choice == 'rock':
            print(f"Paper beats rock, {user_1.title()} wins!")
        else:
            print(f"Scissors beats paper, {user_2.title()} wins!")
    else:
        if u2_choice == 'rock':
            print(f"Rock beats scissors, {user_2.title()} wins!")
        else:
            print(f"Scissors beats paper, {user_1.title()} wins!")

    response = input("Would you like to play again (y/n)? ")
    if response == 'n':
        active = False
    elif response.lower() == 'y':
        active = True
    else:
        print("Invalid response.")
        response


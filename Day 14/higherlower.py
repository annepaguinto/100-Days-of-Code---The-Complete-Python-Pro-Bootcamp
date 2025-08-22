from game_data import data
import random
import art


def higher_lower():
    print(art.logo)

    correct_answer = ""
    score = 0
    game_over = False

    # TODO get random data for A and B
    a = random.choice(data)
    b = random.choice(data)
    back_up = random.choice(data)

    while not game_over:
        # TODO compare the correct answer

        if a == b:
            print('modified')
            b = back_up

        if a['follower_count'] > b['follower_count']:
            correct_answer = 'a'
        else:
            correct_answer = 'b'

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(art.vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

        # TODO get an input from the user and compare the answer
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}")

            a = b
            b = random.choice(data)

        else:
            game_over = True

    print(f"Sorry, that's wrong. Final score: {score}")

    play = input("Do you want to play again? Type 'Y' or 'N: ").lower()

    if play == 'y':
        higher_lower()
    else:
        print("Thank you for playing the game.")

higher_lower()


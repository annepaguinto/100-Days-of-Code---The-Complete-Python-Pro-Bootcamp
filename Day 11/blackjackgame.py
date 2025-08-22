import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_shuffler(count, selected_cards):
    """To add the randomized number to a 'selected_cards' list"""
    while count > 0:
        selected_cards.append(random.choice(cards))
        count -= 1
    return selected_cards

def calculate_score(score, selected_cards):
    """To get the sum of numbers from 'selected_cards' list"""
    for card in selected_cards:
        score += card
    return score

def blackjack():
    """Game Proper"""


    # Initial game data for player
    card_count = 2
    player_cards = []
    player_score = 0

    # Initial game data for the dealer
    computer_count = 2
    computer_cards = []
    computer_score = 0

    # Draw cards for the player and the dealer
    current_player_cards = card_shuffler(card_count, player_cards)
    current_computer_cards = card_shuffler(computer_count, computer_cards)

    # Calculate initial score of the player and the dealer
    player_final_score = calculate_score(player_score, player_cards)
    computer_final_score = calculate_score(computer_score, computer_cards)

    # To determine the ace value

    if 11 in current_player_cards:
        ace_position = current_player_cards.index(11)
        if player_final_score > 21:
            current_player_cards[ace_position] = 1

    if 11 in current_computer_cards:
        ace_position = current_computer_cards.index(11)
        if computer_final_score > 21:
            current_computer_cards[ace_position] = 1


    # Calculate initial score of the player and the dealer
    player_final_score = calculate_score(player_score, player_cards)
    computer_final_score = calculate_score(computer_score, computer_cards)


    # First output of the game

    print(f"Your cards: {current_player_cards}, current score: {player_final_score}")
    print(f"Computer's first card: {current_computer_cards[0]} ")


    def to_continue():
        """To ask the player whether to draw another card or exit the game"""
        draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if draw == 'y':
            current_player_cards.append(random.choice(cards))
            player_final_score = calculate_score(player_score, current_player_cards)
            computer_final_score = calculate_score(computer_score, current_computer_cards)

            if 11 in current_player_cards:
                ace_position = current_player_cards.index(11)
                if player_final_score > 21:
                    current_player_cards[ace_position] = 1

            if 11 in current_computer_cards:
                ace_position = current_computer_cards.index(11)
                if computer_final_score > 21:
                    current_computer_cards[ace_position] = 1

            player_final_score = calculate_score(player_score, current_player_cards)
            computer_final_score = calculate_score(computer_score, current_computer_cards)

            if player_final_score > 21:
                print(f"Your final hand: {current_player_cards}, final score: {player_final_score}")
                print(f"Computer's final hand: {current_computer_cards}, final score: {computer_final_score}")
                print(find_winner(player_final_score, computer_final_score))
            else:
                print(f"Your cards: {current_player_cards}, current score: {player_final_score}")
                to_continue()

        else:
            player_final_score = calculate_score(player_score, current_player_cards)
            computer_final_score = calculate_score(computer_score, current_computer_cards)

            # To determine the ace value
            if 11 in current_player_cards:
                ace_position = current_player_cards.index(11)
                if player_final_score > 21:
                    current_player_cards[ace_position] = 1

            if 11 in current_computer_cards:
                ace_position = current_computer_cards.index(11)
                if computer_final_score > 21:
                    current_computer_cards[ace_position] = 1

            if computer_final_score > 17:
                print(f"Your final hand: {current_player_cards}, final score: {player_final_score}")
                print(f"Computer's final hand: {current_computer_cards}, final score: {computer_final_score}")
                print(find_winner(player_final_score, computer_final_score))
            else:

                # if the dealer's score is 16 or less
                if computer_final_score < 17:
                    while computer_final_score < 17:
                        current_computer_cards.append(random.choice(cards))
                        computer_final_score = calculate_score(computer_score, current_computer_cards)

                if 11 in current_player_cards:
                    ace_position = current_player_cards.index(11)
                    if player_final_score > 21:
                        current_player_cards[ace_position] = 1

                if 11 in current_computer_cards:
                    ace_position = current_computer_cards.index(11)
                    if computer_final_score > 21:
                        current_computer_cards[ace_position] = 1

                player_final_score = calculate_score(player_score, current_player_cards)
                computer_final_score = calculate_score(computer_score, current_computer_cards)
                print(f"Your final hand: {current_player_cards}, final score: {player_final_score}")
                print(f"Computer's final hand: {current_computer_cards}, final score: {computer_final_score}")
                print(find_winner(player_final_score, computer_final_score))

    if player_final_score == 21:
        print(find_winner(player_final_score, computer_final_score))
    else:
        to_continue()


def find_winner(user_score, dealer_score):

    """To compare the final scores and declare the result"""
    if user_score == 21:
        return "Blackjack! You win! :)"
    elif dealer_score == 21:
        return "Blackjack! You lose :("
    elif user_score > 21:
        return 'Dealer wins. You lose :('
    elif dealer_score > 21:
        return "You win! :)"
    elif user_score == dealer_score:
        return "It's a tie. :)"
    elif user_score < 21 > dealer_score:
        if user_score > dealer_score:
            return "You win!"
        else:
            return "You lose. :("

session = True
while session:
    print(art.logo)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == 'y':
        print("=============Welcome to the Blackjack game!==================")
        blackjack()
    else:
        session = False
        print("Thank you for playing Blackjack!")

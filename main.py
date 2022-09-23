import random

points = 0
computer_points = 0
player_hand = []
computer_hand = []
cards = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts',
         '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts',
         '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds',
         '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds',
         'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs',
         '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs',
         '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades',
         '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3,
          2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]


def hit_or_stand():
    global cards
    global points
    global values
    global player_hand
    global computer_hand
    global computer_points
    next_move = input("(h)it or (s)tand? ")
    while next_move == 'h':
        number = random.randint(0, len(cards))
        new_card = cards.pop(number)
        player_hand.append(new_card)
        points += values[number]
        values.pop(number)
        print(f"Player drew {new_card}")
        print(f"Player hand: {player_hand} is worth {points}")
        if points > 21:
            print("Bust!")
            print("Computer wins!")
            break
        elif points < 21:
            next_move = input("(h)it or (s)tand? ")
        elif points == 21:
            print("Player got 21! Blackjack!")
            print("Player wins!")
            break
    if next_move == 's':
        for x in range(2):
            rand = random.randint(0, len(cards))
            computer_hand.append(cards[rand])
            computer_points += values[rand]
            cards.pop(rand)
            values.pop(rand)
        print(f"\nComputer hand: {computer_hand} is worth {computer_points}")
        while True:
            lucky_num = random.randint(0, len(cards))
            computer_card = cards.pop(lucky_num)
            computer_hand.append(computer_card)
            computer_points += values[lucky_num]
            values.pop(lucky_num)
            print(f"Computer drew {computer_card}")
            print(f"Computer hand: {computer_hand} is worth {computer_points}")
            if points < computer_points < 21:
                print("Computer wins!")
                break
            elif computer_points == 21:
                print("Computer got 21! Blackjack!")
                print("Computer wins!")
                break
            elif computer_points > 21:
                print("Bust!")
                print("Player wins!")
                break
            elif computer_points < points and computer_points <= 21:
                continue


def main():
    global cards
    global points
    global values
    global player_hand

    for x in range(2):
        num = random.randint(0, len(cards))
        points += values[num]
        player_hand.append(cards[num])
        del cards[num]
        del values[num]
    print(f"Player hand: {player_hand} is worth {points}")
    hit_or_stand()


if __name__ == '__main__':
    main()

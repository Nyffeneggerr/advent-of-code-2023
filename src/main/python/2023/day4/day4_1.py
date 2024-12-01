

def read_cards():
    with open('cards.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    cards = read_cards()
    total_points = 0
    for card in cards:
        count_wins = 0
        card_points = 0
        winning_numbers = card.split(':')[1].split('|')[0].split()
        my_numbers = card.split(':')[1].split('|')[1].split()
        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                count_wins += 1

        print(count_wins)
        if count_wins > 0:
            card_points = 2 ** (count_wins-1)

        total_points += card_points

    print(total_points)

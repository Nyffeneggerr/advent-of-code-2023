

def read_cards():
    with open('cards.txt') as file:
        return [line.rstrip() for line in file]


def number_of_wins_for_card(card):
    count_wins = 0
    winning_numbers = card.split(':')[1].split('|')[0].split()
    my_numbers = card.split(':')[1].split('|')[1].split()
    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            count_wins += 1

    return count_wins


if __name__ == '__main__':
    cards = read_cards()
    total_cards = 0
    card_amounts = {}

    for index, card in enumerate(cards):
        card_amounts[index+1] = 1

    for index, card in enumerate(cards):
        current_card_number = index + 1
        wins = number_of_wins_for_card(card)
        value_to_add = card_amounts[current_card_number]

        next_card_number = current_card_number + 1
        for number in range(wins):
            card_amounts[next_card_number] = card_amounts[next_card_number] + value_to_add
            next_card_number += 1

    for card_amount in card_amounts.values():
        total_cards += card_amount

    print(total_cards)
